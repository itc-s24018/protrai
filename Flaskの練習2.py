#s24018
#Flaskの練習
#こんにちは世界と書かれた文章を表示するプログラム

from flask import Flask, render_template

#Flaskライブラリをインスタンス化し app 変数に割り当てる
# コントラクタの引数は実行中のモジュールを指定
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=5000,debug=True)
