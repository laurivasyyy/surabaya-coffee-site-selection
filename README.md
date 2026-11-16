# Surabaya Coffee Market Map: Structure, Saturation and White Space

> Work in progress.

**Questions**
1. What is Surabaya's coffee market made of (warkop, independent cafés, specialty, chains)?
2. Where is it saturated, and where is it thin, relative to demand?
3. Where should a specialty coffee chain open next?

**Data:** about 17,700 coffee-related listings collected from Google local search results (raw rows not
published; see `data/manual/README.md`), plus open data: Overture Maps, OpenStreetMap, HDX boundaries,
BPS population.

**Stack:** Python · SQL Server · LLM classification · Power BI

**Rebuild the working table:** `python src/parse_listings.py`
