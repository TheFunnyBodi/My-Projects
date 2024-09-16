from deep_translator import GoogleTranslator

def TransLate(text, lang):
    if not text:
        return "Текст не може бути пустим!"

    try:
        translated = GoogleTranslator(source='auto', target=lang).translate(text)
        return translated
    except Exception as e:
        return f"Помилка перекладу: {e}"

text = "Hello, whats up?"
lang = "uk"  # або "Ukrainian"
#print("Перекладений текст:", TransLate(text, lang))

from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def LangDetect(txt):
    if not txt:
        return "Текст не може бути пустим!"

    try:
        lang = detect(txt)
        return f"Мова: {lang}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

text_for_detection = "Hello, whats up?"
#print("Визначення мови:", LangDetect(text_for_detection))


from deep_translator import GoogleTranslator

def CodeLang(lang):
    if not lang:
        return "Введіть мову або код мови"

    try:
        lang_code = GoogleTranslator().get_supported_languages(as_dict=True)
        lang_lower = lang.lower()

        if lang_lower in [name.lower() for name in lang_code.values()]:
            # Якщо введено назву мови
            return [code for code, name in lang_code.items() if name.lower() == lang_lower][0]
        elif lang_lower in lang_code:
            # Якщо введено код мови
            return lang_code[lang_lower]
        else:
            return "Помилка: мова або код не розпізнані"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

#print("Код мови для 'Ukrainian':", CodeLang("Ukrainian"))
#print("Назва мови для 'uk':", CodeLang("uk"))

from deep_translator import GoogleTranslator

def LanguageList(out="screen", text=None):
    try:
        translator = GoogleTranslator(source='auto', target='en')
        lang_dict = translator.get_supported_languages(as_dict=True)
        headers = ["N", "Language", "ISO-639 code", "Text"] if text else ["N", "Language", "ISO-639 code"]

        # Збірка даних для таблиці
        rows = []
        for i, (lang_name, lang_code) in enumerate(lang_dict.items(), 1):
            row = [str(i), lang_name.capitalize(), lang_code]
            if text:
                try:
                    translated_text = GoogleTranslator(source='auto', target=lang_code).translate(text)
                    row.append(translated_text)
                except Exception as e:
                    row.append(f"Помилка перекладу: {e}")
            rows.append(row)

        # Форматування таблиці
        table = []
        table.append("{:<4} {:<20} {:<10} {}".format(*headers))
        table.append("-" * 50)
        for row in rows:
            table.append("{:<4} {:<20} {:<10} {}".format(*row))

        # Виведення на екран або у файл, якщо треба
        if out == "screen":
            for line in table:
                print(line)
        elif out == "file":
            with open("languages_table.txt", "w", encoding="utf-8") as f:
                for line in table:
                    f.write(line + "\n")
        else:
            return "Невідомий параметр!"

        return "Ok"

    except Exception as e:
        return f"Сталася помилка: {e}"

#print(LanguageList("screen", "Hello, whats up?"))


