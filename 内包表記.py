def overlap(xs,ys):
    return [x for x in xs if x in ys]

#all(xs)
#リストxsに含まれるすべての要素がTrueかどうかをチェック
all((x % 2) == 0 for x in range(0,10))
all((y % 3) == 0 for y in range(0,30))

#any(xs)
#リストxsにTrueとなる要素が含まれるかどうかをチェック
any((x % 2) == 0 for x in range(0,10))
