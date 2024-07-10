# 空の辞書を作成
半蔵門線ナンバリング = {}

# 駅名とナンバリングを辞書に追加
半蔵門線ナンバリング["渋谷"] = "Z01"
半蔵門線ナンバリング["表参道"] = "Z02"
半蔵門線ナンバリング["青山一丁目"] = "Z03"
半蔵門線ナンバリング["永田町"] = "Z04"
半蔵門線ナンバリング["半蔵門"] = "Z05"
半蔵門線ナンバリング["九段下"] = "Z06"  
半蔵門線ナンバリング["神保町"] = "Z07"
半蔵門線ナンバリング["大手町"] = "Z08"
半蔵門線ナンバリング["三越前"] = "Z09"
半蔵門線ナンバリング["水天宮前"] = "Z10"
半蔵門線ナンバリング["清澄白河"] = "Z11"
半蔵門線ナンバリング["住吉"] = "Z12"
半蔵門線ナンバリング["錦糸町"] = "Z13"
半蔵門線ナンバリング["押上"] = "Z14"
#POINT
#辞書[任意のキー] = 値 の式で、辞書に新しい辞書データ「任意のキー；値」を追加する事ができる。

print(半蔵門線ナンバリング)

#キーのリストを作り、for文で一気に辞書を作成しよう。
半蔵門線駅リスト = [
    "渋谷","表参道","青山一丁目","永田町","半蔵門","九段下","神保町","大手町","三越前","水天宮前","清澄白河","住吉","錦糸町","押上",
]

ナンバリングリスト = ["Z01","Z02","Z03","Z04","Z05","Z06","Z07","Z08","Z09","Z10","Z11","Z12","Z13","Z14",
]

for 各駅, ナンバリング in zip(半蔵門線駅リスト,ナンバリングリスト):
    半蔵門線ナンバリング[各駅] = ナンバリング

print(半蔵門線ナンバリング)


