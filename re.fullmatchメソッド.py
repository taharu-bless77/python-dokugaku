import re
def japanese_name(s):
    match  = re.fullmatch (r'(Mr|Ms)\.(\w+) (\w+)',s)
    return '{0}{1}さん'.format(match.group(3),match.group(2))
#{0}⇔match.group(3)=formatの要素１つ目
#{1}⇔match.group(2)=formatの要素2つ目

#match.group.(n)⇔\n

#