# �ѱ��ΰ����ɾ�ī���� & SBA ��ī���� �¶��� ê�� �����ڷ�

Telegram Chatbot Tutorial with Python Flask

## �����ϱ�

�������� : ������ URL �� �����Ͻø� �˴ϴ�.

### ���̽� ��Ű�� ��

[requirements](tuto00(Heroku)/requirements.txt)

### ��ġ
Heroku CLI(Command Line Interface) ��ġ [Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

 ���� Git�� ��ġ �Ǿ����� �ʴٸ� [Install Git](https://git-scm.com/downloads)


## Ngrok �� ���� ������ �׽�Ʈ

[Ngrok �ٿ�](https://ngrok.com/download)

Ngrok ����ȭ�� 
 
```
ngrok http 5000 --region ap 
```
![Untitled](https://user-images.githubusercontent.com/16240290/67308446-14a5e900-f535-11e9-888d-8c660dadf411.png)
![Untitled1](https://user-images.githubusercontent.com/16240290/67308449-15d71600-f535-11e9-8d4b-c1a375c731f9.png)


### Ngrok �� �̿��� �׽�Ʈ 


tuto01 �� �ִ� telegram.py �� ����
```
API_KEY = Telegram Bot ACCESS Key
WEBHOOK URL = Ngrok forwarding HTTPS URL
```

������ ���� tuto02~05�� �ִ� app.py ����
```
python app.py
```

app.py ���� �α�

```
 Running on http://127.0.0.1:5000/
```

## ����

�������������� 
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
