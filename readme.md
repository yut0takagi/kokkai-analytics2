# 国会議員の発言傾向分析アプリ

このアプリは、国会会議録APIを利用して特定議員の発言を収集・分析し、以下の4つの視点から可視化します：

- 📝 発言一覧：原文をそのまま閲覧
- ☁️ WordCloud：出現頻度の高い単語を視覚化
- 📊 感情分析：BERTモデルによる感情分類
- 📚 トピック分析：LDAとノード図で構造化表示

## 💻 使用技術
- Python 3.11+
- Streamlit
- Hugging Face Transformers（感情分析）
- Gensim（LDAトピックモデル）
- Pyvis（ノード可視化）
- Janome（日本語形態素解析）

## 📦 インストール
```bash
pip install -r requirements.txt
```

## ▶️ 起動方法
```bash
streamlit run app.py
```

## 📝 フォルダ構成
```
kokkai-analytics/
├── app.py
├── utils/
│   ├── fetch_kokkai.py
│   ├── analyzer.py
│   ├── sentiment.py
│   └── topic_model.py
├── topic_network.html
├── requirements.txt
└── README.md
```

---
