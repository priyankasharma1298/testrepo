from fastapi import FastAPI

app = FastAPI()

from pydantic import BaseModel
from typing import Optional

class Food(BaseModel):
    id : int
    name : str
    serving_size : str
    kcal_per_serving : int
    protein_grams : float
    fibre_grams : Optional[float]=0


@app.get('/')
def get_view():
    return {"message": "Welcome to PyBites' FastAPI Learning Path"}



foods = {1: {'id': 1, 'name':'egg', 'serving_size':'piece', 'kcal_per_serving':78,
'protein_grams':6.3, 'fibre_grams':0} }    

@app.post('/create-food/{item_id}')
def create_food(item_id : int,food:Food):
    if item_id not in foods:
        foods[item_id] = { "id":food.id,
        "name":food.name,
        "serving_size":food.serving_size,
        "kcal_per_serving":food.kcal_per_serving,
        "protein_grams":food.protein_grams,
        "fibre_grams":food.fibre_grams}
        return foods[item_id]