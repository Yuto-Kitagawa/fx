import traceback
from selenium import webdriver
import chromedriver_binary
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from matplotlib import pyplot as plt
import sys
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.use_chromium = True
driver = webdriver.Chrome(options=options)

source_url = "https://www.rakuten-sec.co.jp/web/fx/"
driver.get(source_url)

# リストを使えるようにするにはまず、これを書く
doll_price_array = []
time_array = []


def getTime():
    dt_now = datetime.datetime.now()
    return dt_now.strftime('%H:%M:%S')


def getPrice():
    price = driver.find_element(By.ID, "FXBID2")

    # リストに入れるコマンド
    # リストの名前 . append　(入れる物)
    doll_price_array.append(price.text)

    # length(日本語で長さの意味)
    # len()で長さがわかる
    print("リストの長さ:"  + str(len(doll_price_array)))  # 数字

    time_str = getTime()
    time_array.append(time_str)

    print(doll_price_array)


time.sleep(2)
getPrice()
fig, ax = plt.subplots(1, 1)
lines, = ax.plot(time_array, doll_price_array)

while(True):
    try:
        getPrice()
        lines.set_data(time_array, doll_price_array)
        ax.set_xlim(min(time_array), max(time_array))

        if(len(time_array) > 20):
            max_index = len(time_array)
            plt.xlim(time_array[max_index - 20], max(time_array))

        ax.set_ylim(min(doll_price_array), max(doll_price_array))
        plt.pause(1)

    except:
        sys.exit()
