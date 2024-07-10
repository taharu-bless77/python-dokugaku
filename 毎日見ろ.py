class daigaku:
    def __init__(self,name, hen, num): 
        self.name = name#大学名
        self.hensati = hen#偏差値
        self.number = num#学生数

universities = [
    daigaku("東洋", 55.1, 10000),
    daigaku("日本", 55.0, 20000),
    daigaku("早稲田", 67.5, 6000),
    daigaku("慶應", 65.0, 7000),
    daigaku("明治", 60.0, 8000),
    daigaku("東京理科", 62.0, 9000),
    daigaku("専修", 54.0, 11000),
    daigaku("駒澤", 54.0, 12000)
]

results = ["{} > {}".format(u1.name, u2.name) if u1.hensati > u2.hensati else "{} < {}".format(u1.name, u2.name)
           for i, u1 in enumerate(universities) for u2 in universities[i + 1:]]

for i, u1 in enumerate(universities):
    for u2 in universities[i + 1:]:
        if u1.hensati > u2.hensati:
            results.append("{} > {}".format(u1.name, u2.name))
        else:
            results.append("{} < {}".format(u1.name, u2.name))