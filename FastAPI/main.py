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

@app.get("/")
def main_page():
    return {"message": "Hello!"}

# Bouquets Endpoints

@app.get("/bouquets/")
def read_bouquets():
    return BOUQUETS_DB

@app.post("/bouquets/")
def create_bouquet(bouquet: Bouquets):
    BOUQUETS_DB.append(bouquet)
    return bouquet

@app.put("/bouquets/{id}")
def update_bouquet(id: int, bouquet: Bouquets):
    for index, existing_bouquet in enumerate(BOUQUETS_DB):
        if existing_bouquet.id == id:
            BOUQUETS_DB[index] = bouquet
            return bouquet
    raise HTTPException(status_code=404, detail="Букет не найден")

@app.delete("/bouquets/{id}")
def delete_bouquet(id: int):
    for index, bouquet in enumerate(BOUQUETS_DB):
        if bouquet.id == id:
            del BOUQUETS_DB[index]
            return {"detail": "Букет удалён"}
    raise HTTPException(status_code=404, detail="Букет не найден")

# Components Bouquets Endpoints

@app.get("/components-bouquets/")
def read_components_bouquets():
    return COMPONENTS_BOUQUETS_DB

@app.post("/components-bouquets/")
def create_component_bouquet(component: СomponentsBouquets):
    COMPONENTS_BOUQUETS_DB.append(component)
    return component

@app.put("/components-bouquets/{id}")
def update_component_bouquet(id: int, component: СomponentsBouquets):
    for index, existing_component in enumerate(COMPONENTS_BOUQUETS_DB):
        if existing_component.id == id:
            COMPONENTS_BOUQUETS_DB[index] = component
            return component
    raise HTTPException(status_code=404, detail="Компоненты не найдены")

@app.delete("/components-bouquets/{id}")
def delete_component_bouquet(id: int):
    for index, component in enumerate(COMPONENTS_BOUQUETS_DB):
        if component.id == id:
            del COMPONENTS_BOUQUETS_DB[index]
            return {"detail": "Компонент букета удалён"}
    raise HTTPException(status_code=404, detail="Компоненты не найдены")

# Customers Endpoints

@app.get("/customers/")
def read_customers():
    return CUSTOMERS_DB

@app.post("/customers/")
def create_customer(customer: Customers):
    CUSTOMERS_DB.append(customer)
    return customer

@app.put("/customers/{id}")
def update_customer(id: int, customer: Customers):
    for index, existing_customer in enumerate(CUSTOMERS_DB):
        if existing_customer.id == id:
            CUSTOMERS_DB[index] = customer
            return customer
    raise HTTPException(status_code=404, detail="Клиент не найден")

@app.delete("/customers/{id}")
def delete_customer(id: int):
    for index, customer in enumerate(CUSTOMERS_DB):
        if customer.id == id:
            del CUSTOMERS_DB[index]
            return {"detail": "Клиент удалён"}
    raise HTTPException(status_code=404, detail="Клиент не найден")

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)