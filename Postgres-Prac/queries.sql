/* 3 - filtering queries */


-- Books under $15 (WHERE + comparison)
SELECT * FROM books WHERE price < 15;

-- Books with "The" in the title (LIKE)
SELECT * FROM books WHERE title LIKE '%The%';

-- Books priced between 12 and 20 (BETWEEN)
SELECT * FROM books WHERE price BETWEEN 12 AND 20;

-- Books in scifi or mystery categories (IN)
SELECT * FROM books WHERE category_id IN (1, 4);

-- Top 3 most expensive books (ORDER BY + LIMIT)
SELECT * FROM books ORDER BY price DESC LIMIT 3;