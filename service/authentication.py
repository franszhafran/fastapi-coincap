from model import User
from sqlalchemy.orm import Session
from exception import AuthorizationException
import time
import os

class AuthenticationService():
    def __init__(self, db):
        self.db: Session = db
        self.app_key = os.getenv('APP_KEY')

    def login(self, email: str, password: str):
        import jwt
        user = self.db.query(User).filter(User.email == email).first()
        if user is not None:
            if user.check_password(password):
                token = jwt.encode({"id": user.id, "time": int(time.time())}, self.app_key, algorithm="HS256")
                return {"token": token}
            else:
                raise AuthorizationException("invalid credentials")
        raise AuthorizationException("invalid credentials")
    
    def register(self, email: str, password: str):
        user = User()
        user.email = email
        user.set_password(password)
        self.db.add(user)
        self.db.commit()

    def get_user(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
        