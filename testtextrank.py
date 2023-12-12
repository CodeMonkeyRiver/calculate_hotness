import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

text = "近期，不少机构认为，石油的需求在下滑，尤其是美国的汽油消费。但OPEC却持反对意见。OPEC秘书长Haitham AlGhais在上周曾表示，尽管面临挑战，但经济“表现仍然良好”。本周，OPEC表示油市基本面仍然强劲，而中国2023年的原油进口量将创下年度新高，该组织认为近期负面市场情绪被夸大了。OPEC还在11月的月报中称:“尽管市场对中国石油需求表现和全球油市总体上存在过度的负面情绪，但最新的数据显示中国10月原油进口增至1,140万桶/日，且今年仍然有望创下年度新高。”中信建投期货表示，原油供需面没有较大变化。EIA公布了最新的库存报告，原油产量持稳于1320万桶/日，证实了数据调整项在2021年9月30日之后就已立即调整产量是因为调整项增加的。美国白宫能源顾问表示可能对伊朗实施新的制裁，11月12日当周俄罗斯原油出口也连续第二周下滑。"
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)  # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

print( '关键词：' )
for item in tr4w.get_keywords(20, word_min_len=1):
    print(item.word, item.weight)

print()
print( '关键短语：' )
for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
    print(phrase)

tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')

print()
print( '摘要：' )
for item in tr4s.get_key_sentences(num=3):
    print(item.index, item.weight, item.sentence)