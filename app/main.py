from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.db.database import database
from app.resources.routes import api_router
from app.reusable.exceptions import OPException
import logging
import time

FORMAT = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
logging.basicConfig(format=FORMAT)
log = logging.getLogger("uvicorn")

app = FastAPI()
app.include_router(api_router)

# origins = [
#     "http://localhost",
#     "http://localhost:4200",
# ]

app = FastAPI()
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.exception_handler(OPException)
async def operations_db_exception_handler(request: Request, exc: OPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.to_dict()
    )
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    log.info(
        {
            "url": request.url,
            "method": request.method,
        }
    )
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response