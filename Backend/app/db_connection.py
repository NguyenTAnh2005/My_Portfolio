from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
DATABASE_URL_CONNECT = os.getenv("DATABASE_URL")

# Tạo Engine để kết nối đến CSDL
engine = create_engine(DATABASE_URL_CONNECT)

# Tạo Sessionmaker để tạo các phiên làm việc với CSDL
Session_Local = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# Tạo lớp cơ sở cho các mô hình ORM
Base = declarative_base()

# Hàm lấy phiên làm việc với CSDL
def get_db():
    db = Session_Local()
    try:
        yield db
    finally:
        db.close()


