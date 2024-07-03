import requests

def get_chat_id(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    response = requests.get(url)
    data = response.json()
    if data['ok']:
        if data['result']:
            chat_id = data['result'][-1]['message']['chat']['id']
            return chat_id
        else:
            print("No messages received yet.")
            return None
    else:
        print(f"Error: {data['description']}")
        return None

if __name__ == "__main__":
    bot_token = "6914400012:AAGTZiJAoi2w_Q24QCidy3apONn0lcDJ_5E"
    chat_id = get_chat_id(bot_token)
    if chat_id:
        print("Chat ID:", chat_id)
        