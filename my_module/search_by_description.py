
import pandas as pd
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize

model_downloaded = Doc2Vec.load("../models/d2v.model")
reviews_with_summary = pd.read_csv("../data/wine_reviews_with_summary.csv", index_col=0, encoding='utf-8')
reviews_with_summary['summary'] = reviews_with_summary['summary'].astype(str)

def top_search_by_description(description, amount = 5):
    """Select most relevant vines from dataset according to users description.

    Tokenized description and find most relevant vines from Dos2Vec dataset.

    Args:
        text: text in str format.
        amount: number of vines listed.

    Returns:
        print amount of vines relevant to description.
    
    Example usage:
        test_text = top_search_by_description(description='Hello world!?', amount = 5)
    """
    #to find the vector of a document which is not in training data
    description = word_tokenize(description)
    description_vec = model_downloaded.infer_vector(description)
    sims = model_downloaded.dv.most_similar([description_vec], topn=len(model_downloaded.dv))
    print('The most suitable wines according to the description:\n')
    for i in range(5):
        index = int(sims[i][0])
        acc = float(sims[i][1]) * 100
        print(f"Vine title: {reviews_with_summary['title'][index]}, vine variety: {reviews_with_summary['variety'][index]}"
            f", WineEnthusiast points: {reviews_with_summary['points'][index]:.0f}. Coincidence: {acc:.2f}%.")
