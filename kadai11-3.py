import re

#半径は0以上の整数
while True:
    s = input("はんけいはー？")
    if re.fullmatch(r'[1-9][0-9]*|0', s):
        break
    print("しねよ")

r = int(s)
print("円の面積は",r*r*3.14159264)

#r''の形式
## 通常の文字列では、バックスラッシュはエスケープシーケンスとして解釈される
#s = "C:\\Users\\John\\Documents"
##  生文字列では、バックスラッシュはそのまま文字列の一部として扱われる
#s = r"C:\Users\John\Documents"
#\d+: 1つ以上の数字。

