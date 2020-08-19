from dotenv import load_dotenv
from os import getenv
from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo

# Load environment variables
load_dotenv()

# Create an instance of Flask
app = Flask(__name__)

# Get the connection string for the database
app.config['MONGO_URI'] = getenv('MONGO_URI', '')

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app)





@app.after_request
def after_request(response):
    header = response.headers
    header["Access-control-allow-origin"] = '*'
    return response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calijuly")
def caliJuly():
    return render_template("calijuly.html")


# Route that will trigger the scrape function
@app.route("/api")
def api():
    # data1 = mongo["covid_db"].covid.find({}, {'_id': False})
    data1= mongo.db.GUSdata.find({}, {'_id': False})

    cases = [case for case in data1]
    data = {

    "cases": cases
    }

    return jsonify(data)

@app.route("/api/march")
def marchapi():
    # data1 = mongo["covid_db"].covid.find({}, {'_id': False})
    marchcoll= mongo.db.GUSdata.find({ "Date":  {"$regex":"3/\d*/2020"}}, {'_id': False})

    marchcases = [case for case in marchcoll]
    marchdata = {

    "cases": marchcases
    }

    return jsonify(marchdata)

@app.route("/api/april")
def aprilapi():
    # data1 = mongo["covid_db"].covid.find({}, {'_id': False})
    aprilcoll= mongo.db.GUSdata.find({ "Date":  {"$regex":"4/\d*/2020"}}, {'_id': False})

    aprilcases = [case for case in aprilcoll]
    aprildata = {

    "cases": aprilcases
    }

    return jsonify(aprildata)

    
@app.route("/api/may")
def mayapi():
    # data1 = mongo["covid_db"].covid.find({}, {'_id': False})
    maycoll= mongo.db.GUSdata.find({ "Date":  {"$regex":"5/\d*/2020"}}, {'_id': False})

    maycases = [case for case in maycoll]
    maydata = {

    "cases": maycases
    }

    return jsonify(maydata)

@app.route("/api/june")
def juneapi():
    # data1 = mongo["covid_db"].covid.find({}, {'_id': False})
    junecoll= mongo.db.GUSdata.find({ "Date":  {"$regex":"6/\d*/2020"}}, {'_id': False})

    junecases = [case for case in junecoll]
    junedata = {

    "cases": junecases
    }

    return jsonify(junedata)

@app.route("/api/july")
def julyapi():
    # data1 = mongo["covid_db"].covid.find({}, {'_id': False})
    julycoll= mongo.db.GUSdata.find({ "Date":  {"$regex":"7/\d*/2020"}}, {'_id': False})

    julycases = [case for case in julycoll]
    julydata = {

    "cases": julycases
    }

    return jsonify(julydata)

@app.route("/api/all-heat")
def heatAPI():
    Heatcoll= mongo.db.allHeat.find({}, {'_id': False})

    Heatcases = [case for case in Heatcoll]
    Heatdata = {

    "cases": Heatcases
    }

    return jsonify(Heatdata)

@app.route("/api/march-heat")
def heatMarchAPI():
    HeatMarcoll= mongo.db.marchHeat.find({}, {'_id': False})

    HeatMarcases = [case for case in HeatMarcoll]
    HeatMardata = {

    "cases": HeatMarcases
    }

    return jsonify(HeatMardata)

@app.route("/api/april-heat")
def heatAprilAPI():
    Heatcoll= mongo.db.aprilHeat.find({}, {'_id': False})

    Heatcases = [case for case in Heatcoll]
    Heatdata = {

    "cases": Heatcases
    }

    return jsonify(Heatdata)

@app.route("/api/may-heat")
def heatMayAPI():
    Heatcoll= mongo.db.mayHeat.find({}, {'_id': False})

    Heatcases = [case for case in Heatcoll]
    Heatdata = {

    "cases": Heatcases
    }

    return jsonify(Heatdata)

@app.route("/api/june-heat")
def heatJuneAPI():
    Heatcoll= mongo.db.juneHeat.find({}, {'_id': False})

    Heatcases = [case for case in Heatcoll]
    Heatdata = {

    "cases": Heatcases
    }

    return jsonify(Heatdata)

@app.route("/api/july-heat")
def heatJulyAPI():
    Heatcoll= mongo.db.julyHeat.find({}, {'_id': False})

    Heatcases = [case for case in Heatcoll]
    Heatdata = {

    "cases": Heatcases
    }

    return jsonify(Heatdata)





if __name__ == "__main__":
    app.run(debug=True)
