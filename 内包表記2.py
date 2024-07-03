def check_scores(xs):
    return all(s >= 60 for s in xs)

#enumirate()
#for文でリストの要素を添字を含めて取り出したいときに使う。

xs = ["た","い","は","え","る","か","ち","く","こ","で","く"]
for s, x in enumerate(xs):
    if s % 2 == 0:
        print(s,x)

#zip(x,y)
#二つ以上のリストから同時に要素を取り出したいときにこれを使う。
station = ['大宮','浦和','赤羽','池袋','新宿','渋谷']
namberling = [24, 23, 22, 21, 20, 19]
for x, y in zip(station, namberling):
    print(x, 'js'+ str(y))