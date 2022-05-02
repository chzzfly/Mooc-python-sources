#BatchInstall.py
from ast import Try
import os

libs = {'numpy', 'matplot', 'pillow', 'sklearn', 'requests', 'jieba'}

try:
    for lib in libs:
        os.system('pip install ' + lib)
    print('成功！')
except:
    print('安装失败！')