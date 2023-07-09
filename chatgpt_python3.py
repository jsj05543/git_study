import openai


def main():
    # https://platform.openai.com/account/api-keysで設定したAPIキー
    openai.api_key = "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"
    amount_tokens = 0
    chat = []

    setting = input("ChatGPTに設定を加えしますか？y/n\n")
    if setting == "y" or setting == "Y":
        content = input("内容を入力してください。\n")
        chat.append({"role": "system", "content": content})

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

chat = main()        