# auth.py
from functools import wraps
from flask import request, Response
import base64

USERNAME = "admin"
PASSWORD = "password"

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not (auth.username == USERNAME and auth.password == PASSWORD):
            return Response("Authentication required", 401, {"WWW-Authenticate": "Basic realm='Login Required'"})
        return f(*args, **kwargs)
    return decorated
