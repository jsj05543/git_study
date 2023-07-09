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
        {"role": "system", "content": "ChatGPTへの指示"},
        {"role": "user", "content": "桜はいつごろ咲きそうですか"}

    ]
)
#print(type(response))
#print(response)
print(response["choices"][0]["message"]["content"])