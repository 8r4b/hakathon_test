# Hakathon Medical Diagnosis Platform

A full-stack project combining a FastAPI backend (with authentication, authorization, and OpenAI-powered diagnosis) and a frontend (to be added) for managing users, doctors, patients, and medical records.

## Features
- User registration and JWT authentication
- Role-based access for patients and doctors
- Medical record management
- AI-powered diagnosis using OpenAI API
- PostgreSQL database with SQLAlchemy ORM
- Modular, production-ready backend structure

## Backend Setup

### 1. Clone the repository
```sh
git clone https://github.com/8r4b/hakathon_test.git
cd hakathon_test
```

### 2. Create and activate a virtual environment
```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory (see `.env.example` for required variables):
```
DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<dbname>
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key
```

### 5. Run the backend server
```sh
uvicorn app.main:app --reload
```

## API Endpoints
- `/register` - Register a new user
- `/login` - Obtain JWT token
- `/users/me` - Get current user info
- `/patients/` - Patient profile and records
- `/doctors/` - Doctor profile
- `/records/` - Medical records (create, list)

## Frontend
The frontend folder can be added to this repository. See the `frontend/` directory (to be created) for setup instructions.

## Testing
- Automated tests can be added in the `tests/` folder using `pytest` and `httpx`.

## Contributing
1. Fork the repo and clone it
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request

## License
MIT
