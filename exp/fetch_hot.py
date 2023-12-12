import requests

# 请求今日热榜 API 获取热搜榜数据
response = requests.get('https://open.tophub.today/hot')
if response.status_code == 200:
    # 将响应的 JSON 数据解析为 Python 对象
    data = response.json()

    # 你可以根据 data 的具体结构来获取需要的信息
    # 例如，打印获取的数据以检查结构
    print(data)
else:
    print("Failed to fetch data: Status code", response.status_code)
