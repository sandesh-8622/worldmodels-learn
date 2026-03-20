from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def say_hello():
    return {"message": "hello from your server"}

@app.get("/topics")
def get_topics():
    return {
        "topics": [
            "I-JEPA"
            "V-JEPA"
            "World Models"
            "Physical AI"
        ]
    }