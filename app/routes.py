from flask import flask
app = Flask(__name__) 

@app.get("/")
def home():
    me = {
        "first_name":"Mauricio",
        "last_name":"Navarro",
        "hobbies": "Watch TV",
        "is_inline": True
    }
    return me