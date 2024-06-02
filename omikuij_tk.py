#s24018
#おみくじプログラムをGUIで
import tkinter as tk
import random

def get_fortune():
    # くじのリスト
    kuji = ["大吉", "中吉", "小吉", "凶"]
    # ラベルにくじの結果を表示
    result_label.config(text=random.choice(kuji))

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("おみくじ")

# ラベルの作成
result_label = tk.Label(root, text="")
result_label.pack()

# おみくじボタンの作成
fortune_button = tk.Button(root, text="おみくじを引く", command=get_fortune)
fortune_button.pack()

# イベントループの開始
root.mainloop()


