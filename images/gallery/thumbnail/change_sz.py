import os
from PIL import Image

os.chdir('./') #해당 폴더로 이동
files = os.listdir(os.getcwd()) #현재 폴더에 있는 모든 파일을 list로 불러오기

def resize(img,minsize):
    width=img.size[0]
    height=img.size[1]

    if(height<width):
        new_width  = minsize
        new_height = int(new_width * height / width)
    else:
        new_height = minsize
        new_width  = int(new_height * width / height)

    img=img.resize((new_width,new_height),Image.LANCZOS)
    return img

for file in files:
    if file.split('.')[-1] != 'jpg':
        continue
    img = Image.open(file)  # 이미지 불러오기
    img_size = img.size  # 이미지의 크기 측정
    # 직사각형의 이미지가 256x512 이라면, img_size = (256,512)가 된다.
    x = img_size[0]  # 넓이값
    y = img_size[1]  # 높이값

    if x != y:
        size = max(x, y)
        resized_img = Image.new(mode='RGB', size=(size, size), color=(255, 255, 255))
        offset = (round((abs(x - size)) / 2), round((abs(y - size)) / 2))
        resized_img.paste(img, offset)
        resized_img = resize(resized_img, 300)
        resized_img.save(file + '_resized.png')