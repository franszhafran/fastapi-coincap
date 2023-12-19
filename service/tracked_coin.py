from model import TrackedCoin
from sqlalchemy.orm import Session
from .coincap import CoincapService

class TrackedCoinService():
    def __init__(self, db, coincap_service):
        self.db: Session = db
        self.coincap_service: CoincapService = coincap_service
    
    def get_tracked_coins(self, user_id: int):
        query = self.db.query(TrackedCoin).filter(TrackedCoin.user_id == user_id)
        rows = query.all()
        for row in rows:
            usd_price = self.coincap_service.get_price(row.coin)
            rate = self.coincap_service.get_usd_rate()
            row.price = usd_price * rate
        return rows
    
    def add_to_tracked_coins(self, user_id: int, coin: str):
        check = self.db.query(TrackedCoin).filter(TrackedCoin.user_id == user_id).filter(TrackedCoin.coin == coin).first()
        if check is None:
            tc = TrackedCoin()
            tc.user_id = user_id
            tc.coin = coin
            self.db.add(tc)
            self.db.commit()

    def remove_from_tracked_coins(self, user_id: int, coin: str):
        check = self.db.query(TrackedCoin).filter(TrackedCoin.user_id == user_id).filter(TrackedCoin.coin == coin).first()
        if check is not None:
            self.db.query(TrackedCoin).filter(TrackedCoin.user_id == user_id).filter(TrackedCoin.coin == coin).delete()
            self.db.commit()