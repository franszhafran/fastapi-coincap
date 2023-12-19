from .base_controller import BaseController

from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    password: str
    password_confirmation: str

class AuthController(BaseController):
    service = None

    def __init__(self, service):
        self.service  = service
    
    def login(self, request: LoginRequest):
        login = self.service.login(request.email, request.password)
        return {"code": 200, "data": login}
    
    def register(self, request: RegisterRequest):
        register = self.service.register(request.email, request.password)
        return self.send_ok()