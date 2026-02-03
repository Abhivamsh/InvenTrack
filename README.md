# InvenTrack - Product Inventory Management System

A full-stack product inventory management system built with FastAPI (backend) and React (frontend).

## Features
- ✅ Create, Read, Update, Delete products
- ✅ Real-time inventory tracking
- ✅ PostgreSQL database
- ✅ Responsive UI
- ✅ RESTful API

## Tech Stack
**Backend:**
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

**Frontend:**
- React
- Axios
- CSS3

## Local Setup

### Prerequisites
- Python 3.12+
- Node.js 16+
- PostgreSQL

### Backend Setup
```bash
cd FASTAPI
python -m venv fastapi
.\fastapi\Scripts\activate  # Windows
pip install -r requirements.txt

# Create PostgreSQL database named 'products'
# Update database credentials in database.py

python -m uvicorn main:app --reload --host localhost --port 8000
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Access
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## API Endpoints
- GET /products - Get all products
- GET /products/{id} - Get product by ID
- POST /products/ - Create new product
- PUT /products/{id} - Update product
- DELETE /products/{id} - Delete product

## License
MIT
