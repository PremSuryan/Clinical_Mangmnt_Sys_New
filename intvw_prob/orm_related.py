"""
ORM Concepts:
question:---.how to reduce database queries and avoid the N+1 Query Problem.

1.select_related()
2.prefetch_related()


ORM stands for Object Relational Mapper.
Instead of writing SQL like

SELECT * FROM student;

you write Python

students = Student.objects.all()

Django converts it into SQL

we have two models
class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


Normal Query
books = Book.objects.all()

for book in books:
    print(book.title)
    print(book.author.name)



Query 1
SELECT * FROM book;

Gets

Python
Django
Java

Now loop starts.

For first book

book.author.name

Django executes

SELECT * FROM author
WHERE id=1;

Second book

Again

SELECT * FROM author
WHERE id=1;

Third book

SELECT * FROM author
WHERE id=2;

Total Queries

1 + 3 = 4

If there were

100 books

Total

101 Queries

This is called

N+1 Query Problem

Solution is # select_related()
    """
"""
Solution 1
select_related()

Suppose

books = Book.objects.select_related("author")

Now Django performs

ONE SQL query

SELECT
book.*,
author.*
FROM book

INNER JOIN author

ON book.author_id=author.id;

Now everything is already fetched.

Loop

for book in books:
    print(book.author.name)

No more SQL queries.

Total

1 Query
"""

"""
When to use select_related?

Only for

ForeignKey

OneToOneField
"""

#2.prefetch_related():

"""
when to use prefetch_related()
prefetch_related()

You ask:

"Give me the list of teachers and also the list of all students."

The office gives you two separate sheets. You then match each student to their teacher yourself (this is what Django does in Python).
"""

"""

class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

Suppose

We start from Author.

authors = Author.objects.all()

for author in authors:
    print(author.book_set.all())


    Again

N+1 problem.
"""

#Solution:

"""

Solution

authors = Author.objects.prefetch_related("book_set")


Note:    print(author.book_set.all()) and Author.objects.prefetch_related("book_set")
book_set.all()and "book_set"  ----> are same
"""

"""
Why not use JOIN here?

Suppose

One author

has

100 books.

A JOIN would repeat the author's information for every book:

John Python

John Django

John Flask

John FastAPI

The author data is duplicated many times.

Instead, prefetch_related() fetches authors once and books once, then links them in memory.
"""


"""
When to use prefetch_related()

Use for

ManyToManyField

Reverse ForeignKey
"""