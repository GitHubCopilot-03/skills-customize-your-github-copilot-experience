# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI that supports creating, reading, updating, and deleting resources. By completing this assignment, you will practice API route design, request validation, and structured JSON responses.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI app with a health-check endpoint and a simple in-memory data store for books.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Define a `GET /health` endpoint that returns `{ "status": "ok" }`.
- Store books in memory using a list or dictionary.
- Include at least the fields `id`, `title`, and `author` for each book.

### 🛠️ Implement CRUD Endpoints

#### Description
Add REST endpoints to create, list, update, and delete books.

#### Requirements
Completed program should:

- Implement `POST /books` to add a new book.
- Implement `GET /books` to return all books.
- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return meaningful error responses for missing book IDs.

### 🛠️ Add Input Validation with Pydantic

#### Description
Use Pydantic models for request validation and response structure.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming book data.
- Validate that required fields are provided.
- Return JSON responses with clear keys and values.
- Keep endpoint behavior consistent for valid and invalid requests.
