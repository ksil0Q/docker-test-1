from flask import Flask, render_template
from db import UserManager
from datetime import date, datetime

app = Flask(__name__)
db_user = UserManager()


@app.route('/')
@app.route('/index', methods=['GET'])
def index_page():
    db_user.add_visits({'time': datetime.now().time(), 'date': date.today()})
    count = db_user.get_count_visits()
    return render_template('index.html', count=count)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
