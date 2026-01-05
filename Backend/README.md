```
/my_portfolio
├── main.py              # File chạy chính
├── .env                 # Lưu các mật khẩu, link DB (đừng push cái này lên github nhé)
├── /app
│   ├── /models          # Chứa SQLAlchemy Models (Database)
│   ├── /schemas         # Chứa Pydantic Models (Dữ liệu đầu vào/ra)
│   ├── /routers         # Chia nhỏ API (blog.py, project.py, auth.py)
│   ├── /core            # Chứa cấu hình bảo mật, JWT, config
│   └── database.py      # Kết nối DB
└── alembic/             # Thư mục chứa các file migration
```