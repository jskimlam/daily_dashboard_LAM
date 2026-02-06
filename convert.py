import os
import glob
import shutil
import json
from datetime import datetime
from PIL import Image

def process_and_archive():
    source_dir = 'images'
    archive_dir = 'images/archive'
    
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # 1. 새로운 PNG 파일 찾기
    image_files = glob.glob(f'{source_dir}/*.png')
    if image_files:
        latest_source = max(image_files, key=os.path.getmtime)
        
        # WebP 변환 (최신본 업데이트)
        with Image.open(latest_source) as img:
            img.save(f'{source_dir}/latest.webp', 'WEBP', quality=80)
        
        # 2. 원본 이동 (사용자 파일명을 우선하되, 중복 방지를 위해 뒤에 시간 추가)
        file_name = os.path.basename(latest_source) # 예: 260206.png
        name, ext = os.path.splitext(file_name)
        
        # 아카이브 파일명 설정: 사용자파일명_시간.png (날짜가 앞에 오므로 정렬에 유리)
        timestamp = datetime.now().strftime("%H%M%S")
        archive_name = f"{name}_{timestamp}{ext}" 
        
        shutil.move(latest_source, os.path.join(archive_dir, archive_name))
        print(f"아카이브 완료: {archive_name}")

    # 3. 아카이브 목록 생성 (파일명 기준 내림차순 정렬 -> 최신 날짜가 위로)
    # os.listdir로 가져온 목록을 sorted(reverse=True)하면 260206이 260205보다 위에 옵니다.
    archive_list = sorted(os.listdir(archive_dir), reverse=True)
    
    with open(f'{source_dir}/list.json', 'w', encoding='utf-8') as f:
        json.dump(archive_list, f, ensure_ascii=False, indent=4)
        
    print("목록 정렬 및 갱신 완료!")

if __name__ == "__main__":
    process_and_archive()
