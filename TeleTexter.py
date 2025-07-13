import argparse
import requests
import time

def send_message(bot_token, chat_id, message, spam=False):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    
    if spam:
        print("[*] Sending messages repeatedly... Press Ctrl+C to stop.")
        try:
            while True:
                response = requests.post(url, data=payload)
                print(f"[+] Sent: {message} (Status: {response.status_code})")
                time.sleep(1.5)
        except KeyboardInterrupt:
            print("\n[!] Stopped spam mode.")
    else:
        response = requests.post(url, data=payload)
        print(f"[+] Sent: {message} (Status: {response.status_code})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a Telegram message via bot")
    parser.add_argument("-t", "--token", required=True, help="Bot token")
    parser.add_argument("-c", "--chat_id", required=True, help="Chat ID")
    parser.add_argument("-m", "--message", required=True, help="Message text")
    parser.add_argument("--spam", action="store_true", help="Send message repeatedly")
    args = parser.parse_args()

    send_message(args.token, args.chat_id, args.message, args.spam)
