# URLs:
# * preprocessing 1 : https://towardsdatascience.com/nlp-preprocessing-with-nltk-3c04ee00edc0
# * preprocessing 2 : https://www.nltk.org/api/nltk.tokenize.html

import string
from nltk.tokenize import LineTokenizer, sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk
# Run the below line only the first time of running nltk
# nltk.download()

# Preprocess a text
def preprocess_text(text, glovemgr, is_sep_n = False, remove_stop_word = True, stemming=True, trunc_sent=-1, padding_sent=-1):
    result = text
    
    # tokenize sentence
    if is_sep_n:
        nltk_line_tokenizer = LineTokenizer()
        result = nltk_line_tokenizer.tokenize(result)
    else:
        result = sent_tokenize(result)

    # lower
    result = [line.lower() for line in result]

    # Remove punctuation
    result = ["".join([char for char in line if char not in string.punctuation]) for line in result]

    # Tokenization
    result = [word_tokenize(line) for line in result]

    # Remove stop word
    if remove_stop_word:
        stop_words = stopwords.words('english')
        result = [[word for word in line if word not in stop_words] for line in result]

    # Stemming
    if stemming:
        porter = PorterStemmer()
        result = [[porter.stem(word) for word in line] for line in result]

    # trunc
    if trunc_sent >= 0:
        result = [line if len(line) <= trunc_sent else line[:trunc_sent] for line in result]

    # word2id
    result = [[glovemgr.w2i(word) for word in line] for line in result]

    # padding
    if padding_sent >= 0:
        result = [line + [0 for i in range(max(0, padding_sent - len(line)))] for line in result]

    return result
