class TrainItem:
    
    # 1, 新たな型MenuItemを定義
    def __init__(self, station, fare):
        self.station = station
        self.fare = fare

    #3, 関数を定義
    def show(self):
        print('赤羽駅から{0}駅まで{1}円で行けます'.format(self.station, self.fare))

    #3, 関数を定義
    def is_affordable(self,yen):
        return self.fare <= yen
    
    # 2, MenuItem型の値を作成
Destination = [
    TrainItem("池袋", 170),
    TrainItem("新宿", 230),
    TrainItem("渋谷", 230),
    TrainItem("大宮", 260),
    TrainItem("横浜", 580),
]

 #program本体
for item in Destination:
    item.show()
    