from flask import Flask, render_template_string, request, jsonify
from content_process import summary, extractSubject
from similarity.match import calculate_topic_similarity
import json

app = Flask(__name__)

articles = [
        {"title": "探访滴滴总部 有员工称:系统崩溃时内网也崩了", "date": "2023-11-28", "content": "11月28日受司机端结算、定位、接单等功能故障影响，他白天选择在家休息，在接单系统恢复正常后决定晚高峰出门跑单。除了外部服务出现问题，从内部员工反馈看，服务系统崩溃时滴滴内网也处于崩溃状态，员工无法正常使用内网相关服务。在11月28日下午，滴滴内网完成修复。", "url": "https://www.yicai.com/news/101914163.html"},
        {"title": "一线城市二手房交易上涨", "date": "2023-12-05", "content": "1月23日起，深圳开始执行两条楼市新政：一是下调二套住房首付比例，二套住房个人住房贷款最低首付款比例统一调整为40%。二是享受优惠政策的普通住房标准有所松动，建筑面积小于144平方米、但总价高于750万元的住宅，将被纳入普通住宅的范畴，二手房交易时将节省不少税费。受此影响，乐有家研究中心监测显示，新政后客户看房量上涨，11月26日当日看房量达9月以来第二高点，接近“认房不认贷”政策后的最高值。从成交量看，乐有家门店成交环比新政前一周涨幅超过10%。“新政出来后，客户预约看房的明显增多，有性价比高的笋盘基本都会出手。我们感受到11月份的市场确实略有回升，大部分是置换型的客户，新政策的出台力度也比较符合预期。”深圳市龙岗区一位房产中介告诉第一财经，从数据和一线情况看，龙岗区当前市场确实比较活跃。北京近期虽没有新政出台，但二手房市场也出现躁动。根据北京市住建委公布的网签数据，11月北京二手住宅网签量为12545套，环比增长17.8%，同比增长16.7%。", "url": "https://www.yicai.com/news/101918689.html"},
        {"title": "滴滴app挂了", "date": "2023-12-03", "content": "滴滴系统崩了", "url": "https://www.yicai.com/news/101914163.html"},
        # ... 更多文章
    ]

@app.route('/')
def index():
    return render_template_string(open('index.html').read())  # 确保 index.html 在同一目录下

@app.route('/get-hot-articles')
def get_hot_articles():
    # 示例数据，实际应该从数据库或其他源获取

    return jsonify(articles)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('text')
    summary_result = summary(text)
    return jsonify({'summary': summary_result})

@app.route('/extract', methods=['POST'])
def extract():
    text = request.form.get('text')
    subject = extractSubject(text)
    return jsonify({'subject': subject})

@app.route('/calculate', methods=['POST'])
def calculate():
    # 这里添加热度计算的逻辑
    topics = request.form.get('subjects')
    subjects = json.loads(topics)
    best_matches = []
    top_two_matches = []
    articles_content = [article['content'] for article in articles]
    for topic in subjects:
        # 获取当前主体与所有文档的相似度分数
        similarity_scores = calculate_topic_similarity(articles_content, topic)
        # top2 逻辑
        top_two_matches = sorted(similarity_scores, key=lambda item: item[1], reverse=True)[:1]
        top_articles = []
        for match in top_two_matches:
            article_index = match[0]
            score = match[1]
            top_articles.append({
                'score': float(score),
                'article': articles[article_index]
            })

        best_matches.append({
            'topic': topic,
            'top_articles': top_articles
        })

        # 找出匹配度最高的文章
        # best_match = max(similarity_scores, key=lambda item: item[1])
        # best_article_index = best_match[0]
        # best_score = best_match[1]
        #
        # best_matches.append({
        #     'topic': topic,
        #     'score': float(best_score),
        #     'best_article': articles[best_article_index]
        # })

    print(best_matches)
    return jsonify(best_matches)
    #return jsonify({'score': score})

if __name__ == '__main__':
    app.run(debug=True)
