from flask import Flask, render_template, request
import sql_api

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return  render_template('index.html')


@app.route('/test/', methods=['GET', 'POST'])
def test():
    a = request.form.get('keyyy')
    sql_api.add(a, a)

    return '我是后端，haha'


if __name__ == '__main__':
    app.run(debug=True)
