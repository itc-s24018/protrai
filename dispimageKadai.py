#s24018
#dispImage.pyをアレンジして機能を追加
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        Label = tk.Label(text=fpath,font=("Helvetica",15))
        Label.pack(side='bottom', padx=20, pady=20)
        
root = tk.Tk()
root.title("画像表示アプリバージョン2.0")
root.geometry("600x500")

lbl = tk.Label(text="画像表示アプリバージョン2.0",font=("Helvetica",20))

btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()


lbl.pack()
btn.pack()
imageLabel.pack()

tk.mainloop()

