
# InvenTrack 📦

A modern inventory management system built with FastAPI and React.

## Features

- ✅ Add, Edit, Delete Products
- ✅ Real-time Stock Tracking
- ✅ Search & Filter
- ✅ Responsive Design
- ✅ PostgreSQL Database

## Tech Stack

**Backend:**
- FastAPI - Modern Python web framework
- SQLAlchemy - Database ORM
- PostgreSQL - Database
- Uvicorn - ASGI server

**Frontend:**
- React - UI library
- Axios - HTTP client
- CSS3 - Styling

## Quick Start

### Backend
```bash
cd C:\Users\DELL\Desktop\FASTAPI
fastapi\Scripts\activate
pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm start
```

### Database Setup
```sql
CREATE DATABASE products;
```

## API Endpoints

- `GET /products` - Get all products
- `POST /products` - Create product
- `PUT /products/{id}` - Update product
- `DELETE /products/{id}` - Delete product

## Project Structure

```
InvenTrack/
├── main.py              # FastAPI app
├── models.py            # Pydantic models
├── database.py          # DB config
├── database_models.py   # SQLAlchemy models
├── frontend/            # React app
│   ├── src/
│   │   ├── App.js
│   │   └── App.css
│   └── public/
└── README.md
```

## Built With

- **FastAPI** - Modern, fast web framework for building APIs
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI server implementation





---

