import numpy as np
import matplotlib.pyplot as plt

def silu(x):
    return x * (1 / (1 + np.exp(-x)))

def mish(x):
    return x * np.tanh(np.log(1 + np.exp(x)))

# 创建输入数据
x = np.linspace(-5, 5, 100)

# 计算SiLU和Mish的输出
y_silu = silu(x)
y_mish = mish(x)

# 绘制SiLU和Mish的图像3
plt.plot(x, y_silu, label='SiLU')
plt.plot(x, y_mish, label='Mish')

# 设置图例和标签
plt.legend()
plt.xlabel('x')
plt.ylabel('Activation')
plt.title('SiLU vs. Mish Activation Function')

# 显示图像
plt.show()
