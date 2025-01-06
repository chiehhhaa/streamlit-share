import streamlit as st
from openai import OpenAI
import time

# 設定 OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("簡單的聊天機器人")

# 設定預設的模型
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# 初始化聊天記錄
if "messages" not in st.session_state:
    st.session_state.messages = []

# 顯示聊天記錄中的消息
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 接收使用者輸入
if prompt := st.chat_input("請輸入您的問題："):
    # 將使用者消息新增到聊天記錄中
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 顯示助理回應的消息容器
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        # 使用 OpenAI 的串流回應
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True  # 啟用串流
        )

        # 逐字顯示回應
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                response_placeholder.markdown(full_response + "▌")
                time.sleep(0.05)

        # 顯示最終回應（移除游標）
        response_placeholder.markdown(full_response)

        # 將完整回應新增到聊天記錄
        st.session_state.messages.append({"role": "assistant", "content": full_response})