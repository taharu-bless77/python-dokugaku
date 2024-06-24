def mikitani(yen):
    yen_str = str(yen)[::-1]
    result = []

    for i in range(0,len(yen_str)):
       result.append(yen_str[i])
       if  (i + 1) % 3 == 0 and (i + 1) != len(yen_str):
       #and演算子は、2つ以上の条件文のうちすべてが正しいという状況を表す時に使用します。
       #”!=”はノットイコール
       #(i + 1) != len(yen_str)により、余分なカンマが最後に追加されるのを防ぐ。
       #要素数３ならば、３桁目は最後の数と表現できる。１２３
           result.append(',') 
    
    return ''.join(result[::-1])


print(mikitani(123456789))