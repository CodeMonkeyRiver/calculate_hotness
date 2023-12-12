from flask import Flask, request, render_template_string
from openai import OpenAI



app = Flask(__name__)

# HTML模板
HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <title>Simple Webpage</title>
    <style>
        input[type="text"] {
            width: 90%; /* 输入框占页面宽度的百分比 */
            height: 50px; /* 输入框的高度 */
            font-size: 20px; /* 输入框内文本的字体大小 */
            margin: 10px 0; /* 输入框的外边距 */
            padding: 10px; /* 输入框的内边距 */
        }
        input[type="submit"] {
            width: 92%; /* 按钮的宽度 */
            height: 50px; /* 按钮的高度 */
            font-size: 20px; /* 按钮的字体大小 */
        }
    </style>
</head>
<body>
    <form action="/submit" method="post">
        <input type="text" name="text_input" placeholder="Enter text here">
        <input type="submit" value="Confirm">
    </form>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit', methods=['POST'])
def submit():
    # 获取输入框的文字
    client = OpenAI()

    messages = [{"role": "system", "content":
        "You are a intelligent assistant."}]

    text = request.form['text_input']
    messages.append(
        {"role": "user", "content": text},
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    # 打印文字
    print("aa", text)
    print("Received text:", completion.choices[0].message.content)
    return f'Received text: {completion.choices[0].message.content}'

if __name__ == '__main__':
    app.run(debug=True)