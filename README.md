## Binance Telegram Delist Alert

This project aims to keep track of Binance's delisting schedule through its API and send timely alerts to a designated Telegram chat.

---

## Features

- Monitors Binance's delisting schedule
- Sends alerts via Telegram bot
- Tracks previously seen symbols to prevent duplicate notifications

---

## Requirements

- Python 3.x
- `telepot` library
- `requests` library
- `configparser` library

---

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Abenchioui/binance-telegram-delist-alert.git
    cd binance-telegram-delist-alert
    ```

2. **Install dependencies**:

    ```bash
    pip install telepot requests configparser
    ```

3. **Configuration**:

    - Create a `config.ini` file in the root directory.
    - Add your Telegram bot token and chat ID:

    ```ini
    [Telegram]
    bot_token = YOUR_TELEGRAM_BOT_TOKEN
    my_chat_id = YOUR_TELEGRAM_CHAT_ID
    ```

4. **Run the script**:

    ```bash
    python _delist.py
    ```

---

## How It Works

- The script runs checks on Binance's delisting schedule continuously.
- It formats and sends messages to the specified Telegram chat in case of new delistings.
- It waits for an hour before performing the next check.

---

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute to this project!

---

## License

This project is licensed under the MIT License.
