class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    #この__init__メソッドは、wとhという2つの引数を受け取り、それらをインスタンス変数self.width,self.heightとして設定します。
    
    def area(self):
        return self.width * self.height

# Rectangleクラスのインスタンスを生成
r = Rectangle(9, 88)

# インスタンスの属性にアクセス
print(r.width)  # 出力: 9
print(r.height)  # 出力: 88

# インスタンスのメソッドを呼び出し
print(r.area())  # 出力: 792

#捜査対象.操作⇒ex,リスト.append(w)