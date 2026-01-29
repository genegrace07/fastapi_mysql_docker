from fastapi import FastAPI,HTTPException,status
from appdb import Users

app = FastAPI()
usersdb_instance = Users()

@app.get('/')
def viewusers():
    return usersdb_instance.view()
@app.post('/adduser')
def add_user(users:Users):
      userslist=usersdb_instance.view()
      if_match = next((u for u in userslist if users.email == u['email']),None)

      if if_match:
          raise HTTPException(status_code=400,detail='email already exist')
      usersdb_instance.add(users.name,users.email)
      return {'message':'successfully added'}
