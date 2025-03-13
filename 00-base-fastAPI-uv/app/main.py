from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI in Dev Container!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}