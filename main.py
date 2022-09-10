from fastapi import FastAPI

app = FastAPI()

# PATH=/bin:/usr/bin:/usr/local/bin:${PATH}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
