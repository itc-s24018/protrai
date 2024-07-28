#s24018
#Flaskの練習

from flask import Flask

#Flaskライブラリをインスタンス化し app 変数に割り当てる
# コントラクタの引数は実行中のモジュールを指定
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

if __name__ == '__main__':
    app.run(debug = True)
