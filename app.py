# app.py
import streamlit as st
from utils.fetch_kokkai import get_speech_by_name
from utils.analyzer import generate_wordcloud
from utils.sentiment import analyze_sentiment
from utils.topic_model import run_lda_topic_model, draw_topic_network
import matplotlib.pyplot as plt

st.set_page_config(page_title="国会議員発言分析", layout="wide")
st.title("🗣️ 国会議員の発言傾向分析アプリ")

# 入力欄
name_input = st.sidebar.text_input("議員名を入力してください（例：岸田文雄）")
submit = st.sidebar.button("分析開始")

if submit and name_input:
    with st.spinner("発言を取得中..."):
        speeches = get_speech_by_name(name_input)
    st.session_state["speeches"] = speeches
    st.session_state["name"] = name_input

# セッションからデータを取得
speeches = st.session_state.get("speeches", [])
name = st.session_state.get("name", "")

if speeches:
    st.success(f"{name} の発言数: {len(speeches)} 件")
    text = "\n".join(speeches)

    tab1, tab2, tab3, tab4 = st.tabs(["📝 発言一覧", "☁️ WordCloud", "📊 感情分析", "📚 トピック分析"])

    with tab1:
        st.subheader("発言内容一覧")
        st.write(speeches)

    with tab2:
        st.subheader("WordCloud")
        wordcloud = generate_wordcloud(text)
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

    with tab3:
        st.subheader("感情分析（BERTベース）")
        results = analyze_sentiment(speeches)
        st.write(results['counts'])
        st.bar_chart(results['counts'])
        st.dataframe(results['details'])

    with tab4:
        st.subheader("LDAによるトピック分析")
        num_topics = st.slider("トピック数", 2, 10, 4)
        topic_words = run_lda_topic_model(speeches, num_topics=num_topics)
        st.write("各トピックに含まれる上位キーワード：")
        st.dataframe(topic_words)
        st.subheader("ノード図（トピック × キーワード）")
        draw_topic_network(topic_words)
else:
    st.info("左のサイドバーに議員名を入力してください")