from flask import Flask
from db_connector import get_user

app = Flask(__name__)


@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST'])
def get_user_name(user_id):
    user = get_user(user_id)
    if not user_id:
        return f"<H1 id='error'>\" no such user: ${user_id} \"</H1>", 500

    if user:
        return f"<H1><b>USERNAME: <span id='user_name'>{user[1]}</span></b></H1>", 200


app.run(host='127.0.0.1', debug=True, port=5001)
