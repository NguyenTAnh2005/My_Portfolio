from app.db_connection import Session_Local
from app.models import models
from app.core.config import settings
from app.core.utils import hashing_password
from app.core.github_repo_service import fetch_github_repo_info

# Role
def seed_data_roles(db):
    db.add(models.Role(id = 1, name = "Admin", description ="Quản trị hệ thống"))
    db.add(models.Role(id = 2, name = "User", description ="Người dùng thông thường"))
    db.commit()
    print("Thêm seed data role thành công!")

# Tài khoản Admin
def seed_data_users(db):
    user_1_pass = hashing_password(settings.FIRST_ADMIN_PASSWORD)
    user_1_email = settings.FIRST_ADMIN_EMAIL
    db.add(models.User(id = 1, username = "Admin_Nguyen_05", password = user_1_pass, email = user_1_email, role_id = 1))
    db.commit()
    print("Thêm seed data user admin thành công!")

# Thông tin cá nhân 
def seed_data_myinfo(db):
    db.add(models.Myinfo(
        id = 1,
        fullname = "Nguyễn Tuấn Anh",
        gender = "Nam",
        hometown = "Hà Tĩnh, Việt Nam",
        id = 1,
        fullname = "Nguyễn Tuấn Anh",
        gender = "Nam",
        hometown = "Hà Tĩnh, Việt Nam",
        major = "Kỹ sư phần mềm - Solfware Engineer",
        languages = ["Python", "HTML", "CSS", "JavaScript", "C#","Java"],
        tech_stack = ["Bootstrap", "Tailwind", "React", "FastAPI", "MVC .Net"],
        social_links = {
            "zalo" : "https://zalo.me/0328884320",
            "github" : "https://github.com/NguyenTAnh2005",
            "email" : "mailto=23050118@student.bdu.edu.vn",
            "facebook" : "https://www.facebook.com/share/14QaznFt8ZF",
            "youtube" : "https://www.youtube.com/@N_T_Anh",
            "instagram" : "https://www.instagram.com/tuananh06102005"
        },
        bio = "Trình độ - kinh nghiệm có thể ít nhưng tinh thần học hỏi thì không bao giờ thiếu!"
    ))
    db.commit()
    print("Thêm seed data myinfo thành công!")

# # Các Project ban đầu
async def seed_data_projects(db):
    list_projects = [
        {
            "title" : "Quản lý siêu thị với Object Oriented Programming",
            "thumbnail_url" : "https://res.cloudinary.com/df5mtvzkn/image/upload/v1767710892/My_Portfolio/Projects/duan_qly_sieuthiOOPCshap/home_w7qxnf.png",
            "project_url" : "https://github.com/NguyenTAnh2005/duan_qly_sieuthiOOPCshap",
            "deploy_url" : "",
            "tech_stack" : []
        },
        {
            "title" : "Hồ sơ cá nhân",
            "thumbnail_url" : "https://res.cloudinary.com/df5mtvzkn/image/upload/v1767711359/My_Portfolio/Projects/My_First_CV/my-vip-cv_tg8hoh.png",
            "project_url" : "https://github.com/NguyenTAnh2005/My_First_CV",
            "deploy_url" : "https://nguyentanh2005.github.io/My_First_CV/",
            "tech_stack" : []
        },
        {
            "title" : "Web nghe nhạc trực tuyến",
            "thumbnail_url" : "https://res.cloudinary.com/df5mtvzkn/image/upload/v1767711439/My_Portfolio/Projects/STAP_Music/stap-music_ued2w9.png",
            "project_url" : "https://github.com/NguyenTAnh2005/STAP_Music",
            "deploy_url" : "https://nguyentanh2005.github.io/STAP_Music/",
            "tech_stack" : []
        },
        {
            "title" : "Ứng dụng dạy nấu ăn ",
            "thumbnail_url" : "https://res.cloudinary.com/df5mtvzkn/image/upload/v1767711370/My_Portfolio/Projects/Let-Cook/let-cook_ptraje.jpg",
            "project_url" : "https://github.com/NguyenTAnh2005/Let-Cook",
            "deploy_url" : "",
            "tech_stack" : ["SQLite"]
        },
        {
            "title" : "Website bán điện thoại cũ",
            "thumbnail_url" : "https://res.cloudinary.com/df5mtvzkn/image/upload/v1767711413/My_Portfolio/Projects/asp_sellphone/asp-sellphone_siuupw.png",
            "project_url" : "https://github.com/NguyenTAnh2005/asp_sellphone",
            "deploy_url" : "http://oldphone.somee.com/",
            "tech_stack" : ["Bootstrap, SweetAlert, Asp .Net, Cloudianry, SQL Sever"]
        },
        {
            "title" : "Ứng dụng theo dõi thói quen",
            "thumbnail_url" : "https://res.cloudinary.com/df5mtvzkn/image/upload/v1767711400/My_Portfolio/Projects/Habit_Tracker/habit-tracker_f9lo64.png",
            "project_url" : "https://github.com/NguyenTAnh2005/Habit_Tracker",
            "deploy_url" : "https://habit-tracker-kappa-gold.vercel.app/",
            "tech_stack" : ["FastAPI", "PostgreSQL", "JWT", "SQLalchemy", "Alembic Migration", "React", "Tailwind", "React-router-DOM", "Lucide React", "ChartJS", "React Calender Heatmap", "React Toolip"]
        },

    ]
    for project in list_projects:
        github_info = await fetch_github_repo_info(project["project_url"])

        if github_info:
            added_project = models.Project(
                title = project["title"],
                description = github_info["description"],
                thumbnail_url = project["thumbnail_url"],
                project_url = project["project_url"],
                deploy_url = project["deploy_url"],
                tech_stack = github_info["tech_stack"],
                created_at = github_info["created_at"],
                last_updated = github_info["last_updated"]
            )
            db.add(added_project)

    db.commit()
    print("Thêm seed data project thành công!")
                
            
# Category

# Blogs



async def seed_data():
    db = Session_Local()

    try:
        # Kiểm tra xem bên trong bảng System config đã có flag thêm dl mẫu chưa 
        check_is_seeded = db.query(models.SystemConfig).filter_by(config_key = "is_seeded").first()
        if check_is_seeded and check_is_seeded.config_value == "true":
            print("🚀 Dữ liệu mẫu đã có sẵn, bỏ qua bước chạy seed data!")
            return
        # Nếu như chưa có data mẫu thì thêm
        seed_data_roles(db)
        seed_data_users(db)
        seed_data_myinfo(db)

        if check_is_seeded:
            check_is_seeded.config_value = "true"
        else: 
            new_config = models.SystemConfig(config_key = "is_seeded", config_value = "true")
            db.add(new_config)

        db.commit()
        print("✅ Hoàn tất nạp dữ liệu lần đầu và đánh dấu Flag!")

    except Exception as e:
        db.rollback()
        print(f"Lỗi: {e}")
    finally:
        db.close()  

if __name__ == "__main__":
    seed_data()



