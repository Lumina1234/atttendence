import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from backend.database import engine, Base
from backend.routers import auth_router, teacher_router, student_router, attendance_router

# ─── Startup: create tables and upload directory ───────────────────────────────
Base.metadata.create_all(bind=engine)
upload_dir = os.getenv("UPLOAD_DIR", "uploads")
Path(upload_dir).mkdir(parents=True, exist_ok=True)

# ─── App setup ─────────────────────────────────────────────────────────────────
app = FastAPI(title="Smart Attendance System", version="1.0.0")

# CORS (useful for local dev / API testing tools)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Static files & templates ──────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "frontend" / "static"), name="static")
app.mount("/uploads", StaticFiles(directory=Path(upload_dir)), name="uploads")

templates = Jinja2Templates(directory=BASE_DIR / "frontend" / "templates")

# Expose API_BASE_URL to every template so JS can use it
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def template_context(request: Request) -> dict:
    return {"API_BASE_URL": API_BASE_URL}

# ─── Include routers ──────────────────────────────────────────────────────────
app.include_router(auth_router.router)
app.include_router(teacher_router.router)
app.include_router(student_router.router)
app.include_router(attendance_router.router)

# ─── Page routes ──────────────────────────────────────────────────────────────

@app.get("/")
async def root():
    return RedirectResponse(url="/login")


@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", template_context(request))


@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse(request, "register.html", template_context(request))


@app.get("/teacher/dashboard")
async def teacher_dashboard(request: Request):
    return templates.TemplateResponse(request, "teacher_dashboard.html", template_context(request))


@app.get("/student/dashboard")
async def student_dashboard(request: Request):
    return templates.TemplateResponse(request, "student_dashboard.html", template_context(request))


# ─── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    import socket
    import sys
    
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    
    # SSL Configuration
    ssl_cert_file = os.getenv("SSL_CERT_FILE")
    ssl_key_file = os.getenv("SSL_KEY_FILE")
    use_https = ssl_cert_file and ssl_key_file and Path(ssl_cert_file).exists() and Path(ssl_key_file).exists()
    
    if use_https:
        # Try to use specified HTTPS port
        https_port = int(os.getenv("HTTPS_PORT", "443"))
        
        # Test if port is available
        def is_port_available(port):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                result = sock.connect_ex(('127.0.0.1', port))
                return result != 0
        
        if https_port == 443 and not is_port_available(443):
            # Port 443 requires elevated privileges; fallback to 8443
            print("⚠️  Port 443 requires elevated privileges (admin/sudo).")
            print("   Falling back to port 8443 for HTTPS development.")
            https_port = 8443
        
        print(f"🔒 Starting HTTPS server on https://{host}:{https_port}")
        print(f"   Certificate: {ssl_cert_file}")
        print(f"   Key: {ssl_key_file}\n")
        
        uvicorn.run(
            "main:app",
            host=host,
            port=https_port,
            reload=True,
            ssl_certfile=ssl_cert_file,
            ssl_keyfile=ssl_key_file,
        )
    else:
        print(f"⚠️  SSL certificates not configured. Running on HTTP.")
        print(f"   To enable HTTPS, run: python generate_cert.py")
        print(f"   Then set SSL_CERT_FILE and SSL_KEY_FILE in .env\n")
        print(f"🔓 Starting HTTP server on http://{host}:{port}\n")
        
        uvicorn.run("main:app", host=host, port=port, reload=True)
