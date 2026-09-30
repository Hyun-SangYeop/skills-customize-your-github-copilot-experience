# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API using FastAPI to learn how to define routes, handle JSON data, and build simple web endpoints for managing application data.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a basic FastAPI application and configure a root endpoint that responds with a welcome message.

#### Requirements
Completed program should:

- Import and initialize a `FastAPI` app.
- Create an endpoint such as `/` that returns a welcome message in JSON.
- Run the app locally with a development server.
- Example output:
  ```json
  {"message": "Welcome to the FastAPI API!"}
  ```

### 🛠️ Create Item Endpoints

#### Description
Add endpoints to retrieve and create items in a simple in-memory list.

#### Requirements
Completed program should:

- Define a `GET /items` endpoint that returns all current items.
- Define a `POST /items` endpoint that accepts JSON data.
- Store new items in an in-memory list for the current session.
- Example request body:
  ```json
  {
    "name": "Laptop",
    "price": 999.99,
    "in_stock": true
  }
  ```

### 🛠️ Validate Requests and Responses

#### Description
Improve the API by validating incoming data and returning structured responses.

#### Requirements
Completed program should:

- Use a Pydantic model to define the request shape.
- Require fields such as `name`, `price`, and `in_stock`.
- Return a clear JSON response after creating an item.
- Example response:
  ```json
  {
    "name": "Laptop",
    "price": 999.99,
    "in_stock": true
  }
  ```
