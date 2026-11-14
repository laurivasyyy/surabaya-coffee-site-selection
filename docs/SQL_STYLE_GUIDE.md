# SQL Style Guide

The standard every SQL file in this repo follows (SQL Server / T-SQL).

## 1. Files
- Name: `NN_verb_object.sql`, numbered in run order.
- Every file runs top to bottom on a fresh server and can be re-run safely:
  `IF DB_ID(...) IS NULL`, `DROP TABLE IF EXISTS`, `CREATE OR ALTER VIEW`, `TRUNCATE` before load.
- Every file starts with this header:

```sql
/* =====================================================================
   NN_file_name.sql
   Purpose : what this file produces, in one or two lines
   Source  : input tables  ->  output tables/views
   Re-runnable: yes
   ===================================================================== */
```

## 2. Layers
| Schema | Holds | Rule |
| --- | --- | --- |
| `raw` | Data exactly as loaded, all `VARCHAR`/`NVARCHAR` | Never rejects a row |
| `clean` | Real types, trimmed text, constraints | Guarantees every row; bad data fails loudly |
| `mart` | Views for analysis, Python and Power BI | Business logic defined once |

Row counts are reconciled across layers after every build.

## 3. Naming
- `snake_case` for everything; units in the name (`area_km2`, `cafes_per_10k`).
- Constraints: `pk_<table>`, `fk_<table>_<ref>`, `ck_<table>_<column>`.
- Views: `v_<content>`. CTEs: descriptive nouns (`ranked`, `scored`, `joined`).
- Never use reserved or built-in names as aliases: `rank`, `order`, `user`, `date`, `count`, `value`.
- No symbols in column aliases (`pct_chain`, not `[%chain]`).

## 4. Formatting
- Keywords UPPERCASE; 4-space indent; one column per line in SELECT lists.
- **Every statement ends with `;`** (a CTE must follow a terminated statement).
- `GO` only where T-SQL requires a new batch: after `CREATE DATABASE`, after `USE`,
  before and after `CREATE VIEW` / `CREATE PROCEDURE`.
- Use `NVARCHAR` for names (Indonesian place names can contain non-ASCII characters).

## 5. Numbers
| Situation | Do | Don't |
| --- | --- | --- |
| Average of an integer column | `AVG(CAST(col AS DECIMAL(10,2)))` | `AVG(col)` (truncated integer) |
| Percentage | `CAST(100.0 * part / total AS DECIMAL(5,1))` | `part * 100 / total` |
| Division that could hit 0 | `/ NULLIF(denominator, 0)` | plain `/` |
| Display rounding | `CAST(... AS DECIMAL(p,1))` | `ROUND()` on a float |
| Type sizing | Fit the realistic domain | Fit only today's sample |

## 6. Window functions
- `ORDER BY` inside `OVER()` must be deterministic: add a unique tie-breaker.
- `ROW_NUMBER()` 1,2,3 (exactly N rows) · `RANK()` 1,1,3 · `DENSE_RANK()` 1,1,2.
- `SUM(COUNT(*)) OVER ()` = share of total in a grouped query.

## 7. Results
- Every final SELECT has an explicit `ORDER BY`.
- Categorical bands carry a sort column so tools never sort them alphabetically.
- Show counts **and** percentages together; flag groups with n < 10.

## 8. Analytical comments
```sql
/* QUESTION : the business question, in plain words
   TECHNIQUE: the SQL concept it demonstrates
   INSIGHT  : what the result means for the business, with numbers */
```
An insight interprets; it does not restate the table. Every number in it is checked against the result.

## 9. Data quality
- Load scripts end with checks: row count, duplicate keys, NULLs per column, value ranges,
  conversion failures, distinct values of categorical columns.
- Every check's result is recorded in the project report.
