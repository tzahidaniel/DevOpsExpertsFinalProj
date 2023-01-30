import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import names

"""
The script will: 
1. Post any new user data to the REST API using POST method.
2. Submit a GET request to make sure data equals to the posted data.
3. Using pymysql, check posted data was stored inside DB (users table).
4. Start a Selenium Webdriver session.
4a. Navigate to web interface URL using the new user id.
4b. Check that the user name is correct.
!!! Any failure will throw an exception using the following code: raise Exception("test failed")
"""


def db_conn():
    schema_name = "freedb_devops"
    try:
        conn = pymysql.connect(
            host='sql.freedb.tech',
            port=3306,
            user='freedb_lalala',
            passwd='P!?k!gbS*5QXnU8',
            db=schema_name
        )
    except pymysql.err.OperationalError as operErr:
        print(operErr)
    finally:
        cursor = conn.cursor()
        return cursor, conn


# Post any new user data to the REST API using POST method.
def combined_testing(username):
    try:
        url = 'http://127.0.0.1:5000/users'
        body = {'user_name': username}
        response = requests.post(url, json=body)

    except requests.exceptions.ConnectionError as err:
        print("rest server is down\n", err)
    except Exception as e:
        print(e)
    finally:
        post_uuid = response.json()[0]['id']
        print(post_uuid)

    # Submit a GET request to make sure data equals to the posted data.

    get_req = requests.get(f"http://127.0.0.1:5000/users/{post_uuid}")
    get_req_uid = get_req.json()[0]['user_name'][0]
    print(get_req_uid)

    # check db
    cursor, conn = db_conn()
    exec_query = f"SELECT * FROM freedb_devops.project WHERE id = '{post_uuid}'"

    cursor.execute(exec_query)
    conn.commit()

    sql_uuid = cursor.fetchall()[0][0]
    print(sql_uuid)

    # selenium web testing
    driver = webdriver.Chrome(service=Service("chromedriver.exe"))
    driver.get(f"http://127.0.0.1:5001/users/get_user_data/{post_uuid}")
    selenium_username = driver.find_element(By.ID, value="user_name").text
    print('selenium user: ', selenium_username)

    # 1
    if post_uuid != get_req_uid:
        raise Exception('test 1 fail')
    else:
        print('test 1 - pass')

    # 2
    if post_uuid != sql_uuid:
        raise Exception('test 2 fail')
    else:
        print('test 2 - pass')

    # 3
    if selenium_username != username:
        raise Exception('test 3 fail')
    else:
        print('test 3 - pass')


def generate_user_name():
    username = names.get_first_name()
    return username


combined_testing(generate_user_name())
