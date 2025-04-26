import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

LANGUAGES = {
    "English": "en",
    "Korean": "ko",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Japanese": "ja",
    "Russian": "ru",
    "Arabic": "ar",
    "Hindi": "hi",
    "Bengali": "bn",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Swedish": "sv",
    "Danish": "da",
    "Finnish": "fi",
    "Norwegian": "no",
    "Polish": "pl",
    "Czech": "cs",
    "Hungarian": "hu",
    "Romanian": "ro",
    "Thai": "th",
    "Indonesian": "id",
    "Vietnamese": "vi",
    "Hebrew": "iw",
    "Malay": "ms",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Punjabi": "pa",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Urdu": "ur",
    "Swahili": "sw",
    "Filipino": "tl",
    "Ukrainian": "uk",
    "Persian": "fa",
    "Bulgarian": "bg",
    "Slovak": "sk",
    "Croatian": "hr",
    "Serbian": "sr",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Estonian": "et",
    "Slovenian": "sl",
    "Macedonian": "mk",
    "Icelandic": "is",
    "Georgian": "ka",
    "Armenian": "hy",
    "Basque": "eu",
    "Catalan": "ca",
    "Galician": "gl",
    "Albanian": "sq",
    "Bosnian": "bs",
    "Malagasy": "mg",
    "Haitian Creole": "ht",
    "Sinhala": "si",
    "Nepali": "ne",
    "Khmer": "km",
    "Lao": "lo",
    "Mongolian": "mn",
    "Somali": "so",
    "Xhosa": "xh",
    "Zulu": "zu",
    "Javanese": "jw",
    "Myanmar (Burmese)": "my",
    "Pashto": "ps",
    "Kazakh": "kk",
    "Uzbek": "uz",
    "Azerbaijani": "az",
    "Tatar": "tt",
    "Turkmen": "tk",
    "Tigrinya": "ti",
    "Sesotho": "st",
    "Maltese": "mt"
}


def setup_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--log-level=3')
    return webdriver.Chrome(options=options)

def open_translator(driver, target_lang):
    url = f"https://translate.google.com/?sl=en&tl={target_lang}&op=translate"
    driver.get(url)
    time.sleep(2)

def translate(driver, text):
    textarea = driver.find_element(By.TAG_NAME, "textarea")
    textarea.clear()
    textarea.send_keys(text)
    time.sleep(2.5)  # Reduced time — works reliably in most cases

    for _ in range(5):  # Try to wait for translation to appear
        try:
            result = driver.find_element(By.CSS_SELECTOR, 'span[jsname="W297wb"]').text
            if result:
                return result
        except:
            pass
        time.sleep(1)

    return text  # Fallback

def process_json(input_file, output_file, target_language):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    translated = {"@@locale": target_language}
    driver = setup_driver()
    open_translator(driver, target_language)
    for key, value in data.items():
        if key == '@@locale':
            continue
        print(f"🔄 Translating [{key}]...")
        translated_value = translate(driver, value)
        translated[key] = translated_value
        print(f"✅ {value} ➜ {translated_value}")

    driver.quit()

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Translation complete. Saved to: {output_file}")

def list_languages():
    print("Available languages:")
    for idx, (lang_name, lang_code) in enumerate(LANGUAGES.items(), start=1):
        print(f"{idx}. {lang_name} ({lang_code})")

def get_language_code(language_index):
    return list(LANGUAGES.values())[language_index - 1]

if __name__ == "__main__":
    list_languages()
    language_index = int(input("\nSelect the language number: "))

    if language_index < 1 or language_index > len(LANGUAGES):
        print("Invalid selection.")
        exit()

    target_language = get_language_code(language_index)
    input_file = input("Enter input JSON path (eg : input.json): ")
    output_file = input("Enter output JSON path (eg : output.json): ")
    process_json(input_file, output_file, target_language)
