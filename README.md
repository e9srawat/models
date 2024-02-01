
## Models Assignment

### 1. Create a model for Profile containing following fields:
- slug
- username
- email
- phone
- address

### 2. Create a model for Author containing following fields:
- slug
- name
- profile [one to one to Profile]

### 3. Create a model for Publisher containing following fields:
- slug
- name
- website
- email
- address

### 4. Create a model for Book containing following fields:
- slug
- author [foreign key to Author]
- title
- publisher [foreign key to Publisher]
- date_of_pub


### 5. Create a model for Collection containing following fields:
- slug
- name
- book [many to many to Book]

## Queries (Write the functions for each query in respective model classes)

### 0. Write functions to generate random data and do a bulk insert to fill these models. It should have 50000 rows for each model.
### 1. Return the list containing the names of the authors.
### 2. Return the list containing the name and full profile detail (use related_name).
### 3. Return the list of books written by authors whose name starts with 'a'.
### 4. Return the list of the books written by a given author_name.
### 5. Return the list of authors who written more than 2 books.
### 6. Return the list of books written by a given author_name and publisher_name.
### 7. Return the list of books written by author whose name ends with 'a'.
### 8. Return the list of books published in a given year.
### 9. Return the list of books for a given publisher_name.
### 10. Return the object and status for given parameters of Book model by either creating the object if exists or create new object.
### 11. Return the profile details if author name matched to given input (input can case insensitive).
### 12. Return all the books published by a given publisher name.
### 13. Return all the books published by a given publisher website.
### 14. Return the dictionary containing the author as key and no. of books written by them (query should by optimized, look for annotate and count).
### 15. Return the list of books published by given publishers (input will be list of publisher names).
### 16. Return the list of books written by the author A and author B using Q object.
### 17. Return the list of books excluding a given author.
### 18. Delete a book if exist and return the status.
### 19. Add ```is_deleted``` boolean field in Book model and migrate.
### 20. Soft delete a book if exist and return the status.
### 21. Add unique constraint for Publisher name and migrate.
### 21. Add unique together constraint for author, title and date_of_pub.
### 22. Add ordering for Book model on date_of_pub.
### 23. Add verbose_name for all models in the Meta class.
### 24. Research and change the database table name for Collection as ``` book_collection ``` 
### 25. Add field ```genre``` in Book model, which should only accept from a list of choices ['horror', 'self help', 'adventure', 'others'].
### 26. Make email field as Primary key in Profile model.

## NOTE: Slug will auto generated slug field.