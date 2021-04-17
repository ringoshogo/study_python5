import csv
from datetime import datetime

SRC_URL = "./source.csv"
LOG_URL = "./log.txt"

def read_csv() -> list:
    """csvファイルを読み込んでlistを返却する"""
    with open(SRC_URL, "r", encoding="utf-8_sig") as f:
        reader = csv.reader(f)
        return [{"code": row[0], "name": row[1], "price": row[2]} for index, row in enumerate(reader) if index != 0]

def write_log(received_money, selected_list):
    """受け取った文字列を"""
    total_price = 0
    result = []
    result.append("============================================日時")
    result.append(datetime.now().strftime('%Y/%m/%d_%H:%M:%S'))
    result.append("=========================================購入商品")
    for item in selected_list:
        result.append(f"購入商品：{item['name']} 購入数量：{item['amount']} 個 小計：{item['price']} 円 ")
        total_price += int(item['price'])
    result.append(f"合計金額：{total_price} 円")
    result.append("======================================お預かり金額")
    result.append(f"{received_money} 円")
    result.append("===========================================御釣り")
    result.append(f"{int(received_money) - total_price} 円")
    log_str = "\n".join(result)
    with open(LOG_URL, "a", encoding="utf-8_sig") as f:
        f.write(log_str + "\n\n")

if __name__ == "__main__":
    print(read_csv())
