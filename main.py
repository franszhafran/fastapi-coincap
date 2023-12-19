from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from route import setup_public_route, setup_private_route
from controller import BaseController

public_app = FastAPI()
private_app = FastAPI()

setup_public_route(public_app)
setup_private_route(private_app)

@private_app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        c = BaseController()
        return JSONResponse(c.send_error(500, e))

app = FastAPI()

app.mount("/public", public_app) 
app.mount("/private", private_app)