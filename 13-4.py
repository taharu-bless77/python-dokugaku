gym = ['JPN','RUS','CHN','GBR','USA','BRA','GER','UKR']
#キー
順位 = [1,2,3,4,5,6,7,8]
#値
gym_Rank = {}
#空辞書

for 国,順位値 in zip(gym, 順位):
    gym_Rank[国] = 順位値

print(gym_Rank)





