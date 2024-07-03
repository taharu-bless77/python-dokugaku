def divide(x,y):
    #まず試してみる処理A
    try:
         result = x / y

    # 引数に応じて処理を変更するフェーズ
    # 今回はy=0という場合に、この関数で行う処理を変更している。
    except ZeroDivisionError:
         print("分数の定義見返してきてね。")
    
    # 引数がexceptにひっからない場合にこの関数で行う処理。
    else: 
         print("結果は", result, "です")

    # 引数に関係なくこの関数で実行する処理。
    finally:
         print("計算を完了しました")   
    
print(divide(2,0))

