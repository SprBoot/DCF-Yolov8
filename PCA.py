import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from PIL import Image

# # 读取图像
# image_path = "D:\\workspace\\pycharm\\ultralytics-improve\\ultralytics\\yolo\\v8\\detect\\VOCdevkit\\VOCdevkit\\VOC2007\\voc_train\\images\\IP000000249.jpg"
# image = Image.open(image_path)
#
# # 将图像转换为NumPy数组
# image_data = np.array(image)
#
# # 获取图像数据的形状
# image_shape = image_data.shape
#
# # 将图像数据展平为一维数组
# image_flattened = image_data.flatten()
#
# # 绘制图像数据的分布
# plt.hist(image_flattened, bins=256)
# plt.xlabel('Pixel Value')
# plt.ylabel('Frequency')
# plt.title('Pixel Value Distribution')
# plt.show()
import numpy as np
import matplotlib.pyplot as plt

def mish(x):
    return x * np.tanh(np.log(1 + np.exp(x)))

x = np.linspace(-5, 5, 100)  # 定义输入范围

y = mish(x)  # 计算Mish激活函数的输出

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Mish(x)')
plt.title('Mish Activation Function')
plt.grid(True)
plt.show()
