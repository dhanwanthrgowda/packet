import requests
import random
import time
import os

def generate_otp():
    otp = random.randint(1000, 9999)
    return otp


def get_updates(bot_token, offset=None):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    if response.ok:
        return response.json()
    else:
        print(f"Failed to get updates: {response.text}")
        return None
def get_last_message(bot_token="6914400012:AAGTZiJAoi2w_Q24QCidy3apONn0lcDJ_5E"):
    offset = None
    last_message = None

    while True:
        updates = get_updates(bot_token, offset)
        if updates:
            for update in updates.get("result", []):
                update_id = update["update_id"]
                message = update.get("message", {})
                if message:
                    text = message.get("text")
                    chat_id = message["chat"]["id"]
                    print(f"Received message: {text} from chat ID: {chat_id}")
                    last_message = text

                # Update the offset to the next update_id
                offset = update_id + 1

            # If a message was received, break out of the loop and return it
            if last_message:
                break

        # Sleep for a short while to avoid hitting the API rate limit
        time.sleep(1)

    return last_message


def send_telegram_otp(bot_token = "6914400012:AAGTZiJAoi2w_Q24QCidy3apONn0lcDJ_5E", chat_id = "1607196823",otp = generate_otp()):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": otp}
    response = requests.post(url, params)
    if response.ok:
        print("otp   sent successfully!")
    else:
        print(f"Failed to send message: {response.text}")
    return otp
def send_telegram_message(bot_token = "6914400012:AAGTZiJAoi2w_Q24QCidy3apONn0lcDJ_5E", chat_id = "1607196823",message="Do you want vedio to verify(type yes or no only)"):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(url, params)
    if response.ok:
        print("message sent sucessfully  sent successfully!")
    else:
        print(f"Failed to send message: {response.text}")
    
def send_telegram_photo(bot_token, chat_id, photo_path):
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    with open(photo_path, 'rb') as photo:
        files = {"photo": photo}
        params = {"chat_id": chat_id}
        response = requests.post(url, params=params, files=files)
        if response.ok:
            print("Photo sent successfully!")
        else:
            print(f"Failed to send photo: {response.text}")

def send_telegram_video(bot_token="6914400012:AAGTZiJAoi2w_Q24QCidy3apONn0lcDJ_5E", chat_id=1607196823, video_path="output_video.mp4"):
    url = f"https://api.telegram.org/bot{bot_token}/sendVideo"
    with open(video_path, 'rb') as video:
        files = {"video": video}
        params = {"chat_id": chat_id}
        response = requests.post(url, params=params, files=files)
        if response.ok:
            print("Video sent successfully!")
        else:
            print(f"Failed to send video: {response.text}")

def send_folder(bot_token="6914400012:AAGTZiJAoi2w_Q24QCidy3apONn0lcDJ_5E", chat_id=1607196823, folder_path="photos"):
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    photo_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]
    photo_files.sort()

    if not photo_files:
        print("No photos found in the folder.")
        return

    for photo_file in photo_files:
        photo_path = os.path.join(folder_path, photo_file)
        send_telegram_photo(bot_token, chat_id, photo_path)


def main(flag):
    if flag == 0:
        bot_token = "6914400012:AAGTZiJAoi2w_Q24QCidy3apONn0lcDJ_5E"
        chat_id = "1607196823"  # Replace this with your chat ID
        message = "Your message for flag 0"
        vedio_path="output_video.avi"
        list=get_last_message(bot_token)
        print(list)
        #send_telegram_message(bot_token, chat_id, message)
        #send_telegram_video(bot_token, chat_id,vedio_path)
    elif flag == 1:
        bot_token = "6914400012:AAGTZiJAoi2w_Q24QCidy3apONn0lcDJ_5E"
        chat_id = "1607196823"  # Replace this with your chat ID
        message = "Otp for enabling Interface: 1298\
                        System Under attack IP: 195.44.53.1"
        send_telegram_message(bot_token, chat_id, message)
    else:
        print("Invalid flag")

if __name__ == "__main__":
    flag = int(input("Enter flag (0 or 1): "))
    main(flag)
