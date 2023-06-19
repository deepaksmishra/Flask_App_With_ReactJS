import datetime
from flask import Flask ,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)   # creating object of the flask

##conbfig database URL with id and pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

# declration of  database models ( columns with datatypes)
class Articles(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text(100))
    date = db.Column(db.DateTime , default = datetime.datetime.now)


def __init__(self,title,description):
    self.title = title
    self.description = description 

             
#added app rounting ( API Craetion with Get Method)
@app.route('/get',methods = ['GET'])
def get_articles():
    return jsonify({"test" :"app"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)

