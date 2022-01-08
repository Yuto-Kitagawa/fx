from selenium import webdriver
# エラー文をなくすパッケージ
import chromedriver_binary
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from matplotlib import pyplot as plt
import sys
# optionをつけないとエラー文がでる
# headerだけを設定するやり方もあるらしい
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True
driver = webdriver.Chrome(options=options)

# 今回は楽天さんのサイトを利用させてもらう
source_url = "https://www.rakuten-sec.co.jp/web/fx/"
# urlの情報を取得
driver.get(source_url)

# リストを宣言
doll_price_array = []
time_array = []

# 今の時間を取得する関数


def getTime():
    dt_now = datetime.datetime.now()
    return dt_now.strftime('%H:%M:%S')

# 今の値段を取得する関数


def getPrice():
    price = driver.find_element(By.ID, "FXBID2")
    doll_price_array.append(price.text)

    print("リストの長さ:" + str(len(doll_price_array)))

    time_str = getTime()
    time_array.append(time_str)

    print(doll_price_array)


time.sleep(2)
# 一度図を書かないと、ループの中でエラーが出る
getPrice()
fig, ax = plt.subplots(1, 1)
# 図の縦軸、横軸を設定
lines, = ax.plot(time_array, doll_price_array)

# pauseで何秒ごとに取得するかを設定できる
# リアルタイムで図を更新できるようにpause()にした
while(True):
    try:
        getPrice()
        # 取得したデータを追加
        lines.set_data(time_array, doll_price_array)
        ax.set_xlim(min(time_array), max(time_array))

        # 横軸はmax20秒までにしている
        if(len(time_array) > 20):
            max_index = len(time_array)
            plt.xlim(time_array[max_index - 20], max(time_array))

        ax.set_ylim(min(doll_price_array), max(doll_price_array))
        plt.pause(1)

    except:
        sys.exit()
