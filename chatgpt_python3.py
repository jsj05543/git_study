import openai


def chatgpt():
    # https://platform.openai.com/account/api-keysで設定したAPIキー
    openai.api_key = "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"
    amount_tokens = 0
    chat = []

    print("チャットを開始します。qまたはquitで終了します。")
    print("_"*50)
    while True:
        user = input("<あなた>\n")
        if user =="q" or user == "quit":
            print(f"トークン数は{amount_tokens}でした。")
            break
        else:
            chat.append({"role": "user", "content": user })

        print("<ChatGPT>")
        # https://platform.openai.com/docs/guides/gpt
        #  ================
        #　role:system:ChatGPUの設定
        #　role:user:ユーザからの質問
        #　role:assistant:ChatGPTの回答
        #  ================
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = chat
        )
        msg = response["choices"][0]["message"]["content"].lstrip()
        amount_tokens += response["usage"]["total_tokens"]
        print(msg)
        chat.append({"role": "assistant", "content": msg})

chat = chatgpt()        