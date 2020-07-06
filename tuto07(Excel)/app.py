# -*- coding: utf-8 -*-

import requests
import os
from flask import Flask, request, Response
from openpyxl_tuto import db_user_set

API_KEY = 'API_KEY'

app = Flask(__name__)


def parse_message(message):
    """
    telegram 에서 data 인자를 받아옴
    data 내부 구조를 이해해야 한다.

    Retuen :
    chat_id = 사용자 아이디 코드
    msg = 사용자 대화 내용
    """
    chat_id = message['message']['from']['id']
    msg = message['message']['text']
    name = message['message']['from']['last_name'] + message['message']['from']['first_name']

    return chat_id, msg, name


def send_message(chat_id, text='bla-bla-bla'):
    """
    Chat-id 와 text를 변수로 받아 메세지를 보내주는데
    params 안에 키보드를 설정해서 같이 보내주는 방법

    https://core.telegram.org/bots/api#keyboardbutton
    """
    # sendMessage URL
    url = 'https://api.telegram.org/bot{token}/sendMessage'.format(token=API_KEY)
    keyboard = {  # Keyboard 형식
        'keyboard': [[{
            'text': '버튼1'
        },
            {'text': '버튼2'
             }],
            [{'text': '버튼3'},
             {'text': '버튼4'}]
        ],
        'one_time_keyboard': True
    }

    if text == '버튼1':  # 사용자가 button_1 이라고 응답하면 ~
        keyboard = {
            'keyboard': [[{'text': '조금 전에 버튼1을 누르셨습니다.'}]],
            'one_time_keyboard': True
        }
        params = {'chat_id': chat_id, 'text': text, 'reply_markup': keyboard}
        requests.post(url, json=params)
        return 0

        # 변수들을 딕셔너리 형식으로 묶음
    params = {'chat_id': chat_id, 'text': text, 'reply_markup': keyboard}

    # Url 에 params 를 json 형식으로 변환하여 전송
    # 메세지를 전송하는 부분
    requests.post(url, json=params)

    return 0


# 경로 설정, URL 설정
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        message = request.get_json()

        # parse_message 함수는 두가지 return 값을 가진다 (chat_id, msg)
        # 순서대로 chat_id, msg의 변수로 받아준다.
        chat_id, msg, name = parse_message(message)

        msg = db_user_set(chat_id, name, msg)
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

