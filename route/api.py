from fastapi import FastAPI, APIRouter, Request
from controller import AuthController, TrackedCoinController
from dependency import Dependency

def setup_public_route(app: FastAPI):
    router = APIRouter()

    resolver = Dependency()
    resolver.resolve()

    # authentication
    auth_controller = AuthController(resolver.auth_service)
    router.add_api_route("/login", auth_controller.login, methods=["POST"])
    router.add_api_route("/register", auth_controller.register, methods=["POST"])

    app.include_router(router)

def setup_private_route(app: FastAPI):
    router = APIRouter()

    resolver = Dependency()
    resolver.resolve()

    tracked_coins_controller = TrackedCoinController(resolver.auth_service, resolver.tracked_coin_service, resolver.coincap_service)
    router.add_api_route("/coins", tracked_coins_controller.assets, methods=["GET"])
    router.add_api_route("/user/tracked-coins", tracked_coins_controller.user_coin, methods=["GET"])
    router.add_api_route("/user/tracked-coins", tracked_coins_controller.track_coin, methods=["POST"])
    router.add_api_route("/user/tracked-coins", tracked_coins_controller.remove_tracked_coin, methods=["DELETE"])

    app.include_router(router)