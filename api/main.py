# print("Hello python")
# create virtual env: 
# flask dependency

# save this as app.py
# from requests import get
import os
# or: import requests ... for all
# to load:  python -m pip install requests
import requests
from flask import Flask, request
from dotenv import load_dotenv
#from other_module import fn_from_other_module
# by default - does not import environ vars. Need to use python-dotenv to do this: 

# default is .env
load_dotenv(dotenv_path="./.env.local")
# print(os.environ["UNSPLASH_KEY"])

#constants upper: 
UNSPLASH_URL = "https://api.unsplash.com/photos/random"
# UNSPLASH_KEY = "Sumb_Wy6axXQVJkeco2vB8bFQk5ezJ9Ca3ecWmwttNgREACT_APP_"
# UNSPLASH_KEY = os.environ["UNSPLASH_KEY"]
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY","")

print("UNSPLASH_KEY is: " + UNSPLASH_KEY)
if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and inserte UNSPLASH_KEY")

#print(__name__)
#fn_from_other_module()
def hello():
    return "Hello, World!"

app = Flask(__name__)

#app.route("/")(hello)

@app.route("/new-image")
def new_image():
    #get params from client request: 
    word = request.args.get("query")
    headers = {
        "Authorization": "Client-ID " + UNSPLASH_KEY,
        "Accept-Version": "v1"
    }

    params = {
        "query": word
    }

    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    
    #print(response.text)
    # print(response.json) 

    data = response.json()

    # dictionary
    #return {"word": word}
    # return {"data": data} 
    # since json is default: 
    return data 


#@app.route("/")
#def hello():
#    return "Hello, World!"

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5050)