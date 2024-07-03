#s24018
#dispImageKadai.pyに機能を追加
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    originalImage = PIL.Image.open(path)
    
   
    grayscaleImage = originalImage.convert("L")
    #９０度回転
    rotatedImage = grayscaleImage.rotate(90)
    
    # 水平反転
    flippedImage = rotatedImage.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    
    # リサイズ
    resizedImage = flippedImage.resize((300, 300))
    
    # ImageオブジェクトをPhotoImageオブジェクトに変換
    imageData = PIL.ImageTk.PhotoImage(resizedImage)
    
    # 画像を表示するラベルを更新
    imageLabel.configure(image=imageData)
    imageLabel.image = imageData  # 参照を保持

def openFile():
    # ファイルダイアログを開く
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        filePathLabel.config(text=fpath)  # ファイルパスを更新

# Tkinterの初期化
root = tk.Tk()
root.title("画像表示アプリバージョン2.0")
root.geometry("600x500")

# ラベルやボタンを作成して配置
titleLabel = tk.Label(root, text="画像表示アプリバージョン2.0", font=("Helvetica", 20))
titleLabel.pack()

openButton = tk.Button(root, text="ファイルを開く", command=openFile)
openButton.pack()

imageLabel = tk.Label(root)
imageLabel.pack()

filePathLabel = tk.Label(root, text="", font=("Helvetica", 12))
filePathLabel.pack(padx=20, pady=10)

# Tkinterのメインループを開始
tk.mainloop()
