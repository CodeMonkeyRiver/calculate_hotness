# content_process.py
import openai

openai.api_key = '###'  # 替换为你的 OpenAI API 密钥

def summary(text):
    # 这里实现摘要逻辑
    completion = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "一句话摘要"},
            {"role": "user", "content": text}
        ]
    )
    print("处理中...")
    print(completion.choices[0].message)
    summary_text = completion.choices[0].message.content
    return summary_text

def extractSubject(summary):
    print('aa')
    # 提取主体
    completion = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "请提取这段文字中描述最重要的主体词语，最多两个主体，请返回为python的数组格式，后续我会以此内容作为函数的入参"},
            {"role": "user", "content": summary}
        ]
    )
    print(completion.choices[0].message)
    return completion.choices[0].message.content
