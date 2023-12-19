from fastapi import Request
from exception import AuthorizationException
import jwt
import os

class BaseController():
    auth_service = None
    def __init__(self, auth_service = None):
        self.auth_service = auth_service
        self.key = os.getenv('APP_KEY')
        
    def send_ok(self):
        return {"code": 200, "message": "OK"}
    
    def send_data(self, data):
        return {"code": 200, "message": "OK", "data": data}
    
    def send_error(self, code: int, error):
        if isinstance(error, AuthorizationException):
            code = 401

        return {"code": code, "message": "error", "data": str(error)}
    
    def check_token(self, request: Request):
        token = request.headers.get("Authorization")
        if token is None or token == "":
            raise AuthorizationException("unauthorized")
        
        jwt_decoded = jwt.decode(token[7:], self.key, algorithms="HS256")
        return self.auth_service.get_user(jwt_decoded['id'])