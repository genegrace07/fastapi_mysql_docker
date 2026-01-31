from fastapi import FastAPI,HTTPException,status
from appdb import Users,Usersdb

app = FastAPI()
usersdb_instance = Usersdb()

@app.get('/')
def viewusers():
    userslist = usersdb_instance.view()
    if not userslist:
        return {'message': 'empty'}
    return userslist
@app.post('/adduser')
def add_user(users:Users):
      userslist=usersdb_instance.view()
      if_match = next((u for u in userslist if users.email == u['email']),None)

      if if_match:
          raise HTTPException(status_code=400,detail='email already exist')
      usersdb_instance.add(users.name,users.email)
      return {'message':'successfully added'}
@app.patch('/updateuser')
def update_user(users:Users):
    userslist = usersdb_instance.view()
    if_match = next((u for u in userslist if users.id == u['id']), None)

    if if_match:
        usersdb_instance.update(users.name, users.email, users.id)
        return {'message': 'successfully updated'}
    raise HTTPException(status_code=404,detail="Not found")
@app.delete('/deleteuser')
def delete_user(id):
    userslist = usersdb_instance.view()
    if_match = next((u for u in userslist if id == u['id']), None)

    if if_match:
        usersdb_instance.delete(id)
        return {'message': 'successfully deleted'}
    raise HTTPException(status_code=404,detail="Not found")




