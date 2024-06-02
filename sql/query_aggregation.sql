--get count on rows, and average publish date
SELECT COUNT (*) AS book_count, 
AVG(year_published) AS average_year_published FROM books;