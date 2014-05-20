# -*- coding: utf-8 -*-

import urllib2, string                                       

#导入所需要的模块

def spider(s, e, url):
	for i in range(s, e + 1):
		file_name = string.zfill(i, 5) + '.html'
		print u"蜘蛛正在下载 %s ......." % file_name
		with open(road + file_name, 'w+') as f:
			html = urllib2.urlopen(url + str(i))
			f.write(html.read())
#定义爬取函数

url = raw_input(u'请输入要爬虫的贴吧网址(去掉网址内pn后面的数字):')
start = raw_input(u'请输入要爬虫的起始页数')
end = raw_input(u'请输入要爬虫的终止页数')
road = r'F:\\recover\\2014.3-2014.6\\python pachong\\download data\\'
start_page = int(start)
end_page = int(end)

spider(start_page, end_page, url)
