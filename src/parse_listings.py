"""Turn the 152 raw listing exports into one clean table of unique places.

Why this is needed
- The browser export names columns after page elements (OSrXXb, rllt__details ...),
  and the same information lands in different columns from file to file.
- Searches for neighbouring areas overlap, so most places appear in several files.

What it does
1. Reads every CSV in data/raw/listings_surabaya/.
2. Works out what each cell IS from its content (price, status, hours, address).
3. Keeps one row per place (same name + same address), with the highest review count seen.
4. Writes data/interim/places.csv (ignored by Git).

Run from the project root:  python src/parse_listings.py
"""
import csv
import hashlib
import re
from pathlib import Path

RAW_DIR = Path("data/raw/listings_surabaya")
OUT_FILE = Path("data/interim/places.csv")

STATUS_WORDS = {"Closed", "Closes soon", "Temporarily closed", "Permanently closed",
                "Open now", "Opens soon", "Open 24 hours"}
DETAIL_COLUMNS = ["rllt__details 2", "rllt__details 3", "rllt__details 4", "rllt__details 5"]
PLUS_CODE = re.compile(r"\b[23456789CFGHJMPQRVWX]{4}\+[23456789CFGHJMPQRVWX]{2,3}\b")
REVIEWS = re.compile(r"^\(([\d.,]+)([KkMm]?)\)$")


def parse_reviews(text):
    """'(258)' -> 258, '(1,2K)' -> 1200. Returns None when the cell is not a review count."""
    match = REVIEWS.match(text.strip())
    if not match:
        return None
    number, suffix = match.groups()
    if suffix:  # abbreviated: comma is a decimal mark
        return int(float(number.replace(",", ".")) * {"k": 1_000, "m": 1_000_000}[suffix.lower()])
    return int(number.replace(".", "").replace(",", ""))


def parse_row(row):
    """Return a clean dict for one listing, or None for junk rows (page menus, blanks)."""
    name = (row.get("OSrXXb") or "").strip()
    if not name:
        return None
    place = {
        "name": name,
        "category": re.sub(r"^[·\s]+", "", row.get("rllt__details") or "").strip(),
        "reviews": parse_reviews(row.get("RDApEe") or ""),
        "address": "", "price_band": "", "status_at_collection": "",
    }
    for column in DETAIL_COLUMNS:
        value = (row.get(column) or "").strip()
        if not value:
            continue
        if value == "No reviews":
            place["reviews"] = 0
        elif value.startswith("Rp"):
            place["price_band"] = value.replace("\xa0", " ")
        elif value in STATUS_WORDS:
            place["status_at_collection"] = value
        elif value.startswith("·") or re.search(r"\d\.\d\d\s?[ap]m", value):
            continue                      # opening-hours fragment: not used
        elif not place["address"]:
            place["address"] = value
    code = PLUS_CODE.search(place["address"])
    place["plus_code"] = code.group(0) if code else ""
    return place


def main():
    files = sorted(RAW_DIR.glob("*.csv"))
    best, batches, rows_read, rows_kept = {}, {}, 0, 0
    for file in files:
        with open(file, newline="", encoding="utf-8-sig") as handle:
            for row in csv.DictReader(handle):
                rows_read += 1
                place = parse_row(row)
                if place is None:
                    continue
                rows_kept += 1
                key = (place["name"].lower(), place["address"].lower())
                batches.setdefault(key, set()).add(file.name)
                current = best.get(key)
                if current is None or (place["reviews"] or -1) > (current["reviews"] or -1):
                    best[key] = place

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    columns = ["place_key", "name", "category", "reviews", "address", "plus_code",
               "price_band", "status_at_collection", "n_search_batches"]
    with open(OUT_FILE, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for key, place in sorted(best.items()):
            place["place_key"] = hashlib.md5("|".join(key).encode()).hexdigest()[:12]
            place["n_search_batches"] = len(batches[key])
            place["reviews"] = "" if place["reviews"] is None else place["reviews"]
            writer.writerow({c: place[c] for c in columns})

    print(f"Files read:        {len(files)}")
    print(f"Rows read:         {rows_read}")
    print(f"Junk rows dropped: {rows_read - rows_kept}")
    print(f"Duplicate rows:    {rows_kept - len(best)}")
    print(f"Unique places:     {len(best)}  ->  {OUT_FILE}")


if __name__ == "__main__":
    main()
