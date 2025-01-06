import streamlit as st

# 應用標題
st.title("Streamlit 小部件範例")

# 按鈕範例
st.header("按鈕範例")
if st.button("點擊我！"):
    st.success("你點了按鈕！")

# 滑桿範例
st.header("滑桿範例")
slider_value = st.slider("選擇一個數字：", min_value=0, max_value=100, value=50)
st.write(f"滑桿值為：{slider_value}")

# 選擇框範例
st.header("選擇框範例")
options = ["選項 1", "選項 2", "選項 3"]
selected_option = st.selectbox("從選擇框中選擇一項：", options)
st.write(f"你選擇了：{selected_option}")

# 多選範例
st.header("多選範例")
multi_select = st.multiselect("選擇多個選項：", options)
st.write(f"你選擇了以下選項：{multi_select}")

# 單選按鈕範例
st.header("單選按鈕範例")
radio_value = st.radio("選擇一個選項：", options)
st.write(f"你選擇了：{radio_value}")

# 檢查框範例
st.header("檢查框範例")
if st.checkbox("點擊此處以顯示訊息"):
    st.info("檢查框已選取！")

# 文本輸入範例
st.header("文本輸入範例")
text_input = st.text_input("輸入一些文字：")
if text_input:
    st.write(f"你輸入了：{text_input}")

# 數字輸入框範例
st.header("數字輸入框範例")
number = st.number_input("輸入一個數字：", min_value=0, max_value=100, value=10)
st.write(f"你輸入的數字是：{number}")

# 文件上傳範例
st.header("文件上傳範例")
uploaded_file = st.file_uploader("上傳一個文件：")
if uploaded_file:
    st.write(f"文件名稱：{uploaded_file.name}")

# 日期選擇範例
st.header("日期選擇範例")
selected_date = st.date_input("選擇一個日期：")
st.write(f"你選擇的日期是：{selected_date}")

# 時間選擇範例
st.header("時間選擇範例")
selected_time = st.time_input("選擇一個時間：")
st.write(f"你選擇的時間是：{selected_time}")
