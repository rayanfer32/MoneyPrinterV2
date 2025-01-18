from cache import get_accounts
from classes.YouTube import YouTube
import os
import sys
from classes.Tts import TTS
from utils import rem_temp_files

import requests

ROOT_DIR = os.path.dirname(sys.path[0])


def send_document_to_telegram(bot_token, chat_id, file_path):
    """Sends a document to a Telegram chat.

    Args:
        bot_token: Your Telegram bot token.
        chat_id: The ID of the Telegram chat.
        file_path: The path to the document file.
    """

    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    files = {"document": open(file_path, "rb")}
    data = {"chat_id": chat_id}

    try:
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error sending document: {e}")


from config import get_config

_config = get_config()
bot_token = _config["bot_token"]  # renderizer_bot
chat_id = _config["chat_id"]
# file_path = "/content/.mp/fb7de757-567f-48c5-9ad3-958b40a51f8f.mp4"  # Replace with the actual path to your file

if __name__ == "__main__":
    accounts = get_accounts("youtube")
    selected_account = accounts[0]
    youtube = YouTube(
        selected_account["id"],
        selected_account["nickname"],
        selected_account["firefox_profile"],
        selected_account["niche"],
        selected_account["language"],
    )
    tts = TTS()

    use_cached = False
    if use_cached:
        # * use cached audio transcript
        youtube.tts_path = os.path.join(
            ROOT_DIR, ".mp", str("07b8d899-155a-425f-b570-80a88b391b6f") + ".wav"
        )  #'80941ef4-817d-4be9-a3d0-23cedfaa7266.wav'

        # * use cached images, get all png files in .mp folder
        cached_images = [
            os.path.join(ROOT_DIR, ".mp", file)
            for file in os.listdir(os.path.join(ROOT_DIR, ".mp"))
            if file.endswith(".png")
        ]
        youtube.images = cached_images
        path = youtube.combine()
    else:
        # * run from scratch
        rem_temp_files()
        path = youtube.generate_video(tts)

    print("Generated Video path:", path)
    send_document_to_telegram(bot_token, chat_id, path)
