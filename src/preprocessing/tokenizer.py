import re
import unicodedata
from nltk import word_tokenize
from typing import List


class AfaanOromooTokenizer:
    """
    Afaan Oromoo tokenizer

    Usage:
        >>> tokenizer = AfaanOromooTokenizer()
        >>> tokenizer.tokenize("Akkam Akkam")
    """

    def __init__(self):
        # Handle accents and variations
        # TODO: Add More replacements later
        self.replacements = {r"\bkh\b": "k",
                             r"\b(\w*)['’](\w*)\b": "h"}

    def word_tokenize(self, text: str) -> List[str]:
        return word_tokenize(text)

    def sentence_tokenize(self, text: str) -> List[str]:
        sentences = re.split(r'\.', text)
        sentences = [sentence.strip() for sentence in sentences]
        return sentences

    def tokenize_with_punctuation(self, text: str) -> List[str]:
        tokens = re.findall(r'\b\w+\b|\S', text)
        return tokens

    def normalize(self, text: str) -> str:
        # Apply replacements
        for pattern, replacement in self.replacements.items():
            pattern = re.compile(pattern)
            text = pattern.sub(replacement, text)

        normalized_text = unicodedata.normalize(
            'NFKD', text).encode('ASCII', 'ignore').decode('utf-8')
        return normalized_text

    def tokenize(self, text: str) -> List[str]:
        normalized_text = self.normalize(text)
        return self.word_tokenize(normalized_text)
