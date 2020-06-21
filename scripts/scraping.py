import re
import time
from typing import List

import pandas as pd
import requests
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


def transform_list(a_list: List[str], old_string: str, replacement_string: str, ) -> List:
    """
    :param old_string: The string to be replaced
    :param replacement_string: The string that will be used to update the old one
    :param a_list: any list (of strings)
    :return: transformed list with string replacement applied
    """
    transformed_list = [x.replace(old_string, replacement_string) for x in a_list]
    return transformed_list


def preprocess(a_corpus: List[str]) -> List[str]:
    """
    :param a_corpus: any list of strings
    :return: transformed list of strings, without html tags, new line and space characters
    """
    tags_regex = re.compile('(<[^>]+>)')
    clean_corpus_1 = [tags_regex.sub('', doc) for doc in a_corpus]
    clean_corpus_2 = [doc.replace('\r', ' ') for doc in clean_corpus_1]
    clean_corpus_3 = [doc.replace('\n', ' ') for doc in clean_corpus_2]
    clean_corpus = [doc.replace('\xa0', ' ') for doc in clean_corpus_3]
    return clean_corpus


articles = [
    "https://apolitical.co/en/solution_article/how-climate-change-adds-fuel-to-the-refugee-crisis",
    "https://apolitical.co/en/solution_article/how-wigan-drove-change-by-putting-people-first",
    "https://apolitical.co/en/solution_article/what-ghana-can-teach-us-about-integrating-refugees",
    "https://apolitical.co/en/solution_article/does-free-public-transport-actually-work",
    "https://apolitical.co/en/solution_article/the-city-of-the-future-is-built-on-open-data",
    "https://apolitical.co/en/solution_article/no-city-limits-how-data-is-helping-shape-urban-health-policy",
    "https://apolitical.co/en/solution_article/syria-displaced-doctors-turkey-workforce",
    "https://apolitical.co/en/solution_article/local-councils-citizens-collaboration",
    "https://apolitical.co/en/solution_article/reasons-to-be-cheerful-about-the-future-of-local-government",
    "https://apolitical.co/en/solution_article/a-case-for-copying-brazils-refugee-policy",
    "https://apolitical.co/en/solution_article/building-safer-and-more-resilient-cities-in-the-philippines",
    "https://apolitical.co/en/solution_article/regional-australia-needs-immigrants-but-forcing-them-there-isnt-the-answer",
    "https://apolitical.co/en/solution_article/a-small-town-solution-to-digitisation",
    "https://apolitical.co/en/solution_article/smart-cities-are-nothing-without-their-citizens",
    "https://apolitical.co/en/solution_article/what-joining-local-government-feels-like-for-a-junior-public-servant",
]

article_corpus = []

if __name__ == '__main__':

    apis = transform_list(articles, "/en/solution_article/", "/api/articles/articles/;slug=")
    for api in apis:
        article = requests.get(api)
        if article.status_code == 429:
            time.sleep(3)
            article = requests.get(api)
        article_json = article.json()
        article_corpus.append(article_json["content"])

    # get rid of everything that isn't pure text content
    new_corpus = preprocess(article_corpus)
    print("NEW CORPUS HERE ", new_corpus)  # debugging

    # # TF-IDF implementation taken from this youtube video https://www.youtube.com/watch?v=BJ0MnawUpaU&t=585s
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'),
                                 use_idf=True,
                                 ngram_range=(1, 2))  # Tokenising using bigrams

    X = vectorizer.fit(new_corpus)
    print(X)  # debugging
    vocab = X.vocabulary_
    print(sorted(vocab.items(), key=lambda x: x[1], reverse=True))
    frame = pd.DataFrame(sorted(vocab.items(), key=lambda x: x[1], reverse=True)).head(30)
    print(frame)

    # TODO: investigate lines 91 onwards ..
    # This will see the most common word in one document - this approach might not be scalable?
    # tokenizer = NLTKWordTokenizer()
    # tokens = tokenizer.tokenize(docs)
    # freq_dist_pos = FreqDist(tokens)
    # print(tokens.most_common(10))

    # TODO: Dont commit geko driver or test
