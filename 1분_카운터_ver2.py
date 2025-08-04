import streamlit as st
import time

# 페이지 설정
st.set_page_config(page_title="1분 타이머", page_icon="⏱️", layout="centered")

st.title("⏱️ 1분 타이머")

# 상태 초기화
if "start" not in st.session_state:
    st.session_state.start = False
if "stop" not in st.session_state:
    st.session_state.stop = False

# 시작 함수
def start_timer():
    st.session_state.start = True
    st.session_state.stop = False

# 정지 함수
def stop_timer():
    st.session_state.stop = True
    st.session_state.start = False

# 버튼 UI
col1, col2 = st.columns(2)
with col1:
    st.button("▶️ 시작", on_click=start_timer)
with col2:
    st.button("⏹️ 정지", on_click=stop_timer)

# 타이머 실행
if st.session_state.start and not st.session_state.stop:
    timer_slot = st.empty()
    for i in range(60):
        if st.session_state.stop:
            timer_slot.markdown("⏹️ 타이머 정지됨")
            break
        timer_slot.markdown(f"## ⏳ {i + 1}초 경과")
        time.sleep(1)
    else:
        timer_slot.markdown("## ✅ 1분 경과!")
    st.session_state.start = False

# Footer
st.markdown("---")
st.caption("🛠️ Made with Streamlit")
