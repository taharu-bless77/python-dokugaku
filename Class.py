class BodyShape:
    def __init__(self, h, w):
        self.height = h
        self.weight = w
#１．self.属性

    def is_taller_than(self, other):
        if not isinstance(other, BodyShape):
##２．引数 other が BodyShape クラスのインスタンスであることを確認します。そうでない場合は TypeError を投げます。
            raise TypeError("Argument must be of type Point")
        elif self.height > other.height:
###３．otherは、クラス型の値(オブジェクト)の代名詞です。
####４．otherというオブジェクトに対してheight属性を指定。
            return True
        else:
            return False
        
taro = BodyShape(170.0, 60.0)
hanako = BodyShape(160.0, 50.0)
print(hanako.height)
print(taro.is_taller_than(hanako))
    

