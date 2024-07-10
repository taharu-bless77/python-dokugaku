import re
def count_uid(xs):
    a = [x for x in xs if re.fullmatch(r's1f\d{9}',x)]
    return len(a)

aaa = ['s1f102401742','iniad','s1f103870329']
print(count_uid(aaa))
    