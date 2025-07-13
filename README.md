
markdown
Copy
Edit
# 📡 TelegramTracker

**TelegramTracker** is a lightweight Python-based tool developed by **Mr Monsif** for collecting, analyzing, and processing data from Telegram.

## 📁 Project Structure

- `TeleGatherer.py` – Main intelligence-gathering module  
- `TeleTexter.py` – Script to send or spam messages to channels  
- `TeleTracker/` – Core features, modules, or UI logic  
- `helpers/` – Supporting scripts and utilities  
- `requirements.txt` – List of required Python libraries

## ⚙️ Installation

```bash
git clone https://github.com/monsifhmouri/TelegramTracker.git
cd TelegramTracker
pip install -r requirements.txt
🚀 Usage
To send a message to a Telegram channel:

bash
Copy
Edit
python TeleTexter.py -t YOUR_BOT_TOKEN -c YOUR_CHAT_ID -m "Your message here"
To gather intelligence:

bash
Copy
Edit
python TeleGatherer.py -t YOUR_BOT_TOKEN -c YOUR_CHAT_ID
🧠 Features
Download media (photos, videos, documents, etc.)

View and save messages in text and JSON

Send or spam messages to Telegram channels

Monitor and interact with malicious channels

Optional menu with MONITOR and DISRUPT functions

🧪 Coming Feature: TeleViewer.py
A new module allowing:

View and download all media

Filter messages by count or ID

Save all messages in both .txt and .json formats

To use TeleViewer.py, create a Telegram API and set your credentials in a .env file:

ini
Copy
Edit
API_ID="your_id"
API_HASH="your_hash"
Developed by Mr Monsif
