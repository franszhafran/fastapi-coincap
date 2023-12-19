from .base_controller import BaseController
from service import CoincapService
from pydantic import BaseModel
from fastapi import Request

class TrackCoinRequest(BaseModel):
    coin: str

class RegisterRequest(BaseModel):
    email: str
    password: str
    password_confirmation: str

class TrackedCoinController(BaseController):
    tracked_coin_service = None
    coincap_service = None

    def __init__(self, auth_service, tracked_coin_service, coincap_service):
        self.tracked_coin_service = tracked_coin_service
        self.coincap_service = coincap_service

        super().__init__(auth_service=auth_service)

    def assets(self, request: Request):
        user = self.check_token(request)

        return self.send_data(self.coincap_service.assets())

    def user_coin(self, request: Request):
        user = self.check_token(request)

        return self.send_data(self.tracked_coin_service.get_tracked_coins(user.id))
    
    def track_coin(self, request: Request, data: TrackCoinRequest):
        user = self.check_token(request)

        self.tracked_coin_service.add_to_tracked_coins(user.id, data.coin)

        return self.send_ok()

    def remove_tracked_coin(self, request: Request, data: TrackCoinRequest):
        user = self.check_token(request)

        self.tracked_coin_service.remove_from_tracked_coins(user.id, data.coin)

        return self.send_ok()
    