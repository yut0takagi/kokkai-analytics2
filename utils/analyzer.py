# utils/analyzer.py
from wordcloud import WordCloud
from janome.tokenizer import Tokenizer

# 日本語ストップワードの例（必要に応じて拡張）
STOPWORDS = set(["する", "ある", "いる", "こと", "これ", "それ", "ため", "よう", "ん", "ます", "です"])

def generate_wordcloud(text):
    t = Tokenizer()
    words = [token.base_form for token in t.tokenize(text)
             if token.part_of_speech.startswith("名詞") and token.base_form not in STOPWORDS]
    word_text = " ".join(words)

    wordcloud = WordCloud(
        width=800,
        height=400,
        font_path="/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
        background_color="white"
    ).generate(word_text)

    return wordcloud