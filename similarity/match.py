from gensim import corpora, models, similarities
import jieba

documents = ["11月28日受司机端结算、定位、接单等功能故障影响，他白天选择在家休息，在接单系统恢复正常后决定晚高峰出门跑单。除了外部服务出现问题，从内部员工反馈看，服务系统崩溃时滴滴内网也处于崩溃状态，员工无法正常使用内网相关服务。在11月28日下午，滴滴内网完成修复。", "受此影响，乐有家研究中心监测显示，新政后客户看房量上涨，11月26日当日看房量达9月以来第二高点，接近“认房不认贷”政策后的最高值。从成交量看，乐有家门店成交环比新政前一周涨幅超过10%。“新政出来后，客户预约看房的明显增多，有性价比高的笋盘基本都会出手。我们感受到11月份的市场确实略有回升，大部分是置换型的客户，新政策的出台力度也比较符合预期。”深圳市龙岗区一位房产中介告诉第一财经，从数据和一线情况看，龙岗区当前市场确实比较活跃。北京近期虽没有新政出台，但二手房市场也出现躁动。根据北京市住建委公布的网签数据，11月北京二手住宅网签量为12545套，环比增长17.8%，同比增长16.7%。", "滴滴系统崩了"]
topic = "二手房成交量"

def calculate_topic_similarity(documents, topic):
    # 示例文本和主题
    print(documents)
    print(topic)
    # 使用 jieba 进行中文分词
    texts = [list(jieba.cut(doc)) for doc in documents]
    topic_words = list(jieba.cut(topic))

    # 创建词典
    dictionary = corpora.Dictionary(texts)

    # 创建语料库
    corpus = [dictionary.doc2bow(text) for text in texts]

    # 使用 LDA 模型
    lda = models.LdaModel(corpus, id2word=dictionary, num_topics=2, random_state=100)

    # 将主题转换为 LDA 空间
    topic_vec = lda[dictionary.doc2bow(topic_words)]

    # 创建相似度矩阵
    index = similarities.MatrixSimilarity(lda[corpus])

    # 计算相似度
    sims = index[topic_vec]
    print(list(enumerate(sims)))

    return list(enumerate(sims))


calculate_topic_similarity(documents, topic)
