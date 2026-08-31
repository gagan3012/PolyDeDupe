import re

NON_ALPHA = re.compile(
    "[^"
    "\u0080-\u00ff"  # Latin-1 Supplement (covers many Western European languages)
    "\u0100-\u017f"  # Latin Extended-A (Central European, Baltic, etc.)
    "\u0180-\u024f"  # Latin Extended-B (additional European languages)
    "\u1e00-\u1eff"  # Latin Extended Additional (covers Vietnamese, some African languages)
    "\u0400-\u04ff"  # Cyrillic (covers Russian, Bulgarian, Serbian, etc.)
    "\u0370-\u03ff"  # Greek and Coptic
    "\u1f00-\u1fff"  # Greek Extended
    # Including your original ranges
    "\u0600-\u06ff"  # Arabic
    "\u07c0-\u07ff"  # N'Ko
    "\u0900-\u097f"  # Devanagari (Hindi, Marathi, Sanskrit)
    "\u1200-\u137f"  # Ethiopic (Amharic, Tigrinya)
    "\u2d30-\u2d7f"  # Tifinagh (Berber languages)
    "\ua500-\ua63f"  # Vai (West African)
    # Additional language ranges
    "\u4e00-\u9fff"  # CJK Unified Ideographs (Chinese)
    "\uac00-\ud7af"  # Hangul Syllables (Korean)
    "\u3040-\u309f\u30a0-\u30ff"  # Hiragana and Katakana (Japanese)
    "\u0b80-\u0bff"  # Tamil
    "\u0c00-\u0c7f"  # Telugu
    "\u0c80-\u0cff"  # Kannada
    "\u0d00-\u0d7f"  # Malayalam
    "\u0980-\u09ff"  # Bengali
    "\u0a00-\u0a7f"  # Gurmukhi (Punjabi)
    "\u0a80-\u0aff"  # Gujarati
    "\u0b00-\u0b7f"  # Oriya
    "\u0750-\u077f"  # Arabic Supplement
    "A-Za-z_0-9"  # General Latin, numerals, and underscore
    "]"
)
