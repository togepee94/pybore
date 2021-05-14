import os
from bs4 import BeautifulSoup
import requests

def Mrank():
    page = requests.get("https://movie.naver.com/movie/running/current.nhn")
    html = page.text
    soup = BeautifulSoup(html,'lxml')
    result = soup.find_all('dl','lst_dsc')
    #print(title_result)

    moviedata = []

    for temp in result:
        mdata = {}
        #제목
        tdata = temp.find('dt','tit')
        tdata = tdata.find('a').text
        mdata['title'] =tdata
        #평점
        star = temp.find('div', 'star_t1')
        star = star.find('span','num').text
        mdata['star'] = star
        #장르
        genre = temp.find('dl','info_txt1')
        genre = genre.find('span','link_txt').text
        genre = genre.replace('\n','')
        genre = genre.replace('\r', '')
        genre = genre.replace('\t', '')
        mdata['genre'] = genre

        moviedata.append(mdata)
        #출연
        #cast = temp.find('dt', 'tit_t3')
        #cast = cast.find('span','link_txt')
        #print(cast)
        #print('=========================')

    imgresult = soup.find_all('div','thumb')
    imgurl = []
    for temp in imgresult:
        url = temp.find('img')
        imgurl.append(url['src'])


    i=0
    for temp in moviedata:
        temp['img'] = imgurl[i]
        i+=1
        #print(temp)

    return moviedata

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import json
import urllib.request




def navermovie(moviename):
    client_id = "RY3aG6FDuv4yWzq3XW3g"
    client_secret = "tO1rR6ci85"
    encText = urllib.parse.quote(moviename)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        jsontemp = json.loads(response_body.decode('utf-8'))


        #for temp in jsontemp['items']:
            #print(temp['author'])

    else:
        print("Error Code:" + rescode)


    return jsontemp


