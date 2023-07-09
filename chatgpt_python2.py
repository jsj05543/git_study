import openai

# https://platform.openai.com/account/api-keysで設定したAPIキー
openai.api_key = "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"

# https://platform.openai.com/docs/guides/gpt
#  ================
#　role:system:ChatGPUの設定
#　role:user:ユーザからの質問
#　role:assistant:ChatGPTの回答
#  ================
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        #{"role": "system", "content": "語頭には「ChatGPT:」、すべての語尾に「じゃ」か「のじゃ。」をつけて質問に短く答えてください"},
        #{"role": "user", "content": "APIってなに？"},
        {"role": "system", "content": "語頭には「ChatGPT:」、すべての語尾に「じゃ」か「のじゃ。」をつけて質問に短く答えてください"},
        {"role": "assistant", "content": "APIとは、Application Programming Interfaceの略で、ソフトウェア同士が情報をやり取りするためのインターフェースのことじゃ。"},
        {"role": "user", "content": "具体的にどこで使われているの？"}

    ]
)
#print(type(response))
#print(response)
print(response["choices"][0]["message"]["content"])