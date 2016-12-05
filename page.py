#coding: UTF-8
__author__ = 'xibolangren'
__website__ = 'western-ranger.com'
__total__ = 2 #最多抓取页数
import urllib
import urllib2
import thread
import lxml.html
import pdb#调试模块
import os

#糗事百科用户头像爬虫
class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2725.0 Safari/537.36'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #存放头像的变量，每一个元素是每一页段子手的头像
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
    #传入某一页的页码 获得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(url,headers = self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode

        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败,错误原因",e.reason
                return None


    #传入某一页页码，返回本页 图片 src list
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)#获取整个页面html代码
        if not pageCode:
            print "页面加载失败...."
            return None

        tree = lxml.html.fromstring(pageCode)#使用lxml处理html数据
        _items = tree.cssselect('div.author>a>img')
        items = []#存放img src
        for x in _items:
            items.append(x.attrib.get('src'))

        return items

    #加载并提取页面的内容，加入到列表中
    def loadPage(self):
        #如果当前未看的页数少于2页，则加载新一页
        if self.pageIndex == __total__ + 1:
            print u"不要贪心哦，你限制了最多爬取",__total__,"页"
            self.enable = False
            return True
        if self.enable == True:
            #获取新一页
            pageStories = self.getPageItems(self.pageIndex)
            for x in pageStories:
                self.saveImg(x,'./img/'+str(self.pageIndex)+'&&'+x[-10:-5]+'PAGE'+str(self.pageIndex)+'.png')
            #将该页的用户 头像 url 存放到全局list中
            if pageStories:
                self.stories.append(pageStories)
                print u"python爬虫，当前第",self.pageIndex,"页，作者",__author__,"个人博客",__website__
                #获取完之后页码索引加一，表示下次读取下一页
                self.pageIndex += 1

    # 保存图片
    def saveImg(self,imageURL,fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        f.close()

    # 创建目录
    def mkdir(self,path):
        path = path.strip()
        # 判断路径是否存在
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建
            return False

    #调用该方法，每次敲回车打印输出一个段子手头像
    def getOneStory(self,page):
        arr = range(__total__)
        #遍历一页的 段子手头像
        for x in arr:
            #等待用户输入
            input = raw_input()
            #每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            #如果输入Q则程序结束
            if input == "Q":
                self.enable = False
                return

    #开始方法
    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        #使变量为True，程序可以正常运行
        self.enable = True
        # 创建img文件已存放图片
        self.mkdir('./img')
        #先加载一页内容
        self.loadPage()
        #局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                #当前读到的页数加一
                nowPage += 1
                del self.stories[0]
                #保存该页的段子手头像
                self.getOneStory(nowPage)


spider = QSBK()
spider.start()
