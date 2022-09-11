from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# PATH=/bin:/usr/bin:/usr/local/bin:${PATH}
import time

@app.get("/")
async def root():
    time.sleep(5.5)  # Pause 5.5 seconds
    return {"status": True, "showResults": True, "cityName": "Split 3", "weatherNow": "rain"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
