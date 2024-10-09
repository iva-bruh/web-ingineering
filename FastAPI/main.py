from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

class Bouquets(BaseModel):
    id: int
    name: str
    price: float

class СomponentsBouquets(BaseModel):
    id: int
    title: str
    text: str

class Customers(BaseModel):
    id: int
    name: str
    phone: str

BOUQUETS_DB = [
    Bouquets(id=1, name="Чистая любовь", price=7230.00),
    Bouquets(id=2, name="Бурлеск", price=7780.00),
    Bouquets(id=3, name="Ностальгия", price=7760.00)
]

COMPONENTS_BOUQUETS_DB = [
    СomponentsBouquets(id=1, title="Чистая любовь", text="Амариллис 4 шт., Калла 9 шт."),
    СomponentsBouquets(id=2, title="Бурлеск", text="Орхидея 6 шт., Роза 11 шт."),
    СomponentsBouquets(id=3, title="Ностальгия", text="Калла 8 шт., Роза 11 шт.")
]

CUSTOMERS_DB = [
    Customers(id=1, name="Алла Ушакова", phone="+79090457761"),
    Customers(id=2, name="Иван Иванов", phone="+79876543215"),
    Customers(id=3, name="Сергей Пенопласт", phone="+79517451945")
]

app = FastAPI()

@app.get("/bouquets/")
def read_bouquets(): return BOUQUETS_DB

@app.get("/bouquets/{id}")
def read_bouquets(id: int):
    for bouquet in BOUQUETS_DB:
        if bouquet.id == id:
            return bouquet
    raise HTTPException(status_code=404, detail="Букет не найден")

@app.get("/components-bouquets/")
def read_componets_bouquets(): return COMPONENTS_BOUQUETS_DB

@app.get("/components-bouquets/{id}")
def read_componets_bouquets(id: int):
    for components_bouquet in COMPONENTS_BOUQUETS_DB:
        if components_bouquet.id == id:
            return components_bouquet
    raise HTTPException(status_code=404, detail="Компоненты не найдены")

@app.get("/customers/")
def read_customers(): return CUSTOMERS_DB

@app.get("/customers/{id}")
def read_customers(id: int):
    for customer in CUSTOMERS_DB:
        if customer.id == id:
            return customer
    raise HTTPException(status_code=404, detail="Клинет не найден")

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)


