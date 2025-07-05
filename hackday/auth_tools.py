import jwt

def decode_jwt(token):
    try:
        return jwt.decode(token, options={"verify_signature": False})
    except Exception as e:
        return str(e)
