# 🌐 JSON Translator using Selenium and Google Translate

This project allows you to **automatically translate the contents of a JSON file** from English to any supported language using Google Translate through **Selenium and ChromeDriver**.

---

## 🚀 Features

- Translates all string values in a JSON file.
- Supports 75+ languages.
- No API keys or third-party services required.
- Fully automated using Selenium.
- CLI language selection.
- Headless Chrome support.

---

## 📦 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
  - Download from: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
- pip (Python package manager)

---

## 🔧 Installation

1. **Clone the repository:**

```
git clone https://github.com/your-username/json-translator.git
cd json-translator
```

```
pip install -r requirements.txt
```

```
json-translator/
│
├── translate_json.py       # Main script to run
├── languages.json          # (optional) Language code map
├── input.json              # Your source JSON (example)
├── output.json             # Output translated file
├── requirements.txt        # Python dependencies
└── README.md               # You're here!
```

{
"@@locale": "en",
"greeting": "Hello",
"farewell": "Goodbye"
}

```
python translate_json.py
```

```

```
