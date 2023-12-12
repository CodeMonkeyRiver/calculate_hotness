from gensim import corpora, models, similarities
import jieba

def calculate_topic_similarity(documents, topic):
    try:
        texts = [list(jieba.cut(doc)) for doc in documents]
        topic_words = list(jieba.cut(topic))
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        lda = models.LdaModel(corpus, id2word=dictionary, num_topics=2, random_state=100)
        index = similarities.MatrixSimilarity(lda[corpus], num_features=len(dictionary))
        for i, doc in enumerate(corpus):
            doc_vec = lda[doc]
            sims = index[doc_vec]
            doc_summary = documents[i][:50] + "..."  # 截取文档的前50个字符作为摘要
            print(f"文档 {i}（摘要：'{doc_summary}'）的相似度分数: {sims}")

        topic_vec = lda[dictionary.doc2bow(topic_words)]
        sims = index[topic_vec]
        return list(enumerate(sims))
    except IndexError as e:
        print("IndexError occurred: ", e)
        # 返回一个默认值或执行其他错误处理
        return []


def calc_topic_similarity(documents, topic):
    try:
        texts = [list(jieba.cut(doc)) for doc in documents]
        topic_words = list(jieba.cut(topic))
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        lda = models.LdaModel(corpus, id2word=dictionary, num_topics=2, random_state=100)
        topic_vec = lda[dictionary.doc2bow(topic_words)]
        index = similarities.MatrixSimilarity(lda[corpus], num_features=len(dictionary))

        sims = index[topic_vec]  # 计算主题向量与所有文档的相似度
        return list(enumerate(sims))
    except IndexError as e:
        print("IndexError occurred: ", e)
        return []


# 示例使用
documents = ["苹果出新手了","iphone 15太好用","华为手机不好用","这场比赛太精彩"]
topic = "小米"
similarity_scores = calculate_topic_similarity(documents, topic)
