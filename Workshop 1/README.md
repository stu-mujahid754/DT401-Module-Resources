# Workshop 1: Introduction to SQL and Programming

SQL — Structured Query Language — is the standard language for communicating with relational databases. Whatever sector you work in, there will be databases that respond to SQL. They are commonly used to store:

- patient records
- transaction histories
- planning data
- customer information

Learning to query a database directly gives you the ability to extract exactly the data you need, without depending on someone else to run it for you.

This workshop introduces SQL through hands-on practice. The skills you develop here are foundational — you will use them throughout DT401 and in subsequent modules. Developing familiarity with relational database systems will also support your reflective writing for the **DT401 Module Challenge**, where you will need to discuss data management systems and their role in digital and technology solutions.

---

## What you will be working with

The **pagila database** models a fictional DVD rental business with brick-and-mortar locations, similar to Blockbuster or a public library. The database contains tables for customers, films, payments, rentals, and store locations. As you explore pagila, consider what equivalent tables and relationships might look like in your own sector.

See the [ERD notebook](ERD.ipynb) for a full view of the database schema.

---

## How to use these notebooks

Each notebook covers a different SQL topic and contains:

- **Explanation cells** that introduce new concepts
- **Practice questions** for you to write and run SQL queries
- **Solution dropdowns** you can open if you get stuck

**Running a code cell:** select it, then either click the **Run** button, press `Ctrl + Enter` to run and stay, or press `Shift + Enter` to run and move to the next cell.

**Important:** each notebook begins with a setup cell that connects to the database. Run this cell first before attempting any questions. If your kernel restarts, run the setup cell again.

---

## Choose your learning path

### I have never coded before

SQL is a good place to start — its syntax reads almost like English, and if you have used Excel formulas you will find many ideas familiar.

**Suggested path:** Work through notebooks [1 - Selecting Data](1_selecting_data.ipynb), [2 - Filtering Data](2_filtering_data.ipynb), and [3 - Sorting and Aggregating](3_sorting_and_aggregating.ipynb) in order. That is a solid foundation — return to the remaining notebooks as you need them.

### I have coded before, but not in SQL

SQL is a specialised query language designed for databases. The logic will feel familiar; the syntax is new.

**Suggested path:** Start with [1 - Selecting Data](1_selecting_data.ipynb) to get oriented, then work through notebooks 2 and 3 at your own pace. Try [4 - Joins](4_joins.ipynb) if time allows.

### I have used SQL before, but not other programming languages

Focus on running SQL inside a Jupyter notebook and exploring how it connects to Python.

**Suggested path:** Skim [1 - Selecting Data](1_selecting_data.ipynb) to get comfortable with the notebook setup, work through [4 - Joins](4_joins.ipynb) and [5 - Subqueries and Tables](5_subqueries_and_tables.ipynb), then explore [7 - SQL Interactions in Python](7_sql_interactions.ipynb).

### I have used both SQL and other programming languages

The main new concept here is running SQL within a Jupyter notebook alongside Python.

**Suggested path:** Glance at [1 - Selecting Data](1_selecting_data.ipynb) to understand the JupySQL setup, try the harder questions in [6 - Advanced Practice](6_advanced_practice.ipynb), then review [7 - SQL Interactions in Python](7_sql_interactions.ipynb) for the SQLAlchemy and pandas integration you will use in DT402.

---

## Notebooks in this workshop

| Notebook | Topic | Level |
|:---------|:------|:------|
| [1 - Selecting Data](1_selecting_data.ipynb) | `SELECT`, `FROM`, `LIMIT`, `COUNT`, `DISTINCT` | Beginner |
| [2 - Filtering Data](2_filtering_data.ipynb) | `WHERE`, `AND`, `OR`, `IN`, `BETWEEN`, `LIKE`, `NULL` | Beginner |
| [3 - Sorting and Aggregating](3_sorting_and_aggregating.ipynb) | `ORDER BY`, `GROUP BY`, `HAVING`, aggregate functions | Intermediate |
| [4 - Joins](4_joins.ipynb) | `LEFT JOIN`, `INNER JOIN`, combining with other keywords | Intermediate |
| [5 - Subqueries and Tables](5_subqueries_and_tables.ipynb) | Subqueries, `CREATE TABLE`, `DROP TABLE` | Intermediate |
| [6 - Advanced Practice](6_advanced_practice.ipynb) | Complex multi-table queries, `CASE`, `CONCAT`, `strftime` | Advanced |
| [7 - SQL Interactions in Python](7_sql_interactions.ipynb) | SQLAlchemy, pandas `read_sql` / `to_sql` | Advanced |
| [ERD - Database Schema](ERD.ipynb) | Entity Relationship Diagram of the pagila database | Reference |
| [SQLite Table Identification](SQLite_table_identification.ipynb) | Exploring database structure with SQLite-specific functions | Reference |