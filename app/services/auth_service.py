from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash, verify_password


class AuthService:
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()


    @staticmethod
    def create_user(db: Session, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = User(email = user.email, hashed_password = hashed_password, full_name=user.full_name)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


    @staticmethod
    def authenticate_user(db:Session, email: str, password: str):
        user = AuthService.get_user_by_email(db, email)
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user
