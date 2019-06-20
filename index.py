from flask import Flask, render_template, request
import json
import sql_api

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    arr = []
    num = arr[9]
    return  render_template('index.html')


# 1.add
@app.route('/add/', methods=['GET', 'POST'])
def add():
    a = request.form.get('keyyy')
    # 测试一下a是不是空滴
    if not a:
        return 'fail'
    sql_api.add(a, a)
    return 'ok'


# 2.delete
@app.route('/delete/', methods=['GET', 'POST'])
def delete():
    the_id = request.form.get('id')
    sql_api.delete(the_id)
    return 'ok'


# 3.search-something
@app.route('/search-something/', methods=['GET', 'POST'])
def search_something():
    keyword = request.form.get('keyword')
    lines = sql_api.seach(keyword)
    return json.dumps(lines)


# 4.show-table
@app.route('/all-lines/', methods=['GET', 'POST'])
def all_lines():
    lines = sql_api.all_lines()
    return json.dumps(lines)


if __name__ == '__main__':
    app.run(debug=True)
