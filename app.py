
from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import random as rn
import csv
from string import ascii_letters as letters
import pandas as pd

"""
From the Tutorial: 
https://pythonbasics.org/flask-sqlalchemy/ 

1) load csv data into pandas dataframe 
2) clean the data using pandas in the dataframe 
2) use sql alchemy to create database / tables 
3) iterate over the dataframe using i.e. df.iterrows()
4) save each row in the database


"""


SECRET_KEY_LEN = 32
app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "".join(letters[rn.randint(0, len(letters) - 1)] for i in range(SECRET_KEY_LEN))


db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200)) 
   pin = db.Column(db.String(10))

   def __init__(self, name, city, addr,pin):
	   self.name = name
	   self.city = city
	   self.addr = addr
	   self.pin = pin


# def populate_database(csv_file = 'eggs.csv'):

# 	with open(csvfile, newline='') as csvfile:
# 	    spamreader = csv.reader(csvfile)
# 	    for row in spamreader:


	        
def read_csv_pandas(med_file = "test.csv"):

	df = pd.read_csv( index_col=None)


@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
