import re

def exists21(xs):
    return any(re.fullmatch(r's1f\d{2}21\d{5}', item) for item in xs)
#`any()`関数を使って,
# リストxs中の少なくとも一つの要素が,
# 条件「re.fullmatch(r's1f\d{2}21\d{5}', item)」に一致するかどうかを判定しています。
aaa = ['s1f102101742', 'iniad', 's1f103870329']

# 関数を呼び出し、結果を表示
print(exists21(aaa))