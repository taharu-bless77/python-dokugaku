#リスト内内包表記
[a1,a2,a3,a4,a5,..an,..] = [expression for item in iterable if condition]

#expression: 新しいリストの"各要素"を生成する式'f(i)'
#item: 反復処理するための変数'i'
#iterable: 反復可能なオブジェクト（例: リスト、タプル、文字列）
#condition（省略可能）: フィルタリングのための条件

#公式
"[f(i) for i in ('リスト,文字列,ダブル') if 'フィルタリング処理']"

#例1 0~9までの数字のリストを作成,
# 0~9のうち奇数リストを作成
numbers = [i for i in range(10)]
kisuunumbers = [i for i in range(10) if i % 2 == 1]

#集合内包表記{a1,a2,a3,...}
  #公式はリスト内内包表記と全く同じなので省略

#辞書内包表記
数値 = [1, 2, 3, 4, 5]
二乗辞書 = {num: num ** 2 for num in 数値}
print(二乗辞書)

