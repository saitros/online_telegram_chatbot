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

Ngrok ����ȭ�� [Ngrok �ٿ�](https://ngrok.com/download)
 
```
ngrok http 5000 --region ap 
```
<div>
<img width="200" src="https://user-images.githubusercontent.com/16240290/67308446-14a5e900-f535-11e9-888d-8c660dadf411.png">
<img width="200" src="https://user-images.githubusercontent.com/16240290/67308449-15d71600-f535-11e9-8d4b-c1a375c731f9.png">
</div>


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


[![Deploy my app to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Built With

* [Telegram](https://telegram.org) - Message Platform
* [Flask](https://github.com/pallets/flask) - The web framework used
* [Heroku](https://dashboard.heroku.com/apps) - Deploy Management
* [ngrok](https://ngrok.com/) - Deploy Test

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **LeeJunho** - *Initial work* - [Panic](https://github.com/saitros)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
