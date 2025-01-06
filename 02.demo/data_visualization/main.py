import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# 快取數據載入
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# 上傳 CSV 檔案
uploaded_file = st.file_uploader("上傳 CSV 檔案", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # 確保日期和數據格式正確
    data["日期"] = pd.to_datetime(data["日期"])  # 確保日期格式正確
    data["訪客數"] = pd.to_numeric(data["訪客數"], errors="coerce")  # 確保訪客數是數字類型

    st.write("數據表格")
    st.dataframe(data)

    # 篩選數據：選擇年份
    st.header("篩選數據 🔍")
    selected_year = st.selectbox("選擇年份", options=data["日期"].dt.year.unique())
    filtered_data = data[data["日期"].dt.year == selected_year]

    if filtered_data.empty:
        st.warning("所選年份無資料！")
    else:
        # 圖表類型選擇
        st.header("選擇圖表類型 📊")
        chart_type = st.selectbox("選擇圖表類型", ["折線圖", "圓餅圖", "柱狀圖"])

        # 折線圖：銷售額變化
        if chart_type == "折線圖":
            st.subheader("折線圖：每日銷售額變化")
            line_chart = (
                alt.Chart(filtered_data)
                .mark_line()
                .encode(
                    x="日期:T",
                    y="銷售額:Q",
                    tooltip=["日期", "銷售額"]
                )
                .interactive()
            )
            st.altair_chart(line_chart, use_container_width=True)

        # 圓餅圖：商品分佈
        elif chart_type == "圓餅圖":
            st.subheader("圓餅圖：商品分佈")
            pie_chart = px.pie(
                filtered_data,
                names="商品分類",
                values="銷售額",
                title="商品分佈"
            )
            st.plotly_chart(pie_chart)

        # 柱狀圖：每日訪客數
        elif chart_type == "柱狀圖":
            st.subheader("柱狀圖：每日訪客數")
            bar_chart = (
                alt.Chart(filtered_data)
                .mark_bar(color="skyblue")
                .encode(
                    x="日期:T",
                    y="訪客數:Q",
                    tooltip=["日期", "訪客數"]
                )
                .interactive()
            )
            st.altair_chart(bar_chart, use_container_width=True)
