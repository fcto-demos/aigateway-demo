import os
import yaml

_LOCALES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "locales")
_translations: dict = {}
_current_lang = "en"


def _load_locales():
    if not os.path.isdir(_LOCALES_DIR):
        return
    for code in os.listdir(_LOCALES_DIR):
        path = os.path.join(_LOCALES_DIR, code, "translations.yaml")
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as f:
                _translations[code] = yaml.safe_load(f)


_load_locales()


def available_languages() -> dict:
    """Return {lang_code: display_name} for all discovered locale packs."""
    return {code: data.get("language_name", code) for code, data in _translations.items()}


def get_prompts(lang: str, fallback_order: list = None) -> list:
    """Load prompts for lang, falling back through fallback_order then 'en'."""
    candidates = [lang] + (fallback_order or []) + ["en"]
    seen = []
    for code in candidates:
        if code in seen:
            continue
        seen.append(code)
        path = os.path.join(_LOCALES_DIR, code, "prompts.yaml")
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as f:
                return yaml.safe_load(f)["prompts"]
    return []


def set_lang(lang: str):
    global _current_lang
    if lang in _translations:
        _current_lang = lang
    else:
        _current_lang = "en"


def get_lang() -> str:
    return _current_lang


def t(key: str, **kwargs) -> str:
    txt = _translations.get(_current_lang, _translations.get("en", {})).get(key, key)
    return txt.format(**kwargs) if kwargs else txt
