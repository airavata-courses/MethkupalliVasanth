#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME']='bookstore'
app.config['MONGO_URI']='mongodb://localhost:27017/bookstore'

mongo = PyMongo(app)

@app.route('/aj')
def get_all_books():
	book=mongo.db.books
	output = []
	for a in book.find():
		output.append({'author' : a['author'], 'create_date' : a['create_date'], 'description':a['description'], 'genre': a['genres']})
	return jsonify({'result':output})



if __name__ == '__main__':
    app.run(debug=True)
