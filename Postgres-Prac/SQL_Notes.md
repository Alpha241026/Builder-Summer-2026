create a datbase in PostgreSQL by right clicking on the default Postgres server in the default workspace...here the one used is builder_books.

after creating a table, it can be found under Schemas > public > Tables

serial primary key - generates a unique, incrementing id automatically

varchar(n) - text field capped at n characters.

not null - this field is required, can't be left empty on insert.

'column1 name' type references 'another table(column2 name)' - makes a foreign key that states that whatever exists in that column must correspond to the other column of the other table.

default - assigns a default value in case the field is left empty

unique - a constraint that means no two rows can have the same value in this column.

date — a data type for storing just a calendar date, no time component.

insert -  multiple rows inserted in one statement using comma-separated value groups;
the order matters when foreign keys exist...eg : categories -> books -> borrowers -> borrow_records, since books/borrow_records reference ids that must already exist in the tables they point to.

select * from table_name - returns all the columns and their data in a tabular format

null - doesn't mean empty....but no value recorded

where - core row filter, same idea as Flask's QUERY filtering logic, now done at the database level instead of a Python loop.

like '%text%' - pattern match, % = wildcard (any length). Case-sensitive by default in Postgres.

between x and y - inclusive range, shorthand for >= x and <= y.

in (a, b, c) - shorthand for multiple OR conditions on the same column.

order by col desc/asc - sorting. asc is default, can be omitted.

limit n - caps result count, commonly paired with ORDER BY for "top N" queries.

inner join table2 on t1.col = t2.col - matches rows across tables using a shared key, same "find matching id" logic used in Flask's loops, now done declaratively at the database level, automatically, for every row.

left join table2 on t1.col = t2.col - keeps every row from the left (base) table regardless of a match; unmatched rows get NULL on the right side's columns instead of being dropped. Answers "what's missing" type questions (e.g. books never borrowed) that inner join structurally can't show.

join (no keyword before it) - defaults to inner join, same meaning, shorter syntax.

as - renames a column just for the output display, purely cosmetic.

which table goes in FROM matters for left join specifically - it determines which side's rows are always kept regardless of a match.

count(*) - counts rows. IS NULL / IS NOT NULL required for null checks (not = NULL, since NULL means "unknown," so equality never matches it, even against another NULL).

sum(col), avg(col), min(col), max(col) - math functions across a column; min/max can be combined in one SELECT since they're independent calculations.

group by col - splits rows into buckets by a shared column value, then runs aggregate functions (COUNT, SUM, etc.) separately within each bucket instead of once across the whole table. SQL's declarative version of
manually grouping items into a dict before counting in Python.

having condition - filters groups AFTER aggregation has happened, unlike WHERE which filters individual rows BEFORE grouping. Needed because COUNT(*)/SUM(...) don't exist yet at the point WHERE runs.

check (condition) - constraint with logic, not just existence/uniqueness.

alter table t add constraint name check (...) - modifies an existing table.

create view name as (select ...) - saves a query under a name, queryable like a table. No data copy - re-runs live each time.

create index on table(col) - speeds up lookups on that column at scale; no visible effect on small tables.