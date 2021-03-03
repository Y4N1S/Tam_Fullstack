from flask import Flask, render_template,abort,jsonify
import wget
from function_tam import download,stations, lines, stations_and_lignes


app = Flask(__name__)


@app.route('/')
def home():
    return 'hello'

@app.route('/stations')
def entry_point():
    return jsonify(stations())
    # return render_template('stations.html',pagetitle="Home",test='home')
    #   
@app.route('/lines')
def transport_lines():
    return jsonify(lines())

@app.route("/stations/<station>")
def about():
    return render_template('station.html',pagetitle="About",test='city')

@app.route("/stations_and_lignes")
def all_infos():
    return jsonify(stations_and_lignes())


if __name__ == '__main__':
    app.run(debug=True)