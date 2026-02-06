from PIL import Image
import os

# 원본은 images/latest.png에 있고, 결과물도 images/latest.webp로 저장해야 합니다.
input_path = 'images/latest.png'
output_path = 'images/latest.webp'

def process_image():
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with Image.open(input_path) as img:
        img = img.convert("RGB")
        img.save(output_path, 'WEBP', quality=80)
        print("Success!")

if __name__ == "__main__":
    process_image()
