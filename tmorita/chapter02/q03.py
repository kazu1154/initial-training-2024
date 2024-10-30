# リスト a を定義
a = [4, 8, 3, 4, 1]

# リスト a の先頭の要素を取り除く（[8, 3, 4, 1]）
a.pop(0)
print(f"先頭の要素を取り除いたリスト: {a}")

# リスト a の末尾の要素を取り除く（[4, 8, 3, 4]）
a.pop()
print(f"末尾の要素を取り除いたリスト: {a}")

# リスト a の末尾に 100 を追加する（[4, 8, 3, 4, 100]）
a.append(100)
print(f"末尾に100を追加したリスト: {a}")