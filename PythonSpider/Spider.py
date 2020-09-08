# coding:utf-8
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

'''
爬取智联招聘 招聘信息
'''

def getJsonData(keyword, page, city):

    url = "https://fe-api.zhaopin.com/c/i/sou"
    params = {
        'start': f'{(page - 1) * 90}',
        'pageSize': '90',
        'cityId': f'{(530 + city)}',
        'salary': '0,0',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        'kw': f'{keyword}',
        'kt': '3',
        '_v': '0.02270441',
        'x-zp-page-request-id': 'a9819f27e6be4eeb867e2e61a068255c-1573447961742-743855',
        'x-zp-client-id': '06a1d1b2-c25b-4359-c5eb-42dd0ba470f3',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.json()
    except:
        print("请求超时！")

def parseJsonData(jsonData):
    data = []
    for dat in jsonData['data']['results']:
        # data.append({"职位名称" : dat['jobName'], "公司名称" : dat['company']['name'], "工作地点" : dat['city']['items'][0]['name'], "发布日期" : dat['updateDate'],
        #       "薪资水平" : dat['salary']})
        data.append([dat['jobName'], dat['company']['name'], dat['city']['items'][0]['name'], str(datetime.strptime(dat['updateDate'], "%Y-%m-%d %H:%M:%S").date()), dat['salary']])
    return data

def saveData(data):
    file = open('111.txt','a',encoding='UTF-8')
    for link in data:
        for s in link:
            file.write(s + ",")

        file.write("\n")

    file.close()

if __name__ == '__main__':
    keyword = input("请输入查询的职位:")

    city = 0
    # for city in range(0, 300):
    while True:
        print("城市id:" + str(530 + city))
        # print(parseJsonData(getJsonData(keyword, page, city)))
        page = 1
        error = 0

        while True:
            if error <= 3:
                try:
                    result = getJsonData(keyword, page, city)
                    # print(parseJsonData(getJsonData(keyword, page, city)))
                    if result['data']['results'] == []:
                        print("当前城市招聘信息采集结束!")
                        break
                    else:
                        print("正在爬取第" + str(page) + "页信息")
                        data = parseJsonData(result)
                        saveData(data)
                        time.sleep(5)
                        page += 1

                except:
                    print("Error!")
                    error += 1
            else:
                break

        city += 1

