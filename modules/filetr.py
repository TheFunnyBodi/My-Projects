import json
import re
from googletrans import Translator

def load_config(config_file):
    with open(config_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_text(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return f.read()

def write_text(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    segments = re.split(r'(\s+|[\.\!\?\,\:\;])', text)
    translated_segments = []

    for segment in segments:
        if segment.strip() and not re.match(r'[\s\.\!\?\,\:\;]', segment):
            translation = translator.translate(segment.strip(), src=source_lang, dest=target_lang)
            translated_segments.append(translation.text)
        else:
            translated_segments.append(segment)

    return ''.join(translated_segments)

def main():
    config = load_config('config.json')
    text = read_text(config['text_file'])
    translated_text = translate_text(text, config['source_language'], config['target_language'])
    write_text(config['output_file'], translated_text)

    print("Переклад завершено. Перекладений текст збережено у", config['output_file'])

if __name__ == "__main__":
    main()

