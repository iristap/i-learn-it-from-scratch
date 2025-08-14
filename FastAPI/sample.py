from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/square/{number}")
def square_number(number: int, unit: str = None):
    result = number ** 2
    response = {"result": result}
    if unit:
        response["unit"] = unit
    return response

