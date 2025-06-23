import requests, threading, time
from colorama import Fore, Style, init
from itertools import cycle

url = "https://raw.githubusercontent.com/AirdropScriptFA/airdrop/main/api.json"
response = requests.get(url)
print(Fore.CYAN + Style.BRIGHT + (response.text))

init(autoreset=True)

BASE = "https://api.openloop.so"

def load_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_proxy_dict(proxy_str):
    if not proxy_str: return None
    return {
        "http": proxy_str,
        "https": proxy_str
    }

def run_client(token, proxy_str, index):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    proxies = get_proxy_dict(proxy_str)

    def share_bandwidth():
        while True:
            try:
                r = requests.post(f"{BASE}/bandwidth/share", headers=headers, json={"quality": 87}, proxies=proxies, timeout=15)
                if r.status_code == 200:
                    print(Fore.GREEN + Style.BRIGHT + f"[{index}] ✓ Share Success")
                else:
                    msg = r.json().get("message", "Unknown")
                    print(Fore.GREEN + Style.BRIGHT + f"[{index}] ✗ Share In Dilema: {msg}")
            except Exception as e:
                print(Fore.RED + Style.BRIGHT + f"[{index}] ✗ Share Error: {e}")
            time.sleep(20)

    def fetch_info():
        while True:
            try:
                print(Fore.CYAN + Style.BRIGHT + f"\n[{index}] 🌟 PROFILE")
                res = requests.get(f"{BASE}/users/profile", headers=headers, proxies=proxies, timeout=15).json()
                user = res.get("data", {})
                print(Fore.YELLOW + Style.BRIGHT + f"👤 Username: {user.get('name')} | 📧 Email: {user.get('username')} | 🎟️ Reff: {user.get('inviteCode')}")

                print(Fore.CYAN + Style.BRIGHT + f"\n[{index}] 📊 BANDWIDTH")
                res = requests.get(f"{BASE}/bandwidth/info", headers=headers, proxies=proxies, timeout=15).json()
                data = res.get("data", {})
                print(Fore.GREEN + Style.BRIGHT + f"💰 Earnings: {data.get('todayEarning')} | 🏦 Points: {data.get('balances', {}).get('POINT')}")

                print(Fore.CYAN + Style.BRIGHT + f"\n[{index}] 🖼️ SLIDES")
                res = requests.get(f"{BASE}/slides/configs", headers=headers, proxies=proxies, timeout=15).json()
                for slide in res.get("data", []):
                    print(Fore.MAGENTA + Style.BRIGHT + f"🌐 {slide.get('link')} | 🖼️ {slide.get('imageUrl')}")

            except Exception as e:
                print(Fore.RED + f"[{index}] ✗ Fetch Error: {e}")
            time.sleep(120)

    # Start Threads
    threading.Thread(target=share_bandwidth, daemon=True).start()
    threading.Thread(target=fetch_info, daemon=True).start()

# === Main Runner ===
if __name__ == "__main__":
    tokens = load_lines("token.txt")
    proxies = load_lines("proxy.txt")
    max_len = max(len(tokens), len(proxies))
    tokens += [None] * (max_len - len(tokens))  # pad if needed
    proxies += [None] * (max_len - len(proxies))

    print(Fore.CYAN + Style.BRIGHT + f"🚀 Starting {len(tokens)} OpenLoop Bot...\n")
    for i, (token, proxy) in enumerate(zip(tokens, proxies), start=1):
        if not token:
            print(Fore.RED + f"[{i}] ⚠️ Skipping empty token.")
            continue
        threading.Thread(target=run_client, args=(token, proxy, i), daemon=True).start()

    while True:
        time.sleep(999)  # Keep main thread alive
