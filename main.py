import os
import psycopg
from psycopg.rows import dict_row
from fastapi import FastAPI, HTTPException


app = FastAPI()


def get_connection():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="library_db",
        user="postgres",
        password=os.environ["DB_PASSWORD"],
        row_factory=dict_row,
    )
    

@app.get("/books")
def get_information_books():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT title FROM books ORDER BY id;"
            )
            books = cursor.fetchall()

    return [book["title"] for book in books]

@app.post("/books")
def create_book(title_new_book: str, author_new_book: str):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO books (title, author)
                VALUES (%s, %s)
                RETURNING id, title, author;
                """,
                (title_new_book, author_new_book),
            )

            new_book = cursor.fetchone()

    return {
        "Message": "The book was successfully registered.",
        "book Information": new_book,
    }

@app.get("/books/{id_book}")
def get_book(id_book: int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, title, author
                FROM books
                WHERE id = %s;
                """,
                (id_book,),
            )

            book = cursor.fetchone()

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return {
        "title": book["title"],
        "author": book["author"],
    }


@app.patch("/books/{id_book}")
def update_book(
    id_book: int,
    title: str | None = None,
    author: str | None = None,
):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, title, author
                FROM books
                WHERE id = %s;
                """,
                (id_book,),
            )

            book = cursor.fetchone()

            if book is None:
                raise HTTPException(
                    status_code=404,
                    detail="Book id not found",
                )

            if title is not None:
                cursor.execute(
                    "UPDATE books SET title = %s WHERE id = %s;",
                    (title, id_book),
                )

            if author is not None:
                cursor.execute(
                    "UPDATE books SET author = %s WHERE id = %s;",
                    (author, id_book),
                )

            cursor.execute(
                """
                SELECT id, title, author
                FROM books
                WHERE id = %s;
                """,
                (id_book,),
            )

            updated_book = cursor.fetchone()

    return {
        "Message": "The book was successfully updated.",
        "book Information": {
            "title": updated_book["title"],
            "author": updated_book["author"],
        },
    }

@app.delete("/books/{id_book}")
def delete_book(id_book: int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM books
                WHERE id = %s
                RETURNING id;
                """,
                (id_book,),
            )

            deleted_book = cursor.fetchone()

    if deleted_book is None:
        raise HTTPException(
            status_code=404,
            detail="Book id not found",
        )

    return "The book was successfully deleted."
