#coding:utf-8
import urllib

class SV:
    # 保存图片
    def saveImg(self,imageURL,fileName):
        # print(imageURL,fileName)
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        f.close()

save = SV()
url = "http://pic.qiushibaike.com/system/avtnew/781/7818766/medium/2016120304115440.JPEG"
save.saveImg(url,'./img/gaoyuanyuan.png')
