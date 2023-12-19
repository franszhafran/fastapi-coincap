from sqlalchemy import Boolean, Column, Integer, String
from dependency import Base
import hashlib

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    """
    Password setter with automatic hashing
    """
    def set_password(self, password: str):
        salt = password[:4]
        password = password.encode('utf-8')
        salt = salt.encode('utf-8')
        hashed_password = hashlib.sha256(password + salt).hexdigest()
        self.password = hashed_password

    """
    Check wether current model password equal to password againts
    """
    def check_password(self, password_againts: str) -> bool:
        if len(password_againts) < 4:
            return False

        salt = password_againts[:4].encode('utf-8')
        password_againts_hashed = hashlib.sha256(password_againts.encode('utf-8') + salt).hexdigest()
        return self.password == password_againts_hashed