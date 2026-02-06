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
        
        # 원본 이동 (날짜 포함)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = os.path.basename(latest_source)
        archive_name = f"{timestamp}_{file_name}"
        shutil.move(latest_source, os.path.join(archive_dir, archive_name))

    # 2. 아카이브 폴더 내 모든 파일 목록 생성 (웹페이지용)
    archive_list = sorted(os.listdir(archive_dir), reverse=True) # 최신순 정렬
    with open(f'{source_dir}/list.json', 'w', encoding='utf-8') as f:
        json.dump(archive_list, f, ensure_ascii=False, indent=4)
        
    print("목록 갱신 완료!")

if __name__ == "__main__":
    process_and_archive()
