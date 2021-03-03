from flask import Flask, render_template,abort,jsonify
import wget
from function_tam import download,stations


app = Flask(__name__)


@app.route('/')
# def entry_point():
#     df = pandas.read_csv('ong.csv', names=['id', 'country', 'year', 'emissions', 'value', 'footnotes', 'source'])
#     if df is None:
#         return abort(404)
#     else:
#         return df
#     return render_template('home2.html',pagetitle="Home",test='home')


@app.route('/stations')
def entry_point():
    return stations().to_string()  
    # return render_template('stations.html',pagetitle="Home",test='home')    

@app.route("/stations/<station>")
def about():
    return render_template('station.html',pagetitle="About",test='city')


if __name__ == '__main__':
    app.run(debug=True)