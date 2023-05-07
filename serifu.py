# ライブラリをインポート
import requests
import pandas as pd
from bs4 import BeautifulSoup

# スクレイピングの準備
load_url = "https://www.dokusyo-geek-ki.com/entry/manga_meigen"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# タグとクラス指定で漫画名、キャラ名、セリフを取ってくる
h4 = soup.find_all("h4")
blb = soup.find_all(class_="booklink-box")

lst = []

# 全角スペース削除、改行削除、漫画名とキャラ名の分割などの処理を行ってリストを作成
for i, j in zip(h4, blb):
    i, i_ = i.text.split("\u3000")
    i_ = i_.replace("「", "").replace("」", "")
    j = j.text.replace("\n", " ").replace("\u3000", " ")
    lst.append([i, i_, j])

# リストをデータフレームに変換
df = pd.DataFrame(lst, columns=['漫画', 'キャラ', 'セリフ'])

print(df)
df.to_csv('manga.csv', encoding="utf-8-sig")