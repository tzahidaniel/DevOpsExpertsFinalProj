import pymysql
import uuid

db_name = 'freedb_devops'
conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_lalala', passwd='P!?k!gbS*5QXnU8',
                       db=db_name)
conn.autocommit(True)
cursor = conn.cursor()


def get_user(user_id=None, username=None):
    if user_id:
        cursor.execute(f"SELECT * FROM {db_name}.project WHERE id = '{user_id}'")
    if username:
        cursor.execute(f"SELECT * FROM {db_name}.project WHERE name = '{username}'")
    user = cursor.fetchone()

    return user


def add_user(username):
    user_id = uuid.uuid4()
    cursor.execute(f"INSERT into {db_name}.project (name, id) VALUES ('{username}', '{user_id}')")
    print(f'user:{username} has been saved to DB')
    return (get_user(user_id),user_id)


def update_user(user_id, username):
    cursor.execute(f"UPDATE {db_name}.project SET name = '{username}' WHERE id = '{user_id}'")


def delete_user(user_id=None, username=None):
    value = 0
    if user_id:
        if get_user(user_id=user_id):
            value = cursor.execute(f"DELETE FROM {db_name}.project WHERE id = '{user_id}' ;")
    elif username:
        if get_user(username=username):
            value = cursor.execute(f"DELETE FROM {db_name}.project WHERE name = '{username}' ;")

    if value > 0:
        return True
    else:
        return False


def check_user_existence(user_id=None, user_name=None):
    exists = None

    if user_id:
        exists = get_user(user_id=user_id)
    elif user_name:
        exists = get_user(username=user_name)

    return exists is not None


# if __name__ == '__main__':
#     delete_user('346e799a-9be8-4043-8c87-6ec58627b516')
