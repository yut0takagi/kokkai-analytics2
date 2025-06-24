# utils/topic_model.py
from janome.tokenizer import Tokenizer
from gensim import corpora, models
import pandas as pd
from pyvis.network import Network
import streamlit.components.v1 as components

STOPWORDS = set(["する", "ある", "いる", "こと", "これ", "それ", "ため", "よう", "ん", "ます", "です"])

def preprocess_docs(docs):
    t = Tokenizer()
    return [[token.base_form for token in t.tokenize(doc)
             if token.part_of_speech.startswith("名詞") and token.base_form not in STOPWORDS]
            for doc in docs]

def run_lda_topic_model(docs, num_topics=4):
    texts = preprocess_docs(docs)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda = models.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, random_state=42)

    topic_words = []
    for i in range(num_topics):
        words = lda.show_topic(i, topn=5)
        for word, weight in words:
            topic_words.append({"トピック": f"Topic {i+1}", "キーワード": word, "重み": round(weight, 4)})
    return pd.DataFrame(topic_words)

def draw_topic_network(topic_df):
    net = Network(height="500px", width="100%", notebook=False)
    net.barnes_hut()

    topics = topic_df["トピック"].unique()
    for topic in topics:
        net.add_node(topic, label=topic, shape="ellipse", color="#ffcc00")

    for _, row in topic_df.iterrows():
        net.add_node(row["キーワード"], label=row["キーワード"], shape="dot", size=10)
        net.add_edge(row["トピック"], row["キーワード"], value=row["重み"])

    net.set_options("{}")
    net.save_graph("topic_network.html")
    with open("topic_network.html", "r", encoding="utf-8") as f:
        components.html(f.read(), height=550, scrolling=True)
