create a datbase in PostgreSQL by right clicking on the default Postgres server in the default workspace...here the one used is builder_books.

after creating a table, it can be found under Schemas > public > Tables

serial primary key - generates a unique, incrementing id automatically

varchar(n) - text field capped at n characters.

not null - this field is required, can't be left empty on insert.

'column1 name' type references 'another table(column2 name)' - makes a foreign key that states that whatever exists in that column must correspond to the other column of the other table.

default - assigns a default value in case the field is left empty

unique - a constraint that means no two rows can have the same value in this column.

date — a data type for storing just a calendar date, no time component.