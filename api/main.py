# print("Hello python")
# create virtual env: 
# flask dependency

# save this as app.py
from flask import Flask
#from other_module import fn_from_other_module

#print(__name__)
#fn_from_other_module()
def hello():
    return "Hello, World!"

app = Flask(__name__)

#app.route("/")(hello)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5050)