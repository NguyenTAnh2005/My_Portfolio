from passlib.context import CryptContext
from datetime import datetime

#================= MẬT KHẨU =======================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function Hashing Pasword
def hashing_password(input):
   return pwd_context.hash(input)

# Checking Correct Password 
def checking_password(plain_password, hashed_password):
   return pwd_context.verify(plain_password, hashed_password)

# Convert time string from github response API to DateTime for PostgreSQL
def parse_github_date(date_str):
   """
   biến đổi chuỗi ở sau cùng và dùng hàm của thư viện biến đổi chuỗi ra object datetime để Máy tính hiểu đc
   """
   if not date_str: return datetime.now()
   return datetime.fromisoformat(date_str.replace("Z", "+00.00"))



