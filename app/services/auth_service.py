from app.schemas.auth import UserInDB
from app.services.security_service import verify_password


def get_user(db, email: str):
    user_dict = next(filter(lambda u: u["email"] == email, db), None)
    if user_dict is None:
        return None
    return UserInDB(**user_dict)

def authenticate_user(fake_db, email: str, password: str):
    user = get_user(fake_db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user