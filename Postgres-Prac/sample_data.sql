/* 2 - adding real data in the created tables */


INSERT INTO categories (name) VALUES
('scifi'),
('fantasy'),
('nonfiction'),
('mystery');

INSERT INTO books (title, category_id, price, stock) VALUES
('Dune', 1, 15.00, 12),
('1984', 1, 10.00, 8),
('Neuromancer', 1, 14.00, 6),
('The Hobbit', 2, 12.00, 20),
('A Game of Thrones', 2, 25.00, 14),
('Sapiens', 3, 20.00, 15),
('Educated', 3, 18.00, 11),
('Thinking, Fast and Slow', 3, 22.00, 5),
('The Silent Patient', 4, 16.00, 9),
('The Girl with the Dragon Tattoo', 4, 13.00, 18);

INSERT INTO borrowers (name, email) VALUES
('Alex Kumar', 'alex.kumar@example.com'),
('Priya Sharma', 'priya.sharma@example.com'),
('Rahul Verma', 'rahul.verma@example.com'),
('Sara Ahmed', 'sara.ahmed@example.com'),
('Vikram Singh', 'vikram.singh@example.com');

INSERT INTO borrow_records (book_id, borrower_id, borrow_date, return_date) VALUES
(1, 1, '2026-06-10', '2026-06-24'),
(3, 1, '2026-07-01', NULL),
(5, 2, '2026-06-15', '2026-06-30'),
(6, 3, '2026-07-05', NULL),
(9, 4, '2026-06-20', '2026-07-01'),
(2, 5, '2026-07-10', NULL);