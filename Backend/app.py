#Importing libraries, modules from other python files and requiored packages.
from datetime import datetime
from flask import Flask                               
from os import path
from models import db                        
from flask_restful import Api         
from flask_cors import CORS
from APIs.User_APIs import User_API, Post_API


#Global_Variable decalarations and assignments
db_name="store.sqlite3"

print("\n",datetime.now(),"-> Manual Logging Started!")
#Create App
def create_app():
    app = Flask(__name__)

    # CORS Configuration
    # CORS(app)

    app.config['SECRET_KEY'] = 'Vikramaditya'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    db.init_app(app)

    api = Api(app)
    api.add_resource(User_API,  '/user','/user/<string:user_name>/<string:password>')
    api.add_resource(Post_API, '/post')

    create_db(app)
    return app

#Create Database
def create_db(app):
    if not path.exists("./"+ db_name):
       with app.app_context():
        db.create_all()
        print("",datetime.now(),"-> Database created Successfully!\n")
    else:
        print(datetime.now(),'-> Database creation failed!!\n')

#Running the final App
app=create_app()
CORS(app)
app.run()