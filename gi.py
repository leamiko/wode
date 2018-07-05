from scrapy import Spider, Request, FormRequest


class GithubLoginSpider(Spider):
    name = "gi"
    # post登入的必须要的头字段
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
    }
    #https://passport.suning.com/ids/login
    #https://order.suning.com/order/orderList.do

    def start_requests(self):
        return [Request("https://xueqiu.com/",
                        meta = {'cookiejar' : 11},
                         headers=self.h,
                        callback = self.post_login)]  #添加了meta

    #FormRequeset出问题了
    def post_login(self, response):
        print('登录'*8,response.text)
        return Request('https://xueqiu.com/stock/f10/finmainindex.json?symbol=SZ000001&page=1&size=1',
                       callback=self.pa,
                       headers=self.h,
                       meta={'cookiejar': response.meta['cookiejar']},
                       dont_filter=True
                       )
    def pa(self, response):
        print(response.text)
        #'''
        with open('1.txt', 'w',encoding='utf8')as f:
            f.write(response.text)
        #'''
