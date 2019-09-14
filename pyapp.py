from flask import Flask, render_template, request, session
from flask_session.__init__ import Session
import datetime
app = Flask(__name__)

#below block is for the note taker page to store the date in the session for the same user even after closing the web browser as the data is stored in the server, if the server is shutted down then the data will be lost.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html") #the main route

@app.route("/page1.1.html") #route for page 1.1
def page1_1():
    return render_template("page1.1.html")

@app.route("/hello.html") #route for the form page to type your name in a form then using post it will appear in welcome.html
def hello():
    return render_template("hello.html")

@app.route("/welcome.html", methods=["GET", "POST"]) #get is used to avoid errors in the website, if someone accesses the url directly without submmitting the form it will get the below message
def welcome():
    if request.method == "GET":
        return("<h1 style='text-align: center;margin-top:10%;'>Please use the form <a href='hello.html'>here</a></h1>")
    else:
        name = request.form.get("name") #storing the name entred in the form in a variale called name
        return render_template("welcome.html", name=name) #assigning the variale name to the HTML jinja variale called name in welcome.html page

# Notes taking page notes.html
@app.route("/notes.html")
def notes():
    return render_template("notes.html")

@app.route("/notes.html", methods=["GET", "POST"])
def notesfunc():
    if session.get("notes") is None: #to avoid overwirting the current input, because the 2nd line will set the list (Notes) to blank
        session["notes"] = []
    if request.method == "POST": #if the list is not empty, then this function will append the new inpute (Note) to the existing inputs (Notes) during the same session (session is permanant for the same browser as long as the server is not shutted down)
        note= request.form.get("notesinput")
        session["notes"].append(note)
    return render_template("notes.html", notes=session["notes"])
