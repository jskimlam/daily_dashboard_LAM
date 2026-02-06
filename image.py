from PIL import Image
import os

input_path = 'images/latest.png'
output_path = 'images/latest.webp'

def process_image():
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with Image.open(input_path) as img:
        img = img.convert("RGB") # PNG의 투명도를 처리하기 위해 RGB로 변환
        img.save(output_path, 'WEBP', quality=80)
        print("Success: latest.webp created")

if __name__ == "__main__":
    process_image()
