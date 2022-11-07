from loguru import logger

strings = {
    "en": {},
    "ru":{}
}

def get_string(key: str, language: int) -> str:
    """Get localized string.
    First, try language as set in db or user variable.
    Then, try English locale.
    Else - raise an exception.

    Args:
        key (str): string name.
        language (str | int): code language.

    Raises:
        KeyError: if "en" and :language: locales are not found.

    Returns:
        str: localized string
    """    
    
    lang = strings.get(language)

    if not lang:
        if not strings.get("en"):
            raise KeyError(f"Neither \"{language}\" nor \"en\" locales found")
        else:
            lang = strings.get("en")
    try:
        return lang[key]
    except KeyError as e:
        logger.error(e)
        try:
            return strings.get("en")[key]
        except Exception:
            raise