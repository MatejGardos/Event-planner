from time import strptime
from flask import Flask, render_template, request
import json
from datetime import datetime, date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def menu():
    with open("database/database.json", "r", encoding="utf-8") as json_file:
             events = json.load(json_file)

    if request.method == "POST":
        return render_template("index.html",events=events)

    elif request.method == "GET":
        with open("database/database.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
    
        cur_date = datetime.today()

        pops = [] 
        for event in data.keys():
            if cur_date > datetime.strptime(event,"%Y-%m-%d"):
                pops.append(event)

        with open("database/database.json", "w+", encoding="utf-8") as json_file:
            for pop in pops:
                data.pop(pop)
            json.dump(data, json_file)
    

        return render_template("index.html",events=events)

@app.route("/new_event", methods=["GET", "POST"])
def new_event():
    if request.method == "POST":
        sport = request.form["Sport"]
        date = request.form["Date"]
        time = request.form["Time"]
        name = request.form["Name"]
        description = request.form["Desc"]

        with open("database/database.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        with open("database/database.json", "w+", encoding="utf-8") as json_file:
            data[date] = {"sport": sport, "date": date, "time": time, "name": name, "description": description}
            json.dump(data, json_file)
        

        return render_template("sucess.html")

    elif request.method == "GET":
        return render_template("new_event.html")

if __name__ == "__main__":
    app.run(debug=True)