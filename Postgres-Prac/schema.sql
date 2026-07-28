/* creating tables ... and later refining the design */


CREATE TABLE categories (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);

CREATE TABLE books (
id SERIAL PRIMARY KEY,
title VARCHAR(100) NOT NULL,
category_id INTEGER REFERENCES categories(id),
price NUMERIC(6,2) NOT NULL,
stock INTEGER NOT NULL DEFAULT 0
);

--
CREATE TABLE borrowers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE borrow_records (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    borrower_id INTEGER REFERENCES borrowers(id),
    borrow_date DATE NOT NULL DEFAULT CURRENT_DATE,
    return_date DATE
);



ALTER TABLE books ADD CONSTRAINT price_positive CHECK (price > 0);

CREATE VIEW book_details AS
SELECT books.title, categories.name AS category, books.price, books.stock
FROM books
JOIN categories ON books.category_id = categories.id;

CREATE INDEX idx_books_category ON books(category_id);