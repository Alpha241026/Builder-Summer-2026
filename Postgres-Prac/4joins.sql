/* relational queries; unifying matching tables for readability */


SELECT borrowers.name, books.title, borrow_records.borrow_date
FROM borrow_records
INNER JOIN borrowers ON borrow_records.borrower_id = borrowers.id
INNER JOIN books ON borrow_records.book_id = books.id;


SELECT books.title, borrow_records.borrow_date
FROM books
LEFT JOIN borrow_records ON books.id = borrow_records.book_id;


SELECT borrowers.name AS borrower, books.title AS book, borrow_records.borrow_date, borrow_records.return_date
FROM borrow_records
JOIN borrowers ON borrow_records.borrower_id = borrowers.id
JOIN books ON borrow_records.book_id = books.id
ORDER BY borrow_records.borrow_date;
