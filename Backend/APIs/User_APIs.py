from datetime import datetime
from distutils.log import error
from functools import wraps
from flask import jsonify, request
from flask_restful import Resource, reqparse
from sqlalchemy import JSON
import jwt
from models import db,User, Post
from werkzeug.security import generate_password_hash, check_password_hash


user_args = reqparse.RequestParser()
user_args.add_argument('user_name')
user_args.add_argument('user_id')
user_args.add_argument('password')
user_args.add_argument('new_password')
user_args.add_argument('first_name')
user_args.add_argument('middle_name')
user_args.add_argument('last_name')
user_args.add_argument('dob')
user_args.add_argument('email')
user_args.add_argument('roll_number')
user_args.add_argument('role')



format = '%Y-%m-%d'
#JWT Tokenization
def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'x-access-tokens' in request.headers:
           token = request.headers['x-access-tokens']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           data = jwt.decode(token, algorithms=["HS256"])
       except:
           return jsonify({'message': 'token is invalid'})
 
       return f(*args, **kwargs)
   return decorator

#USER_Api to deal with all information regarding user.
class User_API(Resource):
    #Create user using post request
    #Body: {'user_name':'',
    #       'password':'',
    #       'first_name':'',
    #       'middle_name':'',
    #       'last_name':'',
    #       'dob':'',
    #       'email':'',
    #       'roll_number':'',
    #       'role':''}
    def post(self):
        #response 
        #status: 201, {'message':'User Created Successfully!'}
        #raise_error: U101, {'message':'Email address already registered!!'}
        #raise_error: U102, {'message':'User_name already taken!!'}
        fields = user_args.parse_args()
        email=User.query.filter_by(email=fields['email']).first()
        user=User.query.filter_by(user_name=fields['user_name']).first()
        if email:
            raise error(msg="Email address already registered!!", code="U101")
        if user:
            raise error(msg="User_name already taken!!", code="U102")

        #Backend Validation to be implemented over field values.
        new_user = User(user_name=fields.user_name, password = generate_password_hash(fields.password, method='sha256'), 
                        first_name=fields.first_name,middle_name=fields.middle_name,last_name=fields.last_name,
                        dob=datetime.strptime(fields.dob,format),email=fields.email,roll_number=fields.roll_number,role=fields.role,created_at=datetime.now())
        try:
            db.session.add(new_user)
            db.session.commit()
            return 201, {'message':'User Created Successfully!'}
        except:
            return error(msg='Something Went Wrong!!',code=501)
    
    #Give information about the user,
    #Body: {'user_name':'','password':''}
    def get(self,user_name,password):
        #response:
        #status: 201,
        #JSON: {'token':'',
        #      'user_name':''       #to be used in display of username in routed view
        #      'first_name':''
        #      'middle_name':'',
        #      'last_name':'',
        #      'dob':'',
        #      'email':'',
        #      'roll_number':'',
        #      'role':'',
        #      'created_at':''}
        #raise_error: L101, {'message':'Credentials not matched!!'}
        # fields = user_args.parse_args()
        user=User.query.filter_by(user_name=user_name).first()
        if check_password_hash(pwhash=user.password,password=password):
            token = jwt.encode({'public_id' : user.user_id }, "HS256")
            return jsonify({'token':token,'user_name':user.user_name,'user_id':user.user_id,'first_name':user.first_name,'middle_name':user.middle_name,'last_name':user.last_name,'dob':user.dob,'email':user.email,'roll_number':user.roll_number,'role':user.role,'created_at':user.created_at})
        else:
            raise error(msg="Credentials not matched!!",code="L101")
    
    
    #To update profile or prefrences of user,
    #Body: {'password':'','changed_field':'value_to_be_updated',---}
    #Authentication Required.
    @token_required
    def put(self):
        #response:
        #status: 201, {'message':'Profile/Preferences updated successfully!'}
        #raise_error: U201, {'message':'Password Incorrect!!'} 
        fields = user_args.parse_args()
        user=User.query.filter_by(user_id=int(fields.user_id)).first()
        if check_password_hash(pwhash=user.password,password=fields.password):
            db.session.delete(user)
            db.session.commit()
            #may give error if nullable constraints are made on User model and due to created_at column as it is not parsed in fields!! 
            if fields.new_password!=None:
                fields.password=fields.new_password
            user = User(user_name=fields.user_name, password = generate_password_hash(fields.password, method='sha256'), 
                        first_name=fields.first_name,middle_name=fields.middle_name,last_name=fields.last_name,
                        dob=datetime.strptime(fields.dob,format),email=fields.email,roll_number=fields.roll_number,role=fields.role,created_at=datetime.now())
            db.session.add(user)
            db.session.commit()
            return User_API.get(user)
            # return 201, {'message':'Profile/Preferences updated successfully!'}
        else:
            raise error(msg="Password Incorrect!!",code="U201")


    #Delete User (Optional to Implement)
    #Body: {'user_name':'', 'password':''}
    #Authentication Required.
    @token_required
    def delete(self):
        #response:
        #status: 201, {'message':'User Deleted Successfully!'}
        #raise_error: U201, {'message':'Password Incorrect!!'}
        fields = user_args.parse_args()
        user=User.query.filter_by(user_id=int(fields['user_id'])).first()
        if not user:
            return error(msg='Something Went Wrong!!',code=501)
        if check_password_hash(pwhash=user.password,password=fields['password']):
            db.session.delete(user)
            db.session.commit()
            return 200,{'message':'User Deleted Successfully!'}
        else:
            raise error(msg="Password Incorrect!!",code="U201")



post_args = reqparse.RequestParser()
post_args.add_argument('user_id')
post_args.add_argument('user_name')
post_args.add_argument('post_id')
post_args.add_argument('text')
post_args.add_argument('likes')

#Post_Api to deal with the posts created by user.
class Post_API(Resource):
    #To create post by user.
    #Authentication Required.
    #Body: {'user_id':'','user_name':'','text':''}
    def post(self):
        #response:
        #status: 201, {'message':'Post Created Successfully!'}
        fields = post_args.parse_args()
        user=User.query.filter_by(user_id=int(fields['user_id']),user_name=fields['user_name']).first()
        if user:
            new_post=Post(text=fields['text'],user_id=fields['user_id'])
            db.session.add(new_post)
            db.session.commit()
            return 201, {'message':'Post Created Successfully!'}
        else:
            return error(msg='Something Went Wrong!!',code=501)
    
    
    #To read the post created by user, can be read by users other than Author user.
    #Authentication Required.
    #Body: {'user_id':''}
    def get(self):
        #response:
        #status: 201,
        #JSON: {'post_id':'','text':'','likes':'','user_name':'post_author's name','created_at':''}
        fields = post_args.parse_args()
        post=Post.query.filterby(user_id=int(fields['user_id'])).first()
        if post:
            return 200, JSON(post)
        else:
            return error(msg='Something Went Wrong!!',code=501)


    #To edit/like post
    #Authentication Required.
    #Allow to edit post if and only if the current user's user_id is same as Author's user_id, do proper function internal validation accordingly during implementation.
    #Body: {'user_id':'','post_id':'','text':'only if required to edit the post'}
    def put(self):
        #response:
        #status: 201, {'message':'Post/Liked Edited Successfully!'}
        #raise_error: P201, {'message':'Author User is required to Edit Post!!'}
        fields = post_args.parse_args()
        post=Post.query.filter_by(user_id=int(fields['user_id'])).first()
        if fields['likes']:
            post.likes=+1  #may give error if nullable constraints are made on User model and due to created_at column as it is not parsed in fields!! 
            db.session.commit()
            return 201, {'message':'Post Liked Successfully!'}
        elif fields:
            post=fields                 #password checking can be implemented to check authorship of post
            db.session.commit()
            return 201, {'message':'Profile/Preferences updated successfully!'}
        else:
            raise error(msg="Password Incorrect!!",code="U201")


    #To Delete Post.
    #Authentication Required.
    #Can only be done by Author user.
    #Body: {'user_id':'','password':'','post_id':''}
    def delete(self):
        #response:
        #status: 201,{'message':'Post Deleted Successfully!!'}
        #raise_error: P201, {'message':'Author User is required to Delete Post!!'}
        fields = user_args.parse_args()
        post=Post.query.filter_by(user_id=int(fields['user_id'])).first()
        if post:
            db.session.delete(post)
            db.session.commit()
            return 202,{'message':'Post Deleted Successfully!'}
        else:
            return error(msg='Something Went Wrong!!',code=501)            