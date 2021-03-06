# -*- coding: utf-8 -*-

import requests
import os
from flask import Flask, request, Response
from kobis_api import movie_actor_search

API_KEY = 'TELEGRAM_API_KEY'

app = Flask(__name__)


def parse_message(message):
    """
    telegram 에서 data 인자를 받아옴
    data 내부 구조를 이해해야 한다.
    
    Retuen :    
    chat_id = 사용자 아이디 코드
    msg = 사용자 대화 내용    
    """
    chat_id = message['message']['chat']['id']
    msg = message['message']['text']
    
    return chat_id, msg


def send_message(chat_id, msg):
    """
    chat_id : 사용자 아이디 코드
    text : 사용자 대화내용

    Return :
    함수에 변수를 할당할때 text='hello' 라고 선언
    --> text에 관련된 값이 전달되지 않으면 hello를 default로 사용
    
    사용자에게 메세지를 보내는 내용의 함수   
    """
    url = 'https://api.telegram.org/bot{token}/sendMessage'.format(token=API_KEY)

    if msg[:3] == '무비봇':
        try:
            movie_name, top5_actor = movie_actor_search(msg[3:])
            msg = "너가 찾은 영화 [{movie_Nm}]의 메인배우 5명은 {actor_name}이야!". \
                format(movie_Nm=movie_name, actor_name=', '.join(top5_actor))
        except ValueError:
            msg = movie_actor_search(msg[3:])


    # 변수들을 딕셔너리 형식으로 묶음
    # 사용자에게 보내는 text는 사용자가 보낸 text와 똑같다
    # 똑같은 소리를 한다고 해서 Echo_bot
    params = {'chat_id': chat_id, 'text': msg}
    
    # Url 에 params 를 json 형식으로 변환하여 전송
    # 메세지를 전송하는 부분
    response = requests.post(url, json=params)
    print(response)
    return response


# 경로 설정, URL 설정
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        message = request.get_json()
                
        # parse_message 함수는 두가지 return 값을 가진다 (chat_id, msg)
        # 순서대로 chat_id, msg의 변수로 받아준다.
        chat_id, msg = parse_message(message)
        
        # send_message 함수에 두가지 변수를 전달
        send_message(chat_id, msg)
        
        # 여기까지 오류가 없으면 서버상태 200 으로 반응
        return Response('ok', status=200)
    else:
        return 'Hello World!'


@app.route('/about')
def about():
    return 'About page'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

