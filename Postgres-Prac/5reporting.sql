/* aggregate reporting */


SELECT COUNT(*) FROM books;
SELECT COUNT(*) FROM borrow_records WHERE return_date IS NULL;


SELECT SUM(stock) FROM books;
SELECT AVG(price) FROM books;
SELECT MIN(price), MAX(price) FROM books;


SELECT category_id, COUNT(*) FROM books GROUP BY category_id;


SELECT borrowers.name, COUNT(*) AS times_borrowed
FROM borrow_records
JOIN borrowers ON borrow_records.borrower_id = borrowers.id
GROUP BY borrowers.name
ORDER BY times_borrowed DESC;


SELECT borrowers.name, COUNT(*) AS times_borrowed
FROM borrow_records
JOIN borrowers ON borrow_records.borrower_id = borrowers.id
GROUP BY borrowers.name
HAVING COUNT(*) > 1;