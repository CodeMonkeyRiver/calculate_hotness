from flask import Flask, request, render_template_string
import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
from io import StringIO
import gopup as gp

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form method="POST" action="/generate-chart">
        <input name="keyword" type="text" placeholder="Enter a keyword" />
        <input type="submit" value="Generate Chart">
    </form>
    '''

@app.route('/generate-chart', methods=['POST'])
def generate_chart():
    keyword = request.form.get('keyword')
    wb_index = gp.weibo_index(word=keyword, time_type="1month")
    # 这里应该是根据关键词查询热度指数的逻辑，现在用假数据代替
    # 使用 Pyecharts 创建折线图
    line_chart = Line()
    line_chart.add_xaxis(wb_index.index.strftime('%Y-%m-%d').tolist())
    line_chart.add_yaxis("热词指数", wb_index.iloc[:, 0].tolist() , is_smooth=True)
    line_chart.set_global_opts(title_opts=opts.TitleOpts(title=f"热词趋势图 - {keyword}"))

    # 将图表渲染为 HTML
    chart_html = line_chart.render_embed()

    # 返回包含图表的 HTML 页面
    return render_template_string(f'<html><body>{chart_html}</body></html>')

if __name__ == '__main__':
    app.run(debug=True)
