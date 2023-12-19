from sqlalchemy import Boolean, Column, Integer, String
from dependency import Base

class TrackedCoin(Base):
    __tablename__ = "tracked_coins"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    coin = Column(String)