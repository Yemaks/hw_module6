
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_lg')
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

punctuations = '!"#$%&\'()*+,-/:;<=>?@[\\]^_`{|}~©'
# Define function to cleanup text by removing personal pronouns, stopwords, and puncuation
def cleanup(docs):
    """Text cleanup.

    Remove all punctuations and stopwords from text, also lemmatizes text.

    Args:
        text: text in str format.

    Returns:
        text in str format without all punctuations and stopwords, lemmatized.
    
    Example usage:
        test_text = cleanup(text='Hello world!?')
    """
    texts = []
    doc = nlp(docs, disable=['parser', 'ner'])
    tokens = [tok.lemma_.lower().strip() for tok in doc if tok.lemma_ != '-PRON-']
    tokens = [tok for tok in tokens if tok not in stopwords and tok not in punctuations]
    tokens = ' '.join(tokens)
    texts.append(tokens)
    return pd.Series(texts)
