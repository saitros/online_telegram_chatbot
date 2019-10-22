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


```
heroku login 
cd tuto00(Heroku)
git init
git add .
heroku git:remote -a [Heroku �� �̸�]
git add .
git commit -m "[�ڸ�Ʈ]"
heroku buildpacks:set heroku/python
git push heroku master
heroku ps:scale web=1
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

