import httpx
from app.core.config import settings

async def fetch_github_repo_info(repo_url: str):
    """
     Calling Github API - return info about a reposity by input url
    """
    #rstip đảm bảo ko có / thừa ở cuối 
    # split sẽ phân ra nhiều phần tử nhưng ta chỉ cần 2 phần tử cuối là owner và repo
    # # Ví dụ: https://github.com/NguyenTAnh2005/Habit_Tracker -> NguyenTAnh2005/Habit_Tracker 
    parts = repo_url.rstrip("/").split("/")
    if len(parts) < 2: 
        return None
    # tham số gọi Github API 
    owner_repo = f"{parts[-2]}/{parts[-1]}"

    # Thiết lập Header với Token để không bị giới hạn lượt gọi
    headers = {
        "Authorization" : f"token {settings.GITHUB_TOKEN}",
        "Accept" : "application/vnd.github.v3+json"
    }
    
    base_api_url = f"https://api.github.com/repos/{owner_repo}"
    languages_url = f"{base_api_url}/languages"
    async with httpx.AsyncClient() as client:
        try:
            repo_response = await client.get(base_api_url, headers = headers)
            lang_response = await client.get(base_api_url, headers = headers)

            if repo_response.status_code == 200:
                repo_data = repo_response.json()
                lang_data = lang_response.json() if lang_response.status_code == 200 else {}
                return {
                    "description" : repo_data.get("description"),
                    "created_at" : repo_data.get("created_at"),
                    "last_updated" : repo_data.get("pushed_at"),
                    "tech_stack" : list(lang_data.key())
                }
            else:
                print(f"❌ Lỗi từ GitHub: {repo_response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Lỗi kết nối API: {e}")
            return None