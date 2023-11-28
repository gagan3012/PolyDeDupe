import re

NON_ALPHA = re.compile(
    "[^"
    "\u0080-\u00FF"  # Latin-1 Supplement (covers many Western European languages)
    "\u0100-\u017F"  # Latin Extended-A (Central European, Baltic, etc.)
    "\u0180-\u024F"  # Latin Extended-B (additional European languages)
    "\u1E00-\u1EFF"  # Latin Extended Additional (covers Vietnamese, some African languages)
    "\u0400-\u04FF"  # Cyrillic (covers Russian, Bulgarian, Serbian, etc.)
    "\u0370-\u03FF"  # Greek and Coptic
    "\u1F00-\u1FFF"  # Greek Extended
    # Including your original ranges
    "\u0600-\u06FF"  # Arabic
    "\u07C0-\u07FF"  # N'Ko
    "\u0900-\u097F"  # Devanagari (Hindi, Marathi, Sanskrit)
    "\u1200-\u137F"  # Ethiopic (Amharic, Tigrinya)
    "\u2D30-\u2D7F"  # Tifinagh (Berber languages)
    "\uA500-\uA63F"  # Vai (West African)
    # Additional language ranges
    "\u4E00-\u9FFF"  # CJK Unified Ideographs (Chinese)
    "\uAC00-\uD7AF"  # Hangul Syllables (Korean)
    "\u3040-\u309F\u30A0-\u30FF"  # Hiragana and Katakana (Japanese)
    "\u0B80-\u0BFF"  # Tamil
    "\u0C00-\u0C7F"  # Telugu
    "\u0C80-\u0CFF"  # Kannada
    "\u0D00-\u0D7F"  # Malayalam
    "\u0980-\u09FF"  # Bengali
    "\u0A00-\u0A7F"  # Gurmukhi (Punjabi)
    "\u0A80-\u0AFF"  # Gujarati
    "\u0B00-\u0B7F"  # Oriya
    "\u0750-\u077F"  # Arabic Supplement
    "A-Za-z_0-9"  # General Latin, numerals, and underscore
    "]"
)
