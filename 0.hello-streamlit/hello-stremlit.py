import streamlit as st

st.title("簡單的 Streamlit 範例")
st.write("這是一個互動式應用")
user_input = st.text_input("請輸入內容：")
if st.button("提交"):
    st.write(f"你輸入了：{user_input}")