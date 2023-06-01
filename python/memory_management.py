from PIL import Image
import gc


image_path = '경로/이미지파일.jpg'
image = Image.open(image_path)


del image
gc.collect()
