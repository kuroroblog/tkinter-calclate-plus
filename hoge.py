import tkinter as tk
import ctypes
import re

# ボタンを選択した場合に、実行される関数
def calcAns():
    # entry Widget内へ入力された数字を取得する。
    tmpNumArea1 = numArea1.get()
    tmpNumArea2 = numArea2.get()

    # entry Widget内へ数字が入力されなかった場合は、計算しない。
    if not tmpNumArea1 == '' and not tmpNumArea2 == '':
        # label Widgetのtextを再設定(計算結果を書き換え)する。
        # text : テキスト情報
        ansLabel.configure(text=int(tmpNumArea1)+int(tmpNumArea2))

# 入力制限について : https://kuroro.blog/python/YaHEdMd4ScGvrU44zdT6/
def onValidate(S):
    # 入力された文字が半角数字の場合
    # reについて : https://note.nkmk.me/python-re-match-search-findall-etc/
    if re.match(re.compile('[0-9]+'), S):
        return True
    else:
        # 入力不正のブザーを鳴らす。
        root.bell()
        return False

# Windowを生成する。
# Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
root = tk.Tk()
# Windowへタイトルをつける。
root.title('pythonで足し算')
# Windowの画面サイズを設定する。
# geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
root.geometry('400x125')

# register : 入力制限を行うための関数の登録を行う。パラメータと関数を紐づけるために必要。
# 入力制限について : https://kuroro.blog/python/YaHEdMd4ScGvrU44zdT6/
vcmd = root.register(onValidate)

# Windowを親要素として、label Widgetを作成する。
# text : テキスト情報
# font : 文字の大きさや形式を変更する。
# fontについて : https://kuroro.blog/python/RZNjLl36upkumxwkTRWl/
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
plusLabel = tk.Label(master=root, text='+', font=100)
# Windowを親要素として、label Widgetをどのように配置するのか?
# placeについて : https://kuroro.blog/python/JyaHUKyFyxCa0baFfXg0/
plusLabel.place(x=141, y=20)

# Windowを親要素として、entry Widgetを作成する。
# width : 幅の設定
# font : 文字の大きさや形式を変更する。
# fontについて : https://kuroro.blog/python/RZNjLl36upkumxwkTRWl/
# validate : 入力制限するオプションの値を設定。
# validatecommand : 入力制限用関数の設定。
# 入力制限について : https://kuroro.blog/python/YaHEdMd4ScGvrU44zdT6/
# Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
numArea1 = tk.Entry(master=root, width=5, font=40, validate="key", validatecommand=(vcmd, '%S'))
# Windowを親要素として、entry Widgetをどのように配置するのか?
# placeについて : https://kuroro.blog/python/JyaHUKyFyxCa0baFfXg0/
numArea1.place(x=60, y=20)

# Windowを親要素として、entry Widgetを作成する。
# width : 幅の設定
# font : 文字の大きさや形式を変更する。
# fontについて : https://kuroro.blog/python/RZNjLl36upkumxwkTRWl/
# validate : 入力制限するオプションの値を設定。
# validatecommand : 入力制限用関数の設定。
# 入力制限について : https://kuroro.blog/python/YaHEdMd4ScGvrU44zdT6/
# Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
numArea2 = tk.Entry(master=root, width=5, font=40, validate="key", validatecommand=(vcmd, '%S'))
# Windowを親要素として、entry Widgetをどのように配置するのか?
# placeについて : https://kuroro.blog/python/JyaHUKyFyxCa0baFfXg0/
numArea2.place(x=180, y=20)

# Windowを親要素として、button Widgetを作成する。
# text : テキスト情報
# command : ボタンを選択した場合に、実行する関数を設定する。calcAnsとする。
# font : 文字の大きさや形式を変更する。
# fontについて : https://kuroro.blog/python/RZNjLl36upkumxwkTRWl/
# Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
ansBtn = tk.Button(master=root, text='足し算', command=calcAns, font=40)
# Windowを親要素として、button Widgetをどのように配置するのか?
# placeについて : https://kuroro.blog/python/JyaHUKyFyxCa0baFfXg0/
ansBtn.place(x=300, y=20)

# Windowを親要素として、label Widgetを作成する。
# width : 幅の設定
# font : 文字の大きさや形式を変更する。
# fontについて : https://kuroro.blog/python/RZNjLl36upkumxwkTRWl/
# background : 背景色を設定
# 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
# Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
ansLabel = tk.Label(master=root, width=5, font=40, background='green')
# Windowを親要素として、label Widgetをどのように配置するのか?
# placeについて : https://kuroro.blog/python/JyaHUKyFyxCa0baFfXg0/
ansLabel.place(x=60, y=80)

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

# Windowをループさせて、継続的にWindow表示させる。
# mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
root.mainloop()
