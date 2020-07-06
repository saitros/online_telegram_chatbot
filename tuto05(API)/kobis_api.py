# -*- coding: utf-8 -*-
"""
@author: Junho
"""

import requests
import json

# 발급 받은 API_KEY
# 해당 정보를 가지고 오는 End-point URL
API_KEY = "KOBIS_API_KEY"
code_search_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
movie_info_search_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json"


def movie_code_search(movie_name):
    """
    movie_code_search는 영화 제목을 인자로 받아서 
    영화 코드를 찾아주는 API를 통해 영화 코드를 리턴
    
    Input : Movie_name
    Return : Movie_code
    """
    
    params = {"key" : API_KEY, "movieNm": movie_name}
    # requests 를 이용해서 end-point에 요구하는 방식대로 param을 전달
    # 받아온 data를 response 에 할당
    response = requests.get(code_search_url, params)
    # json 데이터 형식은 json 라이브러리를 통해서 Dict 형식으로 불러옴
    movie_info = json.loads(response.text)
    try:
        # movie_info 에서 내가 원하는 movie_code만 빼오기
        return movie_info["movieListResult"]["movieList"][0]["movieCd"]

    except:
        return "Error"


# 다른 API를 통해서 영화 코드를 던져주고 영화 정보 리턴
def movie_actor_search(movie_name):
    movie_code = movie_code_search(movie_name)
    if movie_code == "Error":
        return "잘못된 영화 제목입니다. 다시한번 확인해주세요"
    params = {"key": API_KEY, "movieCd": movie_code}
    response = requests.get(movie_info_search_url, params)
    movie_info = json.loads(response.text)
    actor_list = movie_info['movieInfoResult']['movieInfo']['actors']
    movie_name = movie_info['movieInfoResult']['movieInfo']['movieNm']
    top5_actor = [people_info['peopleNm'] for people_info in actor_list[:5]]
    return movie_name, top5_actor


if __name__ == "__main__":
    print(movie_actor_search('해리포터'))
