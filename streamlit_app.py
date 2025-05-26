
import streamlit as st

# --- 사이드바 (슬라이더) ---
st.sidebar.title("슬라이더")
slider_val = st.sidebar.slider("값 선택", 0, 100, 50)

# --- 탭 구성 ---
tab1, tab2, tab3 = st.tabs(["탭 01", "탭 02", "탭 03"])

with tab1:
    st.write("탭 01 내용")

    # 2x2 레이아웃 구성
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🧱 레이아웃 01")
        st.info(f"슬라이더 값: {slider_val}")
    with col2:
        st.markdown("### 🧱 레이아웃 02")
        st.success("오른쪽 상단 영역")

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 🧱 레이아웃 03")
        st.warning("왼쪽 하단 영역")
    with col4:
        st.markdown("### 🧱 레이아웃 04")
        st.error("오른쪽 하단 영역")

with tab2:
    st.write("탭 02 내용")

with tab3:
    st.write("탭 03 내용")


