import hanlp
import openai

openai.api_key = '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'  # 替换为你的 OpenAI API 密钥

text = "中国科学技术大学位于安徽省合肥市，是一所著名的高等学府。"

completion = openai.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
        {"role": "system", "content": "提取主体"},
        {"role": "user", "content": text}
    ]
)
print(completion.choices[0].message)


# 加载预训练模型
recognizer = hanlp.load(hanlp.pretrained.ner.MSRA_NER_BERT_BASE_ZH)

# 示例文本


# 实体识别
#entities = recognizer([list(text)])
#print(entities)



