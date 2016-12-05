# -*- coding:utf-8 -*-
import pdb
import os

class MK:
    def __init__(self):
        return None

    # 创建目录
    def mkdir(self,path):
        pdb.set_trace()
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists=os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

make = MK()
make.mkdir('./img')
