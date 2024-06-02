#GUIで動くアプリを作ってみるよ

import tkinter as tk #まずこの行を書く必要があるよ

root= tk.Tk() #初めのおまじない

root.geometry("1200x2400") #windowのサイズを決める
root.title("ハローアプリ") #windowのタイトルを決める
ldl=tk.Label(text="こんにちは世界") #いつもの
ldl.pack() #ldlを配置させる必要があるよ




root.mainloop() #終わりのおまじない
