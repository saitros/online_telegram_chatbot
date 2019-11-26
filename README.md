# 한국인공지능아카데미 & SBA 아카데미 온라인 챗봇 교육자료

Telegram Chatbot Tutorial with Python Flask

## 시작하기

교육영상 : 동영상 URL 을 참고하시면 됩니다.

Google Firebase Document : https://firebase.google.com/docs/reference/admin/python



### 파이썬 패키지 명세

[requirements](tuto00(Heroku)/requirements.txt)

### 설치
Heroku CLI(Command Line Interface) 설치 [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

 만약 Git이 설치 되어있지 않다면 [Install Git](https://git-scm.com/downloads)


## Ngrok 을 통한 간단한 테스트

Ngrok 실행화면 [Ngrok 다운](https://ngrok.com/download)
 
```
ngrok http 5000 --region ap 
```
<div>
<img width="200" src="https://user-images.githubusercontent.com/16240290/67308446-14a5e900-f535-11e9-888d-8c660dadf411.png">
<img width="200" src="https://user-images.githubusercontent.com/16240290/67308449-15d71600-f535-11e9-8d4b-c1a375c731f9.png">
</div>


### Ngrok 을 이용한 테스트 


tuto01 에 있는 telegram.py 를 수정
```
API_KEY = Telegram Bot ACCESS Key
WEBHOOK URL = Ngrok forwarding HTTPS URL
```

실행할 파일 tuto02~05에 있는 app.py 실행
```
python app.py
```

app.py 실행 로그

```
 Running on http://127.0.0.1:5000/
```

## 배포

[![Deploy my app to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Heroku CLI에서 사용 [ 내용은 해당 내용을  ] 

```
>> heroku login 
>> cd tuto00(Heroku)
>> git init
>> git add .
>> heroku git:remote -a [Heroku 저장소 이름]
>> git add .
>> git commit -m "[코맨트]"
>> heroku buildpacks:set heroku/python
>> git push heroku master
>> heroku ps:scale web=1
```

## Built With

* [Telegram](https://telegram.org) - Message Platform
* [Flask](https://github.com/pallets/flask) - The web framework used
* [Heroku](https://dashboard.heroku.com/apps) - Deploy Management
* [ngrok](https://ngrok.com/) - Deploy Test


## Authors

* **LeeJunho** - *Initial work* - [Panic](https://github.com/saitros)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

