import streamlit as st
import time

# 페이지 설정
st.set_page_config(page_title="1분 타이머", page_icon="⏱️", layout="centered")
st.title("⏱️ 누적 1분 타이머")

# 상태 초기화
if "time_remaining" not in st.session_state:
    st.session_state.time_remaining = 0  # 남은 시간 (초)
if "start" not in st.session_state:
    st.session_state.start = False
if "stop" not in st.session_state:
    st.session_state.stop = False

# 버튼 동작 함수들
def add_one_minute():
    st.session_state.time_remaining += 60

def start_timer():
    if st.session_state.time_remaining > 0:
        st.session_state.start = True
        st.session_state.stop = False

def stop_timer():
    st.session_state.stop = True
    st.session_state.start = False

# 버튼 UI
col1, col2, col3 = st.columns(3)
with col1:
    st.button("➕ 1분 추가", on_click=add_one_minute)
with col2:
    st.button("▶️ 시작", on_click=start_timer)
with col3:
    st.button("⏹️ 정지", on_click=stop_timer)

# 상태 출력
st.markdown(f"### ⏱️ 총 타이머 시간: {st.session_state.time_remaining}초")

# 타이머 실행
if st.session_state.start and not st.session_state.stop:
    timer_slot = st.empty()
    for i in range(st.session_state.time_remaining):
        if st.session_state.stop:
            timer_slot.markdown("⏹️ 타이머 정지됨")
            break
        remaining = st.session_state.time_remaining - i
        timer_slot.markdown(f"## ⏳ 남은 시간: {remaining}초")
        time.sleep(1)
    else:
        timer_slot.markdown("## ✅ 타이머 완료!")
    st.session_state.time_remaining = 0
    st.session_state.start = False
