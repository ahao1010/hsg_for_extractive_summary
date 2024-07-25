from .preprocess_text import preprocess_text

# Preprocess a dataframe: Return an array of {doc preprocessed, labels}
def preprocess_df(df, glovemgr, doc_column_name="docs", labels_column_name="labels", is_sep_n = False, remove_stop_word = True, stemming=True, trunc_sent=-1, padding_sent=-1, trunc_doc=-1):
    result = []
    for idx in df.index:
        result.append({"idx" : idx, "docs" : preprocess_text(df[doc_column_name][idx], glovemgr=glovemgr, is_sep_n=is_sep_n, remove_stop_word=remove_stop_word, stemming=stemming, trunc_sent=trunc_sent, padding_sent=padding_sent), "labels" : df[labels_column_name][idx]})
        if trunc_doc >= 0:
            result[-1] = {"idx" : idx, "docs" : result[-1]["docs"][:min(len(result[-1]["docs"]), trunc_doc)], "labels" : result[-1]["labels"][:min(len(result[-1]["labels"]), trunc_doc)]}
    return result
