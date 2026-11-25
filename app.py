import random
import time
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="스마트 수질 판별기", page_icon="💧")

# 2. 제목 및 설명
st.title("💧 스마트 식수 판별기")
st.write(
    "기계에 물 샘플을 넣고 아래 버튼을 누르면 식용 가능 여부를 분석합니다."
)
st.divider()

# 3. 분석 시작 버튼
if st.button("🔍 수질 검사 시작하기", type="primary", use_container_width=True):

    # 분석 중 로딩 애니메이션
    with st.spinner("물의 성분과 미생물을 분석하는 중입니다..."):
        time.sleep(1.5)

    # random 라이브러리로 가상의 수질 데이터 생성
    ph_level = round(random.uniform(5.0, 9.5), 1)  # 적정 기준: 6.5 ~ 8.5
    turbidity = round(random.uniform(0.1, 3.0), 2)  # 적정 기준: 1.0 NTU 이하
    bacteria_detected = random.choices([False, True], weights=[80, 20])[
        0
    ]  # 80% 미검출, 20% 검출

    # 측정 결과 화면 표시
    st.subheader("📊 수질 측정 결과")
    col1, col2, col3 = st.columns(3)

    col1.metric("산성도 (pH)", f"{ph_level}")
    col2.metric("탁도 (NTU)", f"{turbidity}")
    col3.metric("유해 세균", "검출됨 ⚠️" if bacteria_detected else "미검출 ✅")

    st.divider()

    # 식용 가능 여부 최종 판정
    is_ph_safe = 6.5 <= ph_level <= 8.5
    is_turbidity_safe = turbidity <= 1.0
    is_bacteria_safe = not bacteria_detected

    if is_ph_safe and is_turbidity_safe and is_bacteria_safe:
        st.success("### ✅ 판정: 식용 가능한 깨끗한 물입니다!")
        st.balloons()
        st.write("모든 수질 기준을 통과했습니다. 안심하고 마셔도 좋습니다.")
    else:
        st.error("### 🚨 판정: 식용 불가능한 물입니다!")
        st.write("**[부적합 사유]**")
        if not is_ph_safe:
            st.write(
                f"- **pH 수치 이상:** 현재 {ph_level} (적정 기준: 6.5 ~ 8.5)"
            )
        if not is_turbidity_safe:
            st.write(
                f"- **탁도 기준 초과:** 현재 {turbidity} NTU (적정 기준: 1.0 NTU 이하)"
            )
        if not is_bacteria_safe:
            st.write("- **유해 세균 검출:** 끓여 마시거나 정수 처리가 필요합니다.")
