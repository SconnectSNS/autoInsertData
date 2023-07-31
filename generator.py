import requests
import os
import random

# 사용할 사진관 이름
nicknames = ["빛의렌즈", "스냅퓨전", "무한사진", "사진오라", "셔터꿈",
             "플래시일식", "클릭의본질", "생생스냅샷", "픽셀낙원", "셔터의정신",
             "완벽한사진", "렌즈의기적", "플래시기억", "영원한클릭", "생생한기억"]

# 제목과 내용
titles_contents = [
    ("여행사진입니다", "여행의 추억을 남겨보세요"),
    ("자연사진입니다.", "자연의 아름다움을 즐겨보세요 :)"),
    ("사진을 통해 여행을 추억으로", "여행 사진 위주로 촬영해드립니다."),
    ("해외 여행사진 전문입니다.", "일본, 대만 등 아시아 지역에서 여행한 사진을 촬영합니다."),
    ("메뉴사진 찍어드립니다.", "메뉴판, 가게 홍보등에 사용하실 메뉴 사진 촬영해드립니다."),
    ("인스타 업로드 사진 피드백드립니다.", "인스타에 업로드할 사진을 쉽고 빠르게 편집 및 수정해드립니다."),
    ("파리에 거주중인 사진작가입니다.", "건축물 및 풍경을 위주로 사진 촬영합니다. 파리에서 사진 촬영이 필요하신분들은 연락 부탁드립니다."),
    ("음식 사진 위주로 찍어요~", "sns 홍보용으로 사용하실 음식 사진을 촬영해드립니다. 가격 문의는 DM 부탁드립니다."),
    ("개인 프로필, 우정 사진 등 촬영해드립니다.", "우정 사진, 개인 프로필 사진 등 촬영합니다."),
    ("동아리 홍보에 사용하실 단체사진 촬영합니다.", "단체사진 촬영합니다. 필요하신분은 연락 부탁드립니다."),
    ("지나가는 시간 추억을 사진으로 촬영해드립니다!", "안녕하세요 사진작가 홍길동입니다! 사진관에서 우정 사진 촬영해드립니다 :) 많은 관심 부탁드려요~"),
    ("스튜디오 반려동물 사진입니다.", "반려동물 사진을 스튜디오에서 촬영해드립니다."),
    ("자신의 반려동물과 사진을 남겨보세요!", "반려동물과 함께 출장 사진 찍어드립니다! 원하시는 분은 dm으로 문의 부탁드릴게요~"),
    ("개인 프로필 사진 촬영합니다.", "야외에서 프로필 사진 및 애완동물과 사진 촬영 해드립니다."),
    ("웨딩사진입니다.", "웨딩사진 전문으로 촬영합니다."),
    ("야외 웨딩사진 촬영 전문", "야외에서 촬영하는 웨딩사진 전문입니다."),
    ("스튜디오 웨딩사진 촬영합니다.", "스튜디오에서 웨딩 촬영 원하시는 신랑, 신부님들 연락 기다립니다~"),
    ("스튜디오 한복 결혼사진 원하시는분 연락 부탁드려요~", "웨딩사진 전문기사로 한복사진 위주로 촬영합니다!"),
    ("웨딩사진 촬영합니다.", "웨딩사진입니다."),
    ("지원서, 프로필 등 개인사진 촬영합니다.", "회사 지원서, 프로필 등 개인사진 위주로 촬영합니다."),
    ("개인사진 필요하신분 연락부탁드립니다.", "스튜디오 촬영 위주로 진행합니다. 개인 프로필 사진 원하시는분들 연락 부탁드립니다."),
    ("해외 풍경사진 위주로 촬영합니다.", "원하시는 사진 문의 부탁드립니다."),
    ("아름다운 자연 풍경을 찍습니다.", "우리나라 문화재 및 자연풍경 사진들을 찍습니다."),
    ("사진 촬영합니다.", "피사체를 가리지 않고 촬영합니다."),
    ("자연 풍경 촬영합니다.", "자연 풍경을 위주로 촬영합니다."),
    ("가족사진 및 프로필사진입니다.", "화목한 가족 사진이 될 수 있도록 노력하고있습니다~"),
    ("화보사진입니다.", "모델, 배우분들이나 개인화보 촬영합니다."),
    ("인물사진 촬영합니다.", "인물사진 위주로 촬영합니다.")
]


# 사용자 수와 게시글 수
num_users = 15
num_posts_per_user = 6

# 파일 경로
file_dir = "./"
counter=1
# 회원 가입과 로그인
for i in range(num_users):
    # 회원 가입
    print(f"Signing up user{i}...")
    signup_data = {
        "email": f"user{i}@gmail.com",
        "nickname": nicknames[i],
        "password": "password1"
    }
    signup_response = requests.post('http://localhost:8081/api/users/signup', json=signup_data)
    signup_response.raise_for_status()

    # 로그인
    print(f"Logging in user{i}...")
    login_data = {
        "email": f"user{i}@gmail.com",
        "password": "password1"
    }
    login_response = requests.post('http://localhost:8081/api/users/login', json=login_data)
    login_response.raise_for_status()

    # 엑세스 토큰 추출
    print(f"Extracting access token for user{i}...")
    access_token = login_response.json()["accessToken"]

    # 이미지 업로드와 게시글 작성
    for j in range(num_posts_per_user):
        # 이미지 업로드
        print(f"Uploading image{counter+1} for user{i}...")
        with open(os.path.join(file_dir, f"{counter+1}.jpg"), 'rb') as img_file:
            upload_response = requests.post('http://localhost:8082/api/sns/upload',
                                            files={"file": img_file})
            upload_response.raise_for_status()

            # 이미지 URL과 ID 추출
            image_url = upload_response.json()["imageUrls"]
            image_id = upload_response.json()["imageId"]
            counter=counter+1

        # 게시글 작성
        print(f"Posting for user{i}...")
        title_content_index = (i * num_posts_per_user + j) % len(titles_contents)
        post_data = {
            "title": titles_contents[title_content_index][0],
            "content": titles_contents[title_content_index][1],
            "imageUrl": image_url,
            "imageId": image_id,
            "userId": i+2
        }
        post_headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        post_response = requests.post('http://localhost:8082/api/sns/', headers=post_headers, json=post_data)
        post_response.raise_for_status()

    print(f"Finished processing for user{i}\n")
