# -*- coding: utf-8 -*-

import json
import requests
from typing import List


def send_data():
    """
        http发送请求
    """
    requrl = "https://aries-test.zhenguanyu.com/aries-admin-server-trade/api/orderWithCard/refund"
    data = {
        "orderId":27352
    }
    req_data = json.dumps(data)
    # 发送的完整请求数据
    # do some log
    print(req_data)

    header = {
        "Content-Type": "application/json; charset=UTF-8",
        "cookie": "ajs_user_id=%229a56e677d1c7ce57f7860a1208c88f5171133d37%22; ajs_anonymous_id=%221b02fbdd-f805-4be8-a95d-5f6fedd666f7%22; gr_user_id=103b4475-bae3-4fda-8c6b-9cb0dbad2463; _ga=GA1.1.1676551006.1665653456; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22183f417dfeb9a5-0fd1ec1e14011e-19525635-2211840-183f417dfece43%22%2C%22%24device_id%22%3A%22183f417dfeb9a5-0fd1ec1e14011e-19525635-2211840-183f417dfece43%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga_SSDR76QHV9=GS1.1.1666361111.13.1.1666361111.0.0.0; SESS=FzAcWtUjOwF6JGSgw6P4q4RWy%2BnyN%2B6iSBFgppDSZdWXjjh%2F6BbgJ9IL6O8P8o78; SESS_V2=M4X4FnXIOE7aql2KQJcJXG8hdjODeFncE5nEz0kA0EBtagFZP6tEr4PbpgOlNRreii0Oy2%2FWvVEQf6rs%2FMWWVMKZIbeaIYpoQU6IL%2FfWXMjPs2D6XL54xZ8b%2F0oEEOHtdF01I5ZdReCJg%2B4RoX5gtvQ3WFEFHgCB5Jdn7tT2Rug%3D; YFD_U=1666596053109-35616"
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