import jwt
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import status
from app.core.config import ALGORITHM, SECRET_KEY

class AuthorizeRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path in ["/docs", "/openapi.json", "/auth/login", "/auth/register"]:
            return await call_next(request)
        if request.method == "OPTIONS":
            return await call_next(request)
        
        bearer_token = request.headers.get('Authorization')
        if bearer_token is None or not bearer_token.startswith('Bearer '):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "detail": "Missing access token",
                }
            )

        try:
            token = bearer_token.split(" ")[1]

            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            request.state.user = payload
        except jwt.PyJWTError:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": "Invalid or expired token"}
            )

        return await call_next(request)