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