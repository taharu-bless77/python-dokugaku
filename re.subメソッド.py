import re

smartphones_password = 'スマートフォンのパスワードは 082498 です'
x = re.sub(r'\d{6}','*'*6,smartphones_password)
print(x)


#re.sub(regexp,repl,s)
#正規表現regexpで文字列sの検索を行い、マッチした部分をreplで置き換えた文字列を返します。
