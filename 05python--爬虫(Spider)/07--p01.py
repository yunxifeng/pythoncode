import pytesseract as pt
from PIL import Image

# 生成图像实例
image = Image.open("pt.png")
# 调用pytesseract,把图片转换成文字
text = pt.image_to_string(image)
print(text)