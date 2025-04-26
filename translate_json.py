import json
import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Dictionary of supported languages with their language codes
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
    "Thai": "th",
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
    "Punjabi": "pa",
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
    "Burmese": "my",
    "Maltese": "mt"
}


def translate(text, driver, target_lang='ko'):
    driver.get(f"https://translate.google.com/?sl=en&tl={target_lang}&op=translate")
    time.sleep(2)
    textarea = driver.find_element(By.TAG_NAME, "textarea")
    textarea.clear()
    textarea.send_keys(text)
    time.sleep(3)

    try:
        translated = driver.find_element(By.CSS_SELECTOR, 'span[jsname="W297wb"]').text
        return translated
    except:
        return text

def process_json(input_file, output_file, target_language):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    translated = {"@@locale": target_language}

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    for key, value in data.items():
        if key == '@@locale':
            continue
        print(f"🔄 Translating [{key}]...")
        translated_value = translate(value, driver, target_language)
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
    lang_list = list(LANGUAGES.values())
    return lang_list[language_index - 1]

if __name__ == "__main__":
    # Show available languages and ask user to select a language
    list_languages()
    language_index = int(input("\nPlease select the number corresponding to the language you want to translate to: "))

    # Validate the input
    if language_index < 1 or language_index > len(LANGUAGES):
        print("Invalid selection, exiting...")
        exit()

    target_language = get_language_code(language_index)

    # Ask for input and output JSON file paths
    input_file = input("Enter the input JSON file path (e.g., input.json): ")
    output_file = input("Enter the output JSON file path (e.g., output.json): ")

    # Start the translation process
    process_json(input_file, output_file, target_language)
