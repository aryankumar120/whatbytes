# Healthcare Backend (Django Assignment)

## Overview
Backend system for a healthcare application using Django, Django REST Framework, PostgreSQL, and JWT authentication.

## Tech Stack
- Django
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt

## Testing
- Postman (API testing)

## Setup
1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
```bash
python3 -m pip install -r /Users/aryankumar/Downloads/whatbytes/requirements.txt
```
3. Ensure PostgreSQL is running and create database:
```bash
createdb healthcare
```
4. Configure environment variables in `.env` (already provided).
5. Run migrations:
```bash
cd /Users/aryankumar/Downloads/whatbytes
python3 manage.py makemigrations api
python3 manage.py migrate
```
6. Start server:
```bash
python3 manage.py runserver
```

## API Usage
Base URL: `http://127.0.0.1:8000/api`

### Auth
- `POST /auth/register/`
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "StrongPass123!"
}
```

- `POST /auth/login/`
```json
{
  "username": "testuser",
  "password": "StrongPass123!"
}
```

Use the `access` token in the Authorization header:
```
Authorization: Bearer <access_token>
```

### Patients
- `POST /patients/`
```json
{
  "name": "John Doe",
  "age": 35,
  "gender": "male",
  "address": "NYC",
  "phone": "1234567890"
}
```
- `GET /patients/`
- `GET /patients/<id>/`
- `PUT /patients/<id>/`
- `DELETE /patients/<id>/`

### Doctors
- `POST /doctors/`
```json
{
  "name": "Dr Smith",
  "specialization": "Cardiology",
  "email": "drsmith@example.com",
  "phone": "5555555555"
}
```
- `GET /doctors/`
- `GET /doctors/<id>/`
- `PUT /doctors/<id>/`
- `DELETE /doctors/<id>/`

### Patient-Doctor Mapping
- `POST /mappings/`
```json
{
  "patient": 1,
  "doctor": 1
}
```
- `GET /mappings/`
- `GET /mappings/<patient_id>/` (doctors for a patient)
- `DELETE /mappings/<id>/` (remove mapping)

## Screenshots
Add your Postman or API test screenshots here:

###Register
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/f8694012-f5eb-42e5-9595-cb5345236977" />

###Login
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/5aad5bcd-5271-45c2-aa28-6c99eff6b969" />

###Patients
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/f01c49f1-b0a6-4bbe-b747-a57d9b1c8338" />

###Doctors
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/6a14a5bf-3ac4-40dc-9628-f9c505c836bb" />

###Mappings
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/226da56e-b8f4-4216-9642-0a5b6ca5f577" />

##GET results
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/d7d95cac-6226-4a53-ab55-c60ff990bbb0" />
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/882c854d-2cc1-4c50-989e-2a417a422c63" />
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/59e2902d-2d21-42c6-b592-899d6d158e15" />



## Notes / Suggestions
- Refresh tokens from login then go for requests.
- Keep `.env` out of version control when submitting to public repos.
