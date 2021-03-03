from flask import Flask, render_template,abort,jsonify
import wget
from function_tam import download,stations


app = Flask(__name__)


@app.route('/')

@app.route('/stations')
def entry_point():
    return jsonify(stations())
    # return render_template('stations.html',pagetitle="Home",test='home')    

@app.route("/stations/<station>")
def about():
    return render_template('station.html',pagetitle="About",test='city')


if __name__ == '__main__':
    app.run(debug=True)