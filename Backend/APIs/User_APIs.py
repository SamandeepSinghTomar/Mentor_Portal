from flask_restful import Resource
from requests import delete
import models


#USER_Api to deal with all information regarding user.
class User_API(Resource):
    #Create user using post request
    #Body:{'user_name':'',
    #      'password':'',
    #      'first_name':'',
    #      'middle_name':'',
    #      'last_name':'',
    #      'dob':'',
    #      'email':'',
    #      'roll_number':'',
    #      'role':''}
    def post(self):
        #response 
        #status: 201, {'message':'User Created Successfully!'}
        #raise_error: U101, {'message':'Email address already registered!!'}
        #raise_error: U102, {'message':'User_name already taken!!'}
        pass

    
    #Give information about the user,
    #body:{'user_name':'','password':''}
    def get(self):
        #response:
        #status: 201,
        #JSON {'token':'',
        #      'user_name':''       #to be used in display of username in routed view
        #      'first_name':''
        #      'middle_name':'',
        #      'last_name':'',
        #      'dob':'',
        #      'email':'',
        #      'roll_number':'',
        #      'role':''}
        #raise_error: L101, {'message':'Credentials not matched!'}
        pass
    
    
    #To update profile or prefrences of user,
    #body {'password':'','changed_field':'value_to_be_updated',---}
    def put(self):
        #response:
        #status: 201, {'message':'Profile/Preferences updated successfully!'}
        #raise_error: U201, {'message':'Password Incorrect!!'} 
        pass
    
    
    #Delete User (Optional to Implement)
    def delete(self):
        #response:
        #status: 201, {'message':'User Deleted Successfully!'}
        #raise_error: U201, {'message':'Password Incorrect!!'}
        pass


#Post_Api to deal with the posts created by user.
def Post_API(Resource):
    def post(self):
        pass
    def get(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass