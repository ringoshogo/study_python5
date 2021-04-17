import eel
import desktop

import fileiohandler

app_name="html"
end_point="index.html"
size=(800,600)

@ eel.expose
def get_item_list() -> list:
    """csvファイルを読み込んでlistを返却する"""
    return fileiohandler.read_csv()

@ eel.expose
def write_log(received_money, selected_list):
    """受け取った文字列を"""
    fileiohandler.write_log(received_money, selected_list)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)