from transformers import pipeline
import pandas as pd

# 日本語感情分析モデルの選定
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="christian-phu/bert-finetuned-japanese-sentiment"
)

def analyze_sentiment(speech_list):
    results = []
    for text in speech_list:
        short_text = text[:300]
        try:
            out = sentiment_pipeline(short_text)[0]
            label = out["label"]
        except Exception:
            label = "ERROR"
        results.append({"text": short_text, "label": label})

    df = pd.DataFrame(results)
    counts = df["label"].value_counts()
    return {"details": df, "counts": counts}