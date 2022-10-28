from flask_restful import Resource
import models


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
        pass

    
    #Give information about the user,
    #Body: {'user_name':'','password':''}
    def get(self):
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
        #      'role':''}
        #raise_error: L101, {'message':'Credentials not matched!'}
        pass
    
    
    #To update profile or prefrences of user,
    #Body: {'password':'','changed_field':'value_to_be_updated',---}
    #Authentication Required.
    def put(self):
        #response:
        #status: 201, {'message':'Profile/Preferences updated successfully!'}
        #raise_error: U201, {'message':'Password Incorrect!!'} 
        pass
    
    
    #Delete User (Optional to Implement)
    #Body: {'user_name':'', 'password':''}
    #Authentication Required.
    def delete(self):
        #response:
        #status: 201, {'message':'User Deleted Successfully!'}
        #raise_error: U201, {'message':'Password Incorrect!!'}
        pass


#Post_Api to deal with the posts created by user.
def Post_API(Resource):
    #To create post by user.
    #Authentication Required.
    #Body: {'user_id':'','text':''}
    def post(self):
        #response:
        #status: 201, {'message':'Post Created Successfully!'}
        pass
    
    
    #To read the post created by user, can be read by users other than Author user.
    #Authentication Required.
    #Body: {'user_id':''}
    def get(self):
        #response:
        #status: 201,
        #JSON: {'post_id':'','text':'','likes':'','user_name':'post_author's name','created_at':''}
        pass


    #To edit/like post
    #Authentication Required.
    #Allow to edit post if and only if the current user's user_id is same as Author's user_id, do proper function internal validation accordingly during implementation.
    #Body: {'user_id':'','post_id':'','text':'only if required to edit the post'}
    def put(self):
        #response:
        #status: 201, {'message':'Post/Liked Edited Successfully!'}
        #raise_error: P201, {'message':'Author User is required to Edit Post!!'}
        pass


    #To Delete Post.
    #Authentication Required.
    #Can only be done by Author user.
    def delete(self):
        #response:
        #status: 201,{'message':'Post Deleted Successfully!!'}
        #raise_error: P201, {'message':'Author User is required to Delete Post!!'}
        pass