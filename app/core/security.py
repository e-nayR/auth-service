from passlib.context import CryptContext

PasswordSvc = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return PasswordSvc.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return PasswordSvc.verify(plain_password, hashed_password)

# UPDATE User Password Example
# if PasswordSvc.verify(password, user.hashed_password):
#     if PasswordSvc.needs_update(user.hashed_password):
#         user.hashed_password = PasswordSvc.hash(password)
