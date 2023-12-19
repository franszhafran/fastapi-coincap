from .database import SessionLocal

class Dependency():
    auth_service = None
    tracked_coin_service = None
    coincap_service = None

    def get_db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
            
    def resolve(self):
        from service import AuthenticationService
        from service import TrackedCoinService
        from service import CoincapService

        self.auth_service = AuthenticationService(SessionLocal())
        self.coincap_service = CoincapService()
        self.tracked_coin_service = TrackedCoinService(SessionLocal(), self.coincap_service)
        return
