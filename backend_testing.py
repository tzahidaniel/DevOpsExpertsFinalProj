import requests
import pymysql

schema_name = "freedb_devops"
conn = pymysql.connect(
    host='sql.freedb.tech',
    port=3306,
    user='freedb_lalala',
    passwd='P!?k!gbS*5QXnU8',
    db=schema_name
)

conn.autocommit(True)
cursor = conn.cursor()


def test_add_user():
    try:
        response = requests.post('http://127.0.0.1:5000/users', json={'user_name': "john"})
        if response.status_code == 200 or response.status_code == 201:
            print(response.json())
        else:
            print({'error': response.reason})
    except Exception as e:
        print(e)
    except requests.exceptions.RequestException as reqErr:
        print(reqErr)


if __name__ == '__main__':
    test_add_user()
