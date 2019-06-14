"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpResponse
from app import models
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def dianying(request):
    movie = []
    movie=models.movie.objects.all()
    return render(request,'app/douban250.html',{'movies':movie})

def pcdouban(request):
    '''
    movie_list = []
    moviedata_list = []
    for i in range(0,2):
        link = 'https://movie.douban.com/top250?start=' + str(i*25)
        r = requests.get(link,timeout=10)
        soup = BeautifulSoup(r.text,"lxml")
        div_list = soup.find_all('div',class_='hd')
        div_list2 = soup.find_all('div',class_='bd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
        for each in div_list2:
            moviedata = each.p.text.strip()
            moviedata_list.append(moviedata)
        moviedata_list.remove('豆瓣')
    for i in range(len(movie_list)):
        models.movie.objects.create(movie_name=movie_list[i],movie_data=moviedata_list[i])
    '''
    return render(request,'app/pachong.html',{'a':'豆瓣爬取完毕！'})

def baidu(request):
    b=[]
    a=['华为','苹果','魅族','小米']
    driver = webdriver.Edge()
    url = "https://www.baidu.com/"
    driver.get(url)
    for i in range(len(a)):
        sousuo = driver.find_element_by_id("kw")
        sousuo.clear()
        sousuo.send_keys(a[i])
        driver.find_element_by_id("su").click()
        time.sleep(9)
        jg = driver.find_element_by_css_selector("div.nums")
        jg2 = jg.find_element_by_tag_name("span").text  
        b.append(jg2)
        driver.back()
    driver.quit()
    return render(request,'app/baidu.html',{'jieguo':b,'key':a})

def pcjdshouji(request):
    '''
    driver=webdriver.Edge()
    driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8')
    time.sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    b=[]
    d=[]
    a=driver.find_elements_by_xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')
    c=driver.find_elements_by_xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i')
    for i in range(len(a)):
        b.append(a[i].text)
    for i in range(len(c)):
        d.append(c[i].text) 
    driver.close()
    for i in range(len(b)):
        models.phone.objects.create(phone_name=b[i],phone_price=d[i])
        '''
    return render(request,'app/pachong.html',{'a':'京东手机爬取完毕！'})

def jdshouji(request):
    phone = []
    phone=models.phone.objects.all()
    return render(request,'app/JDshouji.html',{'phones':phone})

def tielu(request):
    driver=webdriver.Edge()
    driver.get('https://kyfw.12306.cn/otn/resources/login.html')
    time.sleep(3)
    driver.find_element_by_link_text("账号登录").click()
    #driver.find_element_by_id("J-userName").clear()
    driver.find_element_by_id("J-userName").send_keys("13758553671")
    #driver.find_element_by_id("J-password").clear()
    driver.find_element_by_id("J-password").send_keys("pd980625")
    time.sleep(7)
    driver.find_element_by_id("J-login").click()
    return render(request,'app/pachong.html',{'a':'登录成功！'})