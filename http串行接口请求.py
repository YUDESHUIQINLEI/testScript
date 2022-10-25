# -*- coding: utf-8 -*-

import json
import requests
from typing import List


def send_data():
    """
        http发送请求
    """
    requrl = "https://www.baidu.com"
    data = {
        "orderId": "xxx"
    }
    req_data = json.dumps(data)
    # 发送的完整请求数据
    # do some log
    print(req_data)

    header = {
        "Content-Type": "application/json; charset=UTF-8",
        "cookie": "xxxxx" 
    }

    # 发送数据，设置失败重试3次
    retry_times = 1
    for i in range(retry_times):
        try:
            res = requests.post(requrl, req_data, headers=header)
            print(res.json())
        except requests.RequestException as e:
            # do something
            print("retry times: {times} e: {e}".format(times=i, e=e))
            continue
    return False


if __name__ == '__main__':
    send_data()
