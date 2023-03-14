from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from flask_migrate import Migrate

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    InputRequired,
    Length
)
from werkzeug.security import (
    generate_password_hash, 
    check_password_hash
)
from flask_login import UserMixin

# from functions.static import *

db = SQLAlchemy()

def get_migrate(app):
  return Migrate(app, db)

def create_db(app):
  db.init_app(app)
  with app.app_context():
    db.create_all()
  
def init_db(app):
  db.init_app(app)
  
def reCreate_db():
  db.create_all()
    
    
'''#'''
class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  board = db.Column(db.Integer, db.ForeignKey('board.id'))
  # owner = db.Column(db.String(64), db.ForeignKey('user.id'))
  title = db.Column(db.String(64), nullable=False)
  message = db.Column(db.String(2048), nullable=False)
  # viewerCount = db.Column(db.Integer, nullable=True)
  image = db.Column(db.Boolean)
  imageLocation = db.Column(db.String(256), nullable=True)
  # dateCreated = db.Column()
  
  def toDict(self):
    return{
      "id": self.id,
      "board": self.board,
      # "owner": self.owner,
      "title": self.title,
      "message": self.message,
      # "viewerCount": self.viewerCount
      "image": self.image,
      "imageLocation": self.imageLocation
      # "dateCreated": self.dateCreate
      
    }
    
'''#'''
class Board(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.String(64), nullable=False)
  faculty = db.Column(db.String(64), nullable=True)
  dept = db.Column(db.String(64), nullable=True)
  # image = db.Column(db.Boolean)
  # imageLocation = db.Column(db.String(256), nullable=True)
  # subscribers = db.Column(db.Integer, nullable=False)
  
  def toDict(self):
    return{
      "id": self.id,
      "title": self.title,
      "faculty": self.faculty,
      "dept": self.dept
      # "image": self.image,
      # "imageLocation": self.imageLocation
      # "subscribers": self.subscribers
    }
    
'''#'''
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), unique=True, nullable=False)
  email = db.Column(db.String(64), nullable=False)
  password = db.Column(db.String(64), nullable=False)
  faculty = db.Column(db.String(64), nullable=False)
  dept = db.Column(db.String(64), nullable=False)
  
  
  def toDict(self):
    return{
      "id": self.id,
      "username": self.username,
      "password": self.password,
      "faculty": self.faculty,
      "dept": self.dept
    }
  
  #hashes the password parameter and stores it in the object
  def set_password(self, password):
    """Create hashed password."""
    self.password = generate_password_hash(password, method='sha256')
  
  #Returns true if the parameter is equal to the object's password property
  def check_password(self, password):
    """Check hashed password."""
    return check_password_hash(self.password, password)
  
  #To String method
  def __repr__(self):
    return '<User {}>'.format(self.username)
    
'''#'''
class FacultyDept(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  faculty = db.Column(db.String(64), nullable=False)
  fLabel = db.Column(db.String(64), nullable=False)
  department = db.Column(db.String(64), nullable=True)
  fLabel = db.Column(db.String(64), nullable=True)
  
  def toDict(self):
    return{
      "id": self.id,
      "faculty": self.faculty,
      "department": self.department
    }
    
'''#'''
class SearchForm(FlaskForm):
    search = StringField("searchCriteria", validators =[DataRequired()])
    submit = SubmitField("Submit")