def mult_table():
    for i in range(1, 10):
        result = []
        for j in range(1, 10):
            result.append(str(i * j))  
        print('\\'.join(result))  

mult_table()

#join関数は、”()内にあるリスト等の各要素間の結合”を引数に取る関数。
#各要素間の結合リストは、mocks上に掲載されている。