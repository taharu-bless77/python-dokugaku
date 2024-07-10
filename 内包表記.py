def overlap(xs,ys):
    return [x for x in xs if x in ys]

#all(xs)
#リストxsに含まれるすべての要素が条件を満たすかどうかをチェック
all((x % 2) == 0 for x in xs)
all((y % 3) == 0 for y in xs)

#any(xs)
#リストxsに条件を満たす要素が含まれるかどうかをチェック
any((x % 2) == 0 for x in xs)
