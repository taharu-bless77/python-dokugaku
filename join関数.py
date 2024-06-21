def mult_table():
    for i in range(1, 10):
        result = []
        for j in range(1, 10):
            result.append(str(i * j))  
        print('\\'.join(result))  

mult_table()



#joinメソッドとは、指定された区切り文字で、”文字列群”を結合するためのメソッド。
#各要素間の結合リストは、mocks上に掲載されている。