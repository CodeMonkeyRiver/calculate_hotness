
import gopup as gp
import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts
from datetime import datetime, timedelta
from pyecharts.commons.utils import JsCode

# 数字格式化函数：将大数字转换为以万为单位
def format_to_wan(num):
    return f'{num / 10000:.2f}万' if num >= 10000 else str(num)

# 假设这是从 GPT 提取出的前 5 个关键词
keywords = ['滑雪','攀岩', '中美']

# 获取今天的日期和一个月前的日期
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# 创建一个折线图
line_chart = Line()
line_chart.set_global_opts(
    title_opts=opts.TitleOpts(title="微博指数趋势"),
    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45))  # 旋转 X 轴标签
)
colors = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#91c7ae']
# 对每个关键词获取数据并添加到图表中
for i, keyword in enumerate(keywords):
    wb_index = gp.weibo_index(keyword, time_type="1month")
    line_chart.add_xaxis(wb_index.index.strftime('%Y-%m-%d').tolist())
    # 每隔几个点显示一个数据标签
    values = wb_index.iloc[:, 0].tolist()
    #labels = [format_to_wan(value) if idx % 5 == 0 else '' for idx, value in enumerate(values)]

    line_chart.add_yaxis(keyword, wb_index.iloc[:, 0].tolist(), color=colors[i % len(colors)],
                         label_opts=opts.LabelOpts(is_show=False, position="top", color=colors[i % len(colors)])
                         # 显示数据标签
                         )


# 生成并保存图表
line_chart.render('weibo_index_trend.html')
