import asyncio
from app.db_connection import Session_Local
from app.models import models
from app.core.config import settings
from app.core.utils import hashing_password, parse_github_date
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
        major = "Kỹ sư phần mềm - Solfware Engineer",
        languages = ["Python", "HTML", "CSS", "JavaScript", "C#","Java"],
        frameworks = ["Bootstrap", "Tailwind", "React", "FastAPI", "MVC .Net"],
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
            "tech_stack" : ["FastAPI", "PostgreSQL", "JWT", "SQLalchemy", "Alembic Migration", "React", "Tailwind", "React-router-DOM", "Lucide React", "ChartJS", "React Calendar Heatmap", "React Tooltip"]
        },
# {PostgreSQL,Mako,HTML,FastAPI,"Lucide React",Python,"React Toolip",JavaScript,CSS,JWT,ChartJS,"React Calender Heatmap",SQLalchemy,"Alembic Migration",React-router-DOM,React,Tailwind}
    ]
    for project in list_projects:
        github_info = await fetch_github_repo_info(project["project_url"])

        if github_info:
            
            final_tech = project["tech_stack"].copy()
            for tech in github_info["tech_stack"]:
                if tech not in final_tech:
                    final_tech.append(tech)

            added_project = models.Project(
                title = project["title"],
                description = github_info["description"],
                thumbnail_url = project["thumbnail_url"],
                project_url = project["project_url"],
                deploy_url = project["deploy_url"],
                tech_stack = final_tech,
                created_at = parse_github_date(github_info["created_at"]),
                last_updated = parse_github_date(github_info["last_updated"])
            )
            db.add(added_project)

    db.commit()
    print("Thêm seed data project thành công!")
                     
# Category
def seed_data_categories(db):
    categories = [
        {"id" : 1,"name": "Học tập", "slug": "hoc-tap--hocthuat", "description": "Chia sẻ kiến thức, kinh nghiệm trong quá trình học tập chính"},
        {"id" : 2,"name": "Giải trí", "slug": "giaitri-thethao", "description": "Chia sẻ xung quanh về giải trí, thể thao"},
        {"id" : 3,"name": "Đời sống", "slug": "life", "description": "Chia sẻ các câu chuyện xung quanh đời sống"},
        {"id" : 4,"name": "Kiến thức", "slug": "other--learning", "description": "Chia sẻ các kiến thức ngoài lĩnh vực đang học tập"},
        {"id" : 5,"name": "Khác", "slug": "other", "description": "Lĩnh vực chưa được phân loại"},
    ]
    for cat in categories:
        db.add(models.Category(**cat))
    db.commit()
    print("Thêm seed data category thành công!")

# Blogs
def seed_data_blogs(db):
    blog_1_content = """
    Đó là thời điểm vào học kỳ đầu tiên của năm học thứ 3. Cũng là thời điểm sau 6 tháng mình làm quen với bộ ba cơ bản HTML-CSS-JavaScript.
     Đây là dự án cho môn học phát triển ứng dụng mã nguồn mở. Và đương nhiên, đây là lần đầu bản thân mình thực sự code một dự án fullstack nên chắc chắn vẫn còn khá nhiều thứ thiếu sót. 
     Tuy nhiên đối với bản thân mình thì đây là dự án thứ 2 mà bản thân mình thực sự tâm đắc (dự án đầu tiên là một CV sau nửa học kỳ làm quen với html-css-js). 
     Dự án được giảng viên yêu cầu bắt buộc backend cần dùng FastAPI kết hợp JWT và dùng PostgreSQL, đây cũng là phần mình code nhiều hơn là frontend - phần giảng viên cho phép dùng AI hỗ trợ. 
     Ở frontend dự án này thì mình dùng React với Vite. Dự án được mô tả là sẽ theo dõi thói quen của người dùng, thống kê lịch sử checkin các thói quen cũng như biểu hiện ra các sơ đồ trực quan (hình tròn, cột).
     Thời điểm này cũng có khá nhiều môn học cùng có dự án cuối kỳ nên thực sự thời gian để dành cho dự án này là không hề nhiều, với đối với một người chân ướt chân ráo - chưa có kinh nghiệm nhiều về code một web đầy đủ frontend - backend,
     thì đây thực sự là một khó khăn. Tuy nhiên, với công nghệ trí tuệ nhân tạo càng ngày phát triển, ngoài các kiến thức giảng viên cung cấp trên lớp học, thì mình cũng dùng một AI chat - Gemini Pro 2.5+, với sự hỗ trợ 
     của nó đã giúp mình hiểu hơn về quy trình thực hiện backend - từ việc xây dựng CSDL, tạo các models, triển khai các API endpoint, tích hợp JWT, xây dựng CORC, kết nối backend - frontend. Và gần như 90% code frontend đều 
     được AI này code <hộ>, tuy nhiên phần này giảng viên không yêu cầu mình phải code, chủ yếu giảng viên chỉ yêu cầu về backend hơn là front. Dù dự án khá thành công nhưng tồn tại song song một số điểm còn thiếu về dự án cũng 
     như cách mình triển khai code web fullstack. Đây sẽ là một động lực thúc đẩy bản thân mình có thể phát triển nhiều hơn. Và trước hết là mình sẽ triển khai một dự án Portfolio - cũng dùng các công cụ như trên. Mục đích là để
     có thể củng cố lại kiến thức backend như trên và quan trọng là nắm vững React căn bản nhất cho một frontend thay vì copy patse như frontend dự án habit-tracker này.
"""
    db.add(models.Blog(
            title="Dự án fullstack đầu tiên và ổn áp nhất của tôi!",
            slug="du-an-fullstack--first",
            summary="Bài viết chia sẻ hành trình bản thân mình code một dự án fullstack đầu tiên và oke nhất!",
            content= blog_1_content,
            category_id = 1,
            status="published",
            thumbnail_url="https://res.cloudinary.com/df5mtvzkn/image/upload/v1767752471/My_Portfolio/Blogs/blog__1/Habit_Tracker_qht1gv.png"
        ))
    db.commit()
    print("Thêm seed data blog thành công!")


async def seed_data():
    db = Session_Local()

    try:
        # Kiểm tra xem bên trong bảng System config đã có flag thêm dl mẫu chưa 
        check_is_seeded = db.query(models.SystemConfig).filter_by(config_key = "is_seeded").first()
        if check_is_seeded and check_is_seeded.config_value == "true":
            print("🚀 Dữ liệu mẫu đã có sẵn, bỏ qua bước chạy seed data!")
            return
        
        # Nếu như chưa có data mẫu thì thêm
        print("🌱 Bắt đầu quá trình nạp dữ liệu...")
        seed_data_roles(db)
        seed_data_users(db)
        seed_data_myinfo(db)
        seed_data_categories(db)
        seed_data_blogs(db)

        await seed_data_projects(db)

        if check_is_seeded:
            check_is_seeded.config_value = "true"
        else: 
            new_config = models.SystemConfig(config_key = "is_seeded", config_value = "true")
            db.add(new_config)

        db.commit()
        print("✅🎉 Hoàn tất nạp dữ liệu lần đầu và đánh dấu Flag!")

    except Exception as e:
        db.rollback()
        print(f"❌ Lỗi: {e}")
    finally:
        db.close()  

if __name__ == "__main__":
    asyncio.run(seed_data())



