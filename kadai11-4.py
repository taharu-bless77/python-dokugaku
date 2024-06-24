import re

def us_to_bk(date):
    # 正規表現でマッチングを行う
    x = re.fullmatch(r'(\d{1,2})\/(\d{1,2})\/(\d{4})', date)
    
    # マッチが成功した場合、イギリス式の日付に変換
    if x:
        return '{}/{}/{}'.format(x.group(2), x.group(1), x.group(3))
    else:
        return None

# テストケース
print(us_to_bk("5/2/2018"))  # 出力: "2/5/2018"