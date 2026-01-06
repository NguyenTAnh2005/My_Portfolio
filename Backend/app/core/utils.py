from passlib.context import CryptContext

#================= MẬT KHẨU =======================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function Hashing Pasword
def hashing_password(input):
   return pwd_context.hash(input)

# Checking Correct Password 
def checking_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)



