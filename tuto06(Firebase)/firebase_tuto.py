# Firebase SDK Document : https://firebase.google.com/docs/admin/setup?hl=ko

from firebase_admin import db, credentials
import firebase_admin

DB_URL = 'https://online-telegram-tuto.firebaseio.com/'

cred = credentials.Certificate('key/firebase_key.json')
firebase_admin.initialize_app(cred, {'databaseURL': DB_URL})
ref = db.reference('server/saving-data/')


def db_set_example():
    user_ref = ref.child('example_user')
    user_ref.set({
        '홍길동': {
            '생년월일': '2019-01-01',
            '나이': 10
        },
        '전우치': {
            '생년월일': '1919-01-01',
            '나이': 10
        },
        '도깨비': {
            '생년월일': '???',
            '나이': '???'
        },
        '홍두깨': {
            '생년월일': '???',
            '나이': '???'
        }
    })


def db_user_set(user_id, name, msg):
    """
    최초에 들어온 사용자에게는 set을 통해서 DB에 저장
    이후 사용자가 보낸 메세지는 update 를 통해서 DB 수정
    """
    user_ref = ref.child('user/{child}'.format(child=user_id))
    user_info = user_ref.get()
    try:
        if len(user_info):
            #  user_id 가 DB안에 존재하면
            user_prev_msg = user_info['prev_msg']
            user_ref.update({
                'prev_msg': msg
            })
        else:
            # 신규 사용자면
            user_prev_msg = None
            user_ref.set({
                    'user_name': name,
                    'prev_msg': ""
            })
    except TypeError:
        # user DB가 처음 호출될 때
        user_prev_msg = None
        user_ref.set({
                'user_name': name,
                'prev_msg': msg
        })

    return user_prev_msg


if __name__ == '__main__':
    # db_set_example()
    test_ref = ref.child('example_user')
    print(test_ref.get())
    print(test_ref.order_by_key().equal_to('홍길동').get())
    print(test_ref.order_by_key().start_at('홍').get())

