from flask import Flask,render_template
import random
from datetime import datetime
Author = "Saurabh Deulkar"
app = Flask(__name__)
import requests
@app.route("/")
def home():
    random_number = random.randint(1,10)
    current = datetime.now()
    year= current.year
    return render_template("index.html",num=random_number,year = year,Author_name=Author)


@app.route("/guess/<name>")
def guess(name):
    header={
        "name":f"{name}"
    }
    response = requests.get("https://api.genderize.io",params=header)
    gender = response.json()["gender"]
    response1 = requests.get("https://api.agify.io/",params=header)
    age = response1.json()["age"]
    return render_template("guess.html",gender = gender,age = age,name = name)


@app.route("/blog/<num>")
def blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("Blog.html",posts=all_posts)

if __name__ ==  "__main__":
    app.run(debug=True)