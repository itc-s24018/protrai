#app2.py バージョン２

import tkinter as tk#tkinterをインポートしてtkと略して使う

def dispLabel():
    lbl.config(text="こんにちは")


root = tk.Tk()
#画面を作る
root.geometry("500x500")
#画面の大きさを決める

lbl = tk.Label(text="LABEL",font=("Helvetica",50))#ラベルを作る
#ボタンを作る
btn = tk.Button(text="PUSH",command=dispLabel,font=("Helvetica",50))

lbl.pack()                  #画面にラベルを配置する
btn.pack()                  #画面にボタンを配置する

lbl2 = tk.Label(text="ラベル２",font=("Helvetica",50)).pack()
btn2 = tk.Button(text="何もしないボタン",command=dispLabel,font=("Helvetica",50)).pack()


tk.mainloop()               #作ったウィンドウを表示する
