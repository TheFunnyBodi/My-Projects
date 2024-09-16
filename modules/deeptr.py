import module2

def module2_functions():
    print("Демонстрація роботи функцій пакету з другого модуля:")
    # Виклик функції TransLate
    print("Демонстрація функції TransLate:")
    text_to_translate = "Hello, whats up?"
    target_language = "uk"  # або "Ukrainian"
    translated_text = module2.TransLate(text_to_translate, target_language)
    print(f"Перекладений текст: {translated_text}")

    # Виклик функції LangDetect
    print("\nДемонстрація функції LangDetect:")
    text_for_detection = "Hello, whats up?"
    detected_language = module2.LangDetect(text_for_detection)
    print(f"Визначення мови: {detected_language}")

    # Виклик функції CodeLang
    print("\nДемонстрація функції CodeLang:")
    # Перевіряємо код мови за назвою
    language_name = "Ukrainian"
    lang_code = module2.CodeLang(language_name)
    print(f"Код мови для '{language_name}': {lang_code}")
    # Перевіряємо назву мови за кодом
    language_code = "uk"
    language_name_from_code = module2.CodeLang(language_code)
    print(f"Назва мови для '{language_code}': {language_name_from_code}")

    # Виклик функції LanguageList
    print("\nДемонстрація функції LanguageList:")
    module2.LanguageList(out="screen", text=text_to_translate)
    print("\nOk")

# Викликаємо функцію для демонстрації всіх функцій
if __name__ == "__main__":
    module2_functions()

