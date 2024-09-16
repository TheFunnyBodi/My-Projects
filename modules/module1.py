from googletrans import Translator, LANGUAGES

def TransLate(text, lang):
    if not text:
        return "Текст не може бути пустим!"

    translator = Translator()

    # Перетворення назви мови в код мови, якщо потрібно
    lang_code = next((code for code, name in LANGUAGES.items() if name.lower() == lang.lower()), lang.lower())

    if lang_code not in LANGUAGES:
        return "Мова або код не розпізнані!"

    try:
        translated = translator.translate(text, dest=lang_code).text
        return translated
    except Exception as e:
        return f"Помилка перекладу: {e}"

text = "Hello, whats up?"
lang = "uk"  # або "Ukrainian"
#print("Перекладений текст:", TransLate(text, lang))

import langid

def LangDetect(txt):
    if not txt:
        return "Текст не може бути пустим!"

    try:
        lang, confidence = langid.classify(txt)
        # Впевненість може бути від'ємною, перетворюємо її в абсолютне значення
        confidence_abs = abs(confidence)
        return f"Мова: {lang}, Впевненість: {confidence_abs:.2f}"
    except Exception as e:
        return f"Помилка визначення мови: {e}"

text_for_detection = "Hello, whats up?"
#print("Визначення мови:", LangDetect(text_for_detection))

from googletrans import LANGUAGES

def CodeLang(lang):
    if not lang:
        return "Введіть мову або код мови"

    lang = lang.lower()

    # Перевірка, чи `lang` э кодом мови
    if lang in LANGUAGES:
        return LANGUAGES[lang]

    # Перевірка, чи `lang` э назвою мови
    lang_code = next((code for code, name in LANGUAGES.items() if name.lower() == lang), None)
    if lang_code:
        return lang_code

    return "Помилка: мова або код не розпізнані"

#print("Код мови для 'Ukrainian':", CodeLang("Ukrainian"))
#print("Назва мови для 'uk':", CodeLang("uk"))


from googletrans import Translator, LANGUAGES

def LanguageList(out="screen", text=None):
    try:
        translator = Translator()

        headers = ["N", "Language", "ISO-639 code"]
        if text:
            headers.append("Text")

        # Збірка даних для таблиці
        rows = []
        for i, (lang_code, lang_name) in enumerate(LANGUAGES.items(), 1):
            row = [str(i), lang_name.capitalize(), lang_code]
            if text:
                try:
                    translated_text = translator.translate(text, dest=lang_code).text
                    row.append(translated_text)
                except Exception as e:
                    row.append(f"Помилка перекладу: {e}")
            rows.append(row)

        # Форматування таблиці
        table = []
        table.append("{:<4} {:<15} {:<10} {}".format(*headers))
        table.append("-" * 50)
        for row in rows:
            table.append("{:<4} {:<15} {:<10} {}".format(*row))

        # Виведення на екран
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
#print(LanguageList("file", "Hello, whats up?"))

