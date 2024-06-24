import re
def to_minutes(t): #引数は文字列
    match = re.fullmatch(r'(\d{1,2})\:(\d{1,2})',t)
    if match:
        hours = int(match.group(1))   #str型の数字を、int型にし、計算可能にする。
        minutes = int(match.group(2))
        total_minutes = hours * 60 + minutes
        return total_minutes
    else:
        raise ValueError("Invalid time format")
    
print(to_minutes("12:45"))

#抽出した時間と分を整数に変換し、合計分数を計算。
#入力を文字列として渡す。
#この修正版は "12:45" という入力を正しく受け取り、合計分数を計算して出力します。

def time_diff(t1,t2):#引数は文字列
    ts1 = to_minutes(t1)
    ts2 = to_minutes(t2)
    return abs(ts1 - ts2)

print(time_diff("12:46","23:12"))


    



