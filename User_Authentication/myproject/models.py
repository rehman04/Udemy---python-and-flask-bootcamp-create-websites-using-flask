from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin #it handles all users request, user logins and authorizing them, it handles all interactial views

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    passowrd_hash=db.Column(db.String(128))


    def __init__(self,email,username,passowrd):
        self.email=email
        self.username=username
        self.passowrd_hash=generate_password_hash(password)


    def check_password(self,password):
        return check_password_hash(self.passowrd_hash,password)
