from fastapi import Depends, HTTPException, status
from fastapi import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.security import verify_token
from app.services.auth_service import AuthService


# Security Bearer Token Dependency
# This dependency is used to authenticate the user by verifying the token
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    # Get the token from the credentials
    token = credentials.credentials

    # Verify the token via verify_token function
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code = status.HTTP_401_UNATHOURIZED,
        detail = "Could not validate credentilas",
        headers = {"WWW-Authenticate = Bearer"}
        )

    # Get the email from the payload
    email = payload.get("sub")
    if email is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials")
    
    # Get the user by email from the database
    user = AuthService.get_user_by_email(db, email = email)

    if user is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user