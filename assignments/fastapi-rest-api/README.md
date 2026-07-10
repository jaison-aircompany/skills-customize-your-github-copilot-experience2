# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using FastAPI to practice route creation, request validation, and standard CRUD operations.

## 📝 Tasks

### 🛠️ Set Up a FastAPI Application

#### Description
Create a FastAPI app with a health check route and a basic in-memory data store for books.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Implement `GET /health` that returns `{ "status": "ok" }`
- Define a `BookCreate` model with `title`, `author`, and `year`
- Use a list to store book records while the server is running


### 🛠️ Implement CRUD Endpoints

#### Description
Add endpoints to create, read, update, and delete books in the API.

#### Requirements
Completed program should:

- Implement `POST /books` to create a new book with an auto-incrementing `id`
- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return one book or 404 if not found
- Implement `PUT /books/{book_id}` to update an existing book
- Implement `DELETE /books/{book_id}` to remove a book and return a confirmation message
