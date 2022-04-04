# FastAPI tutorial

## What is FastAPI

FastAPI framework, high performance, easy to learn, fast to code, ready for production



FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.


## Technical Stacks

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [sqladmin](https://github.com/aminalaee/sqladmin)
- [Uvicorn](https://www.uvicorn.org/)

## Required

- Python 3.9

## Database

- SQLite

## Project Structure

```
src
 ┣ admins
 ┃ ┣ __init__.py
 ┃ ┣ todo.py
 ┃ ┗ user.py
 ┣ base
 ┃ ┣ exceptions.py
 ┃ ┗ model.py
 ┣ models
 ┃ ┣ __init__.py
 ┃ ┣ todo.py
 ┃ ┗ user.py
 ┣ routers
 ┃ ┣ __init__.py
 ┃ ┣ auth.py
 ┃ ┗ todos.py
 ┣ schemas
 ┃ ┣ __init__.py
 ┃ ┣ todo.py
 ┃ ┗ user.py
 ┣ __init__.py
 ┣ apis.py
 ┣ config.py
 ┣ constants.py
 ┣ database.py
 ┗ main.py
```

## APIs

Updating ...

### Links

- API Doc: `http://localhost:8000/docs`
- Admin: `http://localhost:8000/admin/`
- Endpoints:
    - user: `http://localhost:8000/api/v1/users`
    - todo: `http://localhost:8000/api/v1/todos`

## Setup

- Load helper scripts
    ```
    source .activate.sh
    ```

- Run setup
    ```
    run_setup
    ```

## Run

- Load helper scripts
    ```
    source .activate.sh
    ```

- Activate environment
    ```
    activate_env
    ```

- Run app
    ```
    run_app
    ```

## How to Test

Updating ...
