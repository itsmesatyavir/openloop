# OpenLoop

OpenLoop is a multi-account automation tool for validating and checking user data from the OpenLoop platform. It supports multiple tokens, optional proxy rotation, and parallel execution using threading.

## 🔧 Features

- ✅ Supports multiple tokens from `token.txt`
- 🌍 Optional proxy support from `proxy.txt` (HTTP, SOCKS4, SOCKS5)
- 🚀 Fast threaded execution for parallel processing
- 📋 Displays account information such as:
  - Name
  - Username
  - Invite Code
  - Points
- 🔁 Rotates proxies and tokens automatically
- 🎨 Colored terminal output using `colorama`

## 📁 File Structure

| File         | Description                               |
|--------------|-------------------------------------------|
| `main.py`    | Main script for validating and checking   |
| `token.txt`  | Add one token per line                    |
| `proxy.txt`  | (Optional) Add one proxy per line         |
| `LICENSE`    | License file (MIT)                        |
| `README.md`  | This documentation                        |

## 🚀 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/itsmesatyavir/openloop
cd openloop
```

2. **Install dependencies:**

```bash
pip install requests colorama
```

## ✍️ Setup

- **Add your tokens** in (one per line.)
```
token.txt
```
- **(Optional)** Add proxies in
```bash
proxy.txt
```
formats:
  ```
  http://user:pass@host:port
  socks4://host:port
  socks5://user:pass@host:port
  ```

## ▶️ Usage

```bash
python main.py
```

## 📊 Output

For each token, you’ll see:

- ✅ Success or ❌ Error
- 🧑 Name and username
- 🏷️ Referral code
- 💰 Points
- 🌐 Proxy used (or not used)

## 📝 License

This project is licensed under the [MIT License](./LICENSE).

---

Built with ❤️ by [itsmesatyavir](https://github.com/itsmesatyavir)
