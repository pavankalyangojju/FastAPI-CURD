from fastapi import FastAPI

app = FastAPI()

# minimal app - get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return{"Ping": "Pong"}


#get ---> Read ToDo
@app.get('/todo',tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}


# Post --> create Todo
@app.post("/todo", tags=["todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return{
        "data": "A Todo has been added !"
    }
    

#put --> update todo
@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] = body['Activity']
            return{
                "data": f"Todo with id {id} has been update"
            }
            
    return{
        "data": f"Todo with this id number {id} was not found !"
    }
    
    
    
# delte --> delete todo
@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todos.remove(todo)
            return{
                "data": f"Todo with id {id} has been deleted"
            }
            
    return{
        "data": f"Todo with this id number {id} was not found !"
    }































todos = [
    {"id": "1",
     "Activity": "jogging for 2 hors at 7:00"
    },
    {"id": "2",
     "Activity": "writing 3 aojkhsd"
    }
]