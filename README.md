# ComfyUI-Pil2Tensor
# 图片从tensor转换成PIL图像
from PIL import Image

import numpy as np

import torch


def ac_tensor2pilac(image):

    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def ac_pil2tensor(image):

    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
# 图片转64位编码格式并返回
import base64

f = open(r'D:\AC Center\Button.png','rb')

res = f.read()

s = base64.b64encode(res)

f.close()


print(s)   
