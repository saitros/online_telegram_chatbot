# 한국인공지능아카데미 & SBA 아카데미 온라인 챗봇 교육자료

Telegram Chatbot Tutorial with Python Flask

## 시작하기

교육영상 : 동영상 URL 을 참고하시면 됩니다.

### 파이썬 패키지 명세

[requirements](tuto00(Heroku)/requirements.txt)

### 설치
Heroku CLI(Command Line Interface) 설치 [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

 만약 Git이 설치 되어있지 않다면 [Install Git](https://git-scm.com/downloads)


## Ngrok 을 통한 간단한 테스트

[Ngrok 다운](https://ngrok.com/download)

Ngrok 실행화면 
 
```
ngrok http 5000 --region ap 
```
![Untitled](https://user-images.githubusercontent.com/16240290/67308446-14a5e900-f535-11e9-888d-8c660dadf411.png)
![Untitled1](https://user-images.githubusercontent.com/16240290/67308449-15d71600-f535-11e9-8d4b-c1a375c731f9.png)


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

배포과정에서는 
[![Deploy my app to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
