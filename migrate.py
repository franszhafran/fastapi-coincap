from dependency import Base, engine

# state your models here
from model import User
from model import TrackedCoin

Base.metadata.create_all(bind=engine)