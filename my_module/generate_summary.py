
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

def summary(cleaned_text):
    """Summarizes text.

    Summarizes text according to TfidfVectorizer.

    Args:
        text: text in str format.

    Returns:
        text in str format sortedt and summarized according to TfidfVectorizer.
    
    Example usage:
        test_text = summary(text='Hello world!?')
    """
    tfidf_vectorizer = TfidfVectorizer()

    sentences = sent_tokenize(cleaned_text)

    tfidf_matrix = tfidf_vectorizer.fit_transform(sentences)
    scores = tfidf_matrix.toarray().sum(axis=0)
    ranked_sentences = sorted(((scores[i], sentence) for i, sentence in enumerate(sentences)), reverse=True)
    summary_sentences = [sentence for score, sentence in ranked_sentences[:3]]

    original_sentences = [sentences[sentences.index(summary_sentence)] for summary_sentence in summary_sentences]

    summary = ' '.join(original_sentences)

    return summary
