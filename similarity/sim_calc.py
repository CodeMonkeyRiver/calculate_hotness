from gensim import corpora, models, similarities
import jieba

# 示例文本（中文）
documents = ["这是一个句子", "这也是一个句子", "这个句子没有语病"]

# 使用 jieba 进行中文分词
texts = [list(jieba.cut(doc)) for doc in documents]

# 创建词典
dictionary = corpora.Dictionary(texts)

# 创建语料库
corpus = [dictionary.doc2bow(text) for text in texts]

# 使用 TF-IDF 模型
tfidf = models.TfidfModel(corpus)

# 创建相似度矩阵
index = similarities.MatrixSimilarity(tfidf[corpus])

# 查询句子
query_document = '这是一个没有语病的句子'
query_bow = dictionary.doc2bow(list(jieba.cut(query_document)))
query_tfidf = tfidf[query_bow]

# 计算相似度
sims = index[query_tfidf]
print(list(enumerate(sims)))
