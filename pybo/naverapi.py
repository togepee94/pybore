# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import json
import urllib.request


def naverbook(bookname):
    client_id = "RY3aG6FDuv4yWzq3XW3g"
    client_secret = "tO1rR6ci85"
    encText = urllib.parse.quote(bookname)
    url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
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


def naverbook(bookname):
    client_id = "RY3aG6FDuv4yWzq3XW3g"
    client_secret = "tO1rR6ci85"
    encText = urllib.parse.quote(bookname)
    url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
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

#jsonstring = '''
#"date":"2021-05-11" , "data":[{"price":300 , "total":20},{"price":100 , "total":120}
#,{"price":1200 , "total":52}]}
#'''

#jdata = json.loads(jsonstring)

#print(jdata)

#result = jdata['data']
#print(result)

#total=0
#for temp in result:
#    print(temp)
#    total = total + (temp['price'] * temp['total'])
#print(total)

