a = [str(i) for i in range(100)]
s = " ".join(a)
print(s)
#リスト内包表記と文字列の結合を用いて0~99までをスペース区切りで
#aのような文字列のリストを作成
#s = " ".join(a)で文字列結合を行う、リストaの各要素を""でスペース区切りで結合する（ｓに）

s = "{0:.9f}".format(1.0 / 7.0)
print(s)
#"{0:.9f}"のフォーマットを利用する
#{0}で最初の値を指定して、:.9fで小数点以下9桁まで表示する浮動小数点数を指定する
#結果→0.142857143