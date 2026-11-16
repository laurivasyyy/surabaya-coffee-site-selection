# Data sources and collection log

## Listings (data/raw/listings_surabaya/ — not published)
- **What:** coffee-related business listings for Kota Surabaya: name, category, review count, address,
  price band, status at collection.
- **Source:** Google local search results.
- **How:** searched area by area (see `search_kelurahan.csv`, 153 kelurahan) and exported each results list
  with a browser table-export extension, 14–16 Nov 2026. 152 export files, 28,527 rows.
- **Use:** the raw rows stay on the author's machine and are excluded from this repository.
  Only aggregated results (district-level tables, charts) are published.
- **Known limits:** no coordinates, no star ratings, no stable place ID; overlapping searches (deduplicated by
  name + address); category noise (restaurants, malls, convenience stores appear in results);
  review counts favour older places.

## search_kelurahan.csv
The 153 kelurahan used as search areas. Names and codes from Surabaya's open-data portal
(ckan.surabaya.go.id, "Jumlah Kelurahan", December 2023). Two kelurahan are both named "Wonorejo"
(Rungkut and Tegalsari).

## Open data
- Overture Maps Places (CDLA Permissive 2.0 / Apache 2.0): used to borrow coordinates by name matching.
- OpenStreetMap (ODbL): roads for street-to-district matching; universities, offices, malls as demand drivers.
- HDX COD-AB boundaries and BPS Kota Surabaya population.
