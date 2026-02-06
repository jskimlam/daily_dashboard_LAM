from PIL import Image
import os

# 1. 파일 경로 설정
input_file = "latest.png"  # 원본 파일명
output_file = "latest.webp" # 변환될 파일명

# 2. 이미지 열기
with Image.open(input_file) as img:
    # 3. 리사이징 (이미지가 너무 크면 너비를 1000px 정도로 조절)
    if img.width > 1000:
        ratio = 1000 / float(img.width)
        new_height = int(float(img.height) * ratio)
        img = img.resize((1000, new_height), Image.Resampling.LANCZOS)
    
    # 4. 진짜 WebP로 변환하며 저장 (압축률 80% 설정)
    img.save(output_file, "WEBP", quality=80, optimize=True)

print(f"✅ 변환 완료! 용량: {os.path.getsize(output_file)//1024}KB")
