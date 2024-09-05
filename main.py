from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
   return {"data": [{"Hello":" World"}]}

@app.get("/class")
def get_class():
    return {"class_name": "Math 101", "teacher": "Mr. Smith", "students": 30}

