import os
from PIL import Image

SCALE_FACTOR = 0.7


for filename in os.listdir('../'):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        src_path = os.path.join('../', filename)
        dst_path = os.path.join('../downsized', filename)
        try:
            with Image.open(src_path) as img:
                new_size = (int(img.width * SCALE_FACTOR), int(img.height * SCALE_FACTOR))
                downsized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                downsized_img.save(dst_path)
        except Exception as e:
            print(f"Skipping {filename}: {e}")