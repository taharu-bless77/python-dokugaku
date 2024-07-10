import re
def get_gmail(xs):
    return [x +"@iniad.org" for x in xs if re.fullmatch(r's1f\d{9}',x)]

aaa = ['s1f102401742','iniad','s1f103870329']
print(get_gmail(aaa))

    
