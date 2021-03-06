#网易云音乐抓取评论，需要先定位到iframe再抓取评论，
#而且页面评论翻页后iframe不变，所以switch_to_frame只要运行一次，
#while np可以替换成while True，跳出条件是下一页不可点击
#使用了两种点击下一页的方法，直接点击经常无效，需要在输入一个回车键。或者用js代码点击  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


dr=webdriver.Firefox()
u='http://music.163.com/#/song?id=30953009'
dr.get(u)
cant=set()      #用来保存无法打印的评论
np=1            #初始值，没实际作用

iframe=WebDriverWait(dr,30).until(EC.presence_of_element_located((By.TAG_NAME,'iframe')))
dr.switch_to_frame(iframe)

while np:
    np=WebDriverWait(dr,13).until(EC.visibility_of_element_located((By.LINK_TEXT,'下一页')))
    dd=np.get_attribute('id')

    S=dr.find_elements_by_class_name('cntwrap')
    for i in S:
        try:
            print(i.text)
        except UnicodeEncodeError:
            cant.add(i.text)

    if 'js-disabled' in np.get_attribute('class'):
        break
        
    #两种点击下一页的方法，直接点击经常无效，需要在输入一个回车键。或者用js代码点击    
    #ss='document.getElementById("{}").click();'.format(dd)
    #dr.execute_script(ss)
    np.click()
    np.send_keys(Keys.ENTER)



