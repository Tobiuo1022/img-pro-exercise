import sys
from PIL import Image
import numpy

# 処理する画像の名前を取得. 
image_name = sys.argv[1].split('/')[-1]

# 画像をpillowで扱える形に読み込んで変数に代入する. 
suba_img = Image.open(sys.argv[1])

# ----- マスク画像の作成. -----
# 画像を白黒にする. 
suba_mono_img = suba_img.convert("L")
# numpyで扱える形に変換して変数に代入する. 
suba_mono = numpy.array(suba_mono_img)

# 閾値よりも明るいピクセルを真っ白に, それ以外を真っ黒に. 
threshold = int(sys.argv[-1])
boolean = suba_mono > threshold
mask = boolean * 255
# numpyから画像に変換. 
mask_img = Image.fromarray(numpy.uint8(mask))

# ----- グリーンバックの画像の作成. -----
height = suba_mono.shape[0]
width = suba_mono.shape[1]
greenback = numpy.array([[[0, 255, 0] for pixel in range(width)] for row in range(height)])
# numpyから画像に変換. 
green_img = Image.fromarray(numpy.uint8(greenback))

# ----- 合成. -----
suba_gpla = Image.composite(green_img, suba_img, mask_img)

# ----- 保存. -----
save_path = "../image/after/"
suba_gpla.save(save_path + image_name)
