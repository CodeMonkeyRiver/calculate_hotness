#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
from flask import Flask, request, render_template_string
import gopup as gp
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from datetime import datetime, timedelta
import openai

#接口地址
url ="http://ltpapi.xfyun.cn/v1/ke"
#开放平台应用ID
x_appid = "c973bdcc"
#开放平台应用接口秘钥
api_key = "ac8cf13d2b69e41d2132f1704c20153e"
#语言文本
#TEXT="近期，不少机构认为，石油的需求在下滑，尤其是美国的汽油消费。但OPEC却持反对意见。OPEC秘书长Haitham AlGhais在上周曾表示，尽管面临挑战，但经济“表现仍然良好”。本周，OPEC表示油市基本面仍然强劲，而中国2023年的原油进口量将创下年度新高，该组织认为近期负面市场情绪被夸大了。OPEC还在11月的月报中称:“尽管市场对中国石油需求表现和全球油市总体上存在过度的负面情绪，但最新的数据显示中国10月原油进口增至1,140万桶/日，且今年仍然有望创下年度新高。”中信建投期货表示，原油供需面没有较大变化。EIA公布了最新的库存报告，原油产量持稳于1320万桶/日，证实了数据调整项在2021年9月30日之后就已立即调整产量是因为调整项增加的。美国白宫能源顾问表示可能对伊朗实施新的制裁，11月12日当周俄罗斯原油出口也连续第二周下滑。"

def extract_words(TEXT):
    body = urllib.parse.urlencode({'text': TEXT}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    # print(result.decode('utf-8'))

    json_data = json.loads(result)
    keywords = json_data["data"]["ke"]
    top_three_keywords = keywords[:5]
    top_three_words = [keyword["word"] for keyword in top_three_keywords]
    print(top_three_words)

    return top_three_words

app = Flask(__name__)
openai.api_key = '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'  # 替换为你的 OpenAI API 密钥

# HTML模板
HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <title>Simple Webpage</title>
    <!-- 在这里添加你的CSS样式 -->
     <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f2f2f2;
        }

        .form-container {
            width: 50%; /* 控制表单容器的宽度 */
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
            font-size: 16px;
            resize: vertical;
            min-height: 200px;
        }

        button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        .keywords-container {
            margin-top: 20px;
        }
        
        .chart-container {
            width: 100%; /* 控制表单容器的宽度 */
            margin: 0 auto;
            padding: 20px;
            text-aligh: center;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <form action="/submit" method="post">
            <textarea name="text_input" placeholder="Enter text here">
                {% if text %}
                    {{ text }}
                {% endif %}
            </textarea>
            <button type="submit">Confirm</button>
        </form>
    
         <div class="keywords-container">
            {% if keywords %}
                <p>Keywords: {{ keywords }}</p>
            {% endif %}
         </div>
         <div class="chart-container">
             {% if chart_html %}
                {{ chart_html | safe }}
            {% endif %}
         </div>
    </div>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit', methods=['POST'])
def submit():
    # 获取输入框的文字
    text = request.form['text_input']
    chart_html = ""
    # 使用 GPT 模型提取关键词
    try:

        # completion = openai.chat.completions.create(
        #     model="gpt-4-1106-preview",
        #     messages=[
        #         {"role": "system", "content": "Extract top 5 keywords from the following text."},
        #         {"role": "user", "content": text}
        #     ]
        # )
        # print(completion.choices[0].message)
        # keywords = completion.choices[0].message.content
        #
        # print(keywords)
        #keywords = ['石油需求', 'OPEC','']
        keywords = extract_words(text)
        print(keywords)
        # 创建一个折线图
        line_chart = Line(init_opts=opts.InitOpts(width="100%", height="400px"))  # 调整为合适的大小
        line_chart.set_global_opts(
            title_opts=opts.TitleOpts(title="微博指数趋势"),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45))  # 旋转 X 轴标签
        )
        colors = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae']
        # 获取关键字后，搜索指数
        for i, keyword in enumerate(keywords):
            wb_index = gp.weibo_index(keyword, time_type="1month")
            print(wb_index)
            if wb_index is not None:
                line_chart.add_xaxis(wb_index.index.strftime('%Y-%m-%d').tolist())
                # 每隔几个点显示一个数据标签
                values = wb_index.iloc[:, 0].tolist()
                # labels = [format_to_wan(value) if idx % 5 == 0 else '' for idx, value in enumerate(values)]

                line_chart.add_yaxis(keyword, wb_index.iloc[:, 0].tolist(), color=colors[i % len(colors)],
                                     label_opts=opts.LabelOpts(is_show=False, position="top", color=colors[i % len(colors)])
                                     # 显示数据标签
                                     )

        chart_html = line_chart.render_embed()

    except Exception as e:
        keywords = f"Error: {e}"

    # 将关键词返回到前端
    return render_template_string(HTML_TEMPLATE,keywords=keywords, chart_html=chart_html)



if __name__ == '__main__':
    app.run(debug=True)
