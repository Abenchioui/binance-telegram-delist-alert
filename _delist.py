import configparser
import telepot
import time
import requests
from urllib.parse import urlencode
from binance_client import Pkey
from datetime import datetime

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

telegram_bot_token = config['Telegram']['bot_token']
telegram_chat_id = config['Telegram']['my_chat_id']

# Initialize Telegram bot
bot = telepot.Bot(telegram_bot_token)

# Binance API base URL
BASE_URL = "https://api.binance.com"

def get_timestamp():
    return int(time.time() * 1000)

def dispatch_request(url):
    session = requests.Session()
    session.headers.update(
        {"Content-Type": "application/json;charset=utf-8", "X-MBX-APIKEY": Pkey}
    )
    return session.get(url)

def send_public_request(url_path, payload={}):
    query_string = urlencode(payload, True)
    url = BASE_URL + url_path
    if query_string:
        url = url + "?" + query_string
    response = dispatch_request(url)
    return response.json()

def convert_timestamp(timestamp):
    dt_object = datetime.fromtimestamp(timestamp / 1000)
    return dt_object.strftime('%Y-%m-%d %H:%M:%S')

# Set to keep track of previously sent symbols
seen_symbols = set()

while True:
    try:
        # Fetch the response from Binance API
        response = send_public_request("/sapi/v1/spot/delist-schedule", {"timestamp": get_timestamp()})

        new_entries = []
        for entry in response:
            symbols = set(entry['symbols'])  # Convert list of symbols to a set for easy comparison
            if not symbols.issubset(seen_symbols):  # Check if there are new symbols
                new_entries.append(entry)
                seen_symbols.update(symbols)  # Add new symbols to the set

        if new_entries:
            for entry in new_entries:
                delist_time = convert_timestamp(entry['delistTime'])
                symbols = ', '.join([f"#{symbol}" for symbol in entry['symbols']])
                message = (
                        "🚨🚨🚨🚨🚨\n"
                        f"𝐃𝐞𝐥𝐢𝐬𝐭 𝐓𝐢𝐦𝐞: **{delist_time}**\n"
                        f"𝐒𝐲𝐦𝐛𝐨𝐥𝐬: {symbols}"
                        )
                bot.sendMessage(telegram_chat_id, message, parse_mode='Markdown')
                print(message)

    except Exception as e:
        print(f"An error occurred: {e}")

    # Wait for a hour before checking again
    time.sleep(3600)
