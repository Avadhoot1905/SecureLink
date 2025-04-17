# 🔒 SecureLink

**SecureLink** is a terminal-based, real-time LAN messaging application that uses **UDP broadcast** to send and receive messages across devices connected to the same router. It's a lightweight and cross-platform alternative for local chat — no servers required!

---

## 📦 Features

- 🧠 Real-time messaging
- 🖥 Works across Windows, Linux, and macOS
- 🌐 Uses UDP broadcast for efficient LAN communication
- 🔁 Both sender and receiver run simultaneously
- 🚪 Gracefully exits with `exit` command

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on all systems
- All devices connected to the **same local network/router**
- Basic command-line knowledge

---

### 📥 Installation

Clone or download this repository on all systems you want to connect:

```bash
git clone https://github.com/yourusername/securelink.git
cd securelink
```

---

### 🛠 Usage

Run the app from the terminal:

```bash
python securelink.py
```

Start typing messages and hit **Enter** to send. Messages will appear on all devices running SecureLink on the same network.

Type `exit` to leave the chat cleanly.

---

## 🧪 Sample Screenshot

```bash
🔒 SecureLink 
Type messages below. Type 'exit' to quit.

> hey!
[192.168.1.12] hey!
> how are you?
[192.168.1.13] I'm good! You?
```

---

## 🧠 How It Works

SecureLink uses **UDP broadcast** to send messages to the IP `224.0.0.1` on port `5005`. All clients join this multicast group and listen for messages, making it ideal for LAN-only communication.

---

## ⚠️ Troubleshooting

- Make sure **firewalls** allow inbound/outbound UDP traffic on **port 5005**
- Devices must be on the **same subnet** (e.g., `192.168.1.X`)
- Try **disabling VPNs** if messages aren't visible
- Check for **Wi-Fi router settings** that may block broadcast

---

## 🛡 Planned Features (Optional Ideas)

- Nicknames/usernames
- Message timestamps
- Encrypted messaging (AES)
- File sharing support
- Terminal UI using `rich` or `curses`
