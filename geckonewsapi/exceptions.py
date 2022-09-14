class InvalidLanguage(Exception):
    langs = {'en': 'English', 'de': 'Deutsch', 'es': 'Español', 'fr': 'Français', 'it': 'Italiano', 'pl': 'język polski', 'ro': 'Limba română', 'hu': 'Magyar nyelv', 'nl': 'Nederlands', 'pt': 'Português', 'sv': 'Svenska', 'vi': 'Tiếng việt', 'tr': 'Türkçe', 'ru': 'Русский', 'ja': '日本語', 'zh': '繁體中文', 'ko': '한국어', 'ar': 'العربية', 'th': 'ภาษาไทย', 'id': 'Bahasa Indonesia', 'cs': 'čeština', 'da': 'dansk', 'el': 'Ελληνικά', 'hi': 'हिंदी', 'no': 'norsk', 'sk': 'slovenský jazyk', 'uk': 'украї́нська мо́ва', 'he': 'עִבְרִית', 'fi': 'suomen kieli', 'bg': 'български', 'hr': 'hrvatski', 'lt': 'lietuvių kalba', 'sl': 'slovenski jezik'}

    def __init__(self, lang):
        self.lang = lang

    def __str__(self):
        string = f'{self.lang} is not in available lang codes: \n'
        for code, name in self.langs.items():
            string += f'{name}: {code}\n'

        return string

class InvalidPage(Exception):
    def __init__(self, page):
        self.page = page

    def __str__(self):
        return f'Page must be >= 1, recived {self.page}'

class MaxRetries(Exception):
    def __str__(self):
        return f'Maximum number of retries reached'
