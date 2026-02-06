import os
import glob
import shutil
from datetime import datetime
from PIL import Image

def process_and_archive():
    source_dir = 'images'
    archive_dir = 'images/archive'
    
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # 1. images 폴더 내 모든 png 파일 검색
    image_files = glob.glob(f'{source_dir}/*.png')
    if not image_files:
        print("새로운 PNG 파일이 없습니다.")
        return

    # 2. 가장 최근에 업로드된 파일 선정
    latest_source = max(image_files, key=os.path.getmtime)
    
    # 3. WebP 변환 (파일명은 항상 latest.webp로 고정)
    output_webp = f'{source_dir}/latest.webp'
    with Image.open(latest_source) as img:
        img.save(output_webp, 'WEBP', quality=80)
    
    # 4. 원본 파일 아카이브 (이름 앞에 날짜를 붙여 중복 방지)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.basename(latest_source)
    archive_name = f"{timestamp}_{file_name}"
    
    shutil.move(latest_source, os.path.join(archive_dir, archive_name))
    print(f"완료: {archive_name} 아카이브 및 latest.webp 업데이트")

if __name__ == "__main__":
    process_and_archive()
