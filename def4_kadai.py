# def4.kadai.py
#
#ランダムでくじの中の一つを返す関数
import random
def omikuji():
    kuji = ["大吉","中吉","小吉","凶"]
    return random.choice(kuji)
#エントリーポイントの定義
kekka = omikuji()
print("結果は", kekka, "です")

if __name__ == "_main_":
    main()
