# Smart Classroom & Timetable Scheduler

A full-stack starter kit to build a **Smart Classroom** platform with an **intelligent Timetable Scheduler**.

## What you get
- **Backend**: FastAPI (Python) + SQLAlchemy + OR-Tools (constraint solver) + SQLite (dev) / Postgres (optional).
- **Frontend**: React (Vite) + TailwindCSS.
- **Scheduler**: Generates conflict-free timetables using teacher/room availability and timeslots.
- **Docker**: Optional `docker-compose.yml` to run Postgres + backend + frontend.
- **API Docs**: Auto docs at `/docs` when backend is running.

## Quick Start (Dev, no Docker)
1) **Backend**
```bash
cd backend
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Backend runs at: http://localhost:8000  (API docs at /docs)

2) **Frontend**
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at: http://localhost:5173

## Populate minimal data
Use the **API docs** at `http://localhost:8000/docs` to POST some teachers, rooms, subjects, and timeslots.
Then click **Generate** on the frontend or call `POST /scheduler/generate` via API.

## Optional: Docker (with Postgres)
```bash
docker compose up --build
```
- Backend: http://localhost:8000
- Frontend: http://localhost:5173
- Postgres: exposed at 5432 (dev only). Default credentials in `docker-compose.yml`.

> By default, backend uses **SQLite** for simplicity. To switch to Postgres, set `DATABASE_URL` in environment
> (see `backend/app/database.py`) or use Docker compose which sets it for you.

## Project Structure
```
smart-classroom-scheduler/
├─ backend/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ database.py
│  │  ├─ models.py
│  │  ├─ schemas.py
│  │  ├─ routers/
│  │  │  ├─ teachers.py
│  │  │  ├─ rooms.py
│  │  │  ├─ subjects.py
│  │  │  ├─ timeslots.py
│  │  │  └─ scheduler.py
│  │  └─ services/
│  │     └─ scheduler.py
│  └─ requirements.txt
├─ frontend/
│  ├─ index.html
│  ├─ package.json
│  ├─ vite.config.js
│  ├─ postcss.config.js
│  ├─ tailwind.config.js
│  └─ src/
│     ├─ main.jsx
│     ├─ App.jsx
│     ├─ api.js
│     ├─ components/
│     │  └─ TimetableGrid.jsx
│     └─ pages/
│        ├─ DataEntry.jsx
│        └─ Scheduler.jsx
└─ docker-compose.yml
```

## Next Steps
- Add attendance (QR/RFID/FaceID), class IoT (MQTT), notifications, Google Calendar export, role-based auth.
- Expand solver: preferences, lab constraints, consecutive periods, teacher load balancing, etc.
