from .tokenizer import AfaanOromooTokenizer
from .stopword_remover import StopwordRemover
from .stemmer import AfaanOromooStemmer
from .special_char_handler import SpecialCharacterHandler


class PreprocessingPipeline:
    """
    Afaan Oromoo Text Preprocessing Pipeline

    This class integrates the application of varios preprocessing steps on Afaan Oromoo text,

    Methods:
        - preprocess(text): Applies the preprocessing steps to the input text.

    Example:
     >>> pipeline = PreprocessingPipeline()
     >>> preprocessed_text = pipeline.preprocess("Garaan mataa caalti.")
     >>> print(preprocessed_text)
     "garaa mataa caal"
    """

    def __init__(self, stopwords=None):
        """
        Initialize the PreprocessingPipeline

        Parameters:
         - stopwrods (set)L A set of stop words. If not provided, default stopwords will be used.
        """
        self.tokenizer = AfaanOromooTokenizer()
        self.stopword_remover = StopwordRemover(stopwords)
        self.stemmer = AfaanOromooStemmer()
        self.special_char_handler = SpecialCharacterHandler()

    def process(self, text: str, stem: bool = False) -> str:
        """
        Apply the preprocessing steps to the input text.

        Parameters:
         - text (str): The input text to be prepocessed

        Returns:
         - str: The preprocessed text.
        """
        # Step 1: Case Normalization
        
        text = text.lower()
        # Step 2: Tokenize
        tokens = self.tokenizer.tokenize(text)

        # Step 3: Remove stopwrods
        tokens = self.stopword_remover.remove_stopwords(
            tokens)

        # Step 4: Stemming (If required)
        tokens = [self.stemmer.stem(token)
                          for token in tokens] if stem else tokens

        # Step 5: Join back and return
        preprocessed_text = " ".join(tokens)

        return preprocessed_text
    
if __name__ == "__main__":
    pipeline = PreprocessingPipeline()
    preprocessed_text = pipeline.process("Garaan mataa caalti.")
    print(preprocessed_text)