from flask import Flask, render_template
from db import UserManager
from datetime import date, datetime

app = Flask(__name__)
db_user = UserManager()


@app.route('/index', methods=['GET'])
def index_page():
    db_user.add_visits({'time': datetime.now().time(), 'date': date.today()})
    return render_template('index.html',)


if __name__ == '__main__':
    app.run(debug=True)
