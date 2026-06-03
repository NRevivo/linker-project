# Linker Frontend

Vite + React + Tailwind frontend for the Linker URL shortener.

## Setup

```bash
cd frontend
npm install
```

## Run the dev server

```bash
npm run dev
```

The app runs on [http://localhost:5173](http://localhost:5173).

## Pointing at a different backend

By default, the frontend talks to `http://localhost:8000`. Override by creating a `.env`
(see `.env.example`):

```
VITE_API_BASE_URL=https://your-backend.example.com
```

Restart the dev server after changing env vars.

## Backend CORS setup (required)

The FastAPI backend in `app/` does not currently allow cross-origin requests, so the browser
will block calls from `http://localhost:5173`. Add the following to `app/main.py` (do not
commit this change unless intended):

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Restart the backend after adding the middleware.

## Build

```bash
npm run build
npm run preview
```

## Component layout

```
src/
  App.jsx
  api.js                  # POST /shorten wrapper
  components/
    Navbar.jsx
    Wordmark.jsx
    Hero.jsx
    Sparkles.jsx          # decorative background sparkles
    ShortenerCard.jsx     # tabs + form (also renders ResultView)
    ResultView.jsx        # success state with copy + reset
    FeatureBullets.jsx
```
