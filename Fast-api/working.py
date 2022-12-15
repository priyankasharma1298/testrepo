# API= application programing interface => does data validation , generates auto documentation

#import fastapi         #to check if fastapi is installed
from typing import Optional
from pydantic import BaseModel

'''writing our fastapi'''
from fastapi import FastAPI,Path

app = FastAPI()  #creates an api object  where FastApi is class/module

class Item(BaseModel):   #structure of data 
    name:str
    price:int
    brand: Optional[str]=None
    
# EXAMPLE
# to create an endpoint for home(are like routes in url => /user  ,  /adduser , /home)
# http methods= get  post  put  delete
@app.get("/")
def home():
    return {'data':'testing'}  #automatic generates documentation of your api



'''
this dict is auto converted into json, as soon as the dict is returned from the function the
fastapi handles this conversion 
when ever we return any data/info which we write using python scripts
from endpoint[def home()] its gets converted in to json format

'''
#EXAMPLE
# creating few more end points
@app.get('/about')
def about():
    return{'data':'about'}





# inventory = { 1  :   {'name':'milk', 'price':5,'brand':'omfed'}   }
inventory = {}

#path parameters
@app.get('/get-item/{item_id}')
def get_item(item_id: int):
    return inventory[item_id]



# multiple path parameters
@app.get('/get-item/{item_id}/{name}')
def get_item(item_id: int, name:str):
    return inventory[item_id]


# adding details to path parameter such as contraints and description
# always add a default valuei.e None when using functions such as path() inside parameters for 
# endpoints
@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None,description='the id of the item u want to see', gt=0,lt=2)):
    return inventory[item_id]




# query parameters  => that comes after an ? in an url
# if we dont provide query parameter in url [http://127.0.0.1:8000/get-by-name?name=milk]
# then it will give error

@app.get('/get-by-name')
def get_item(name:str):  #it takes 1 query parameter i.e name [REQUIRED QUERY PARAMETER]
    for item_id in inventory:
        if inventory[item_id]['name'] == name:   
            return inventory[item_id]    # returns the value at inventory[1]
    else:
        return {"data":"not found"} 


@app.get('/get-by-price')
def get_item(price:int):
    for item_id in inventory:
        if inventory[item_id]['price']  == price:
            return inventory[item_id]
    else:
        return "oops!!! data not found..... "        



# make query parameters optional
# for this we need to import optional from typing
@app.get('/get-by-name')
def get_item(test:int, name: Optional[str] = None):  # query parameter name becomes optional here so this wont give us any error if we dont pass name value in url[OPTIONAL QUERY PARAMETER]
    for item_id in inventory:
        if inventory[item_id]['name']==name:
            return inventory[item_id]
    else:
        return {'data':'not found'}  






# combining query=> name,test and path parameters =>item_id
@app.get('/get-by-name/{item_id}')
def get_item( test:int , item_id:int , name: Optional[str] = None):  # query parameter name becomes optional here so this wont give us any error if we dont pass name value in url
    for item_id in inventory:
        #if inventory[item_id]['name'] == name:
        if inventory[item_id].name == name:
            return inventory[item_id]
    else:
        return {'data':'not found'}








#request body
# create new item in the database
        
@app.post('/create-item/{item_id}')
def create_item(item_id: int , item: Item):
    if item_id in inventory:
        return {'error':'this item id already exixts'}
    else:
        #inventory[item_id] = {'name': item.name, 'price': item.price, 'brand': item.brand}
        inventory[item_id] = item     
        return inventory[item_id]




#put method 
#to update in database 
@app.put('/update-item/{item_id}')
def update_item(item_id: int , item: Item):
    if item_id not in inventory:
        return {'error':'this item id does not exixts'}
    if item.name != None:
        inventory[item_id].name=item.name

    if item.price != None:
        inventory[item_id].price=item.price 

    if item.brand != None:
        inventory[item_id].brand=item.brand 
    return inventory[item_id]          
        



# delete
# to delete item from database
@app.delete('/delete-item')
def delete_item(item_id: int ):
    if item_id not in inventory:
        return {'error':'id does not exits'}
    else:
        del inventory[item_id] 
        return{'succes':'item deleted!!!!'}   


