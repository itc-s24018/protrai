#s24018
#GUIで現在時刻を表示するモジュール

import datetime
import tkinter as tk　#このモジュールをGUIで表示できる　[tkinter,tk]

#時間を処理する2行を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    
    lbl.config(text=current_time)
    root.after(1000, update_time)　#自分をもう一度呼び出す

# Tkinterの画面(ウィンドウ)を表示
root = tk.Tk() #始まり

root.title("現在の時刻")
#ウィンドウ内にいろいろな要素(文字の大きさなど)を追加する [tk.Label]
#tk.Labelを変数lblに入れて見やすくしている
lbl = tk.Label()
lbl.config(text="",font=("Helvetica",50))
lbl.pack()

#作った関数を呼び出す
update_time()

root.mainloop()
