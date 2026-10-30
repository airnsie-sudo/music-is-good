import streamlit as st

# 1. 페이지 설정 (가장 먼저 와야 합니다)
st.set_page_config(page_title="라디오 링크 보기", page_icon="📻")

# 2. 배경 이미지 및 깔끔한 박스 스타일(CSS) 적용
page_bg_img = """
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=1000&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
/* 글자가 배경에 묻히지 않도록 반투명 흰색 박스 처리 */
.block-container {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 15px;
    margin-top: 3rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# 3. 본문 내용 작성
st.title("📻 라디오 채널 링크 확인하기")
st.write("원하는 채널을 선택하고 버튼을 누르면 화면에 링크가 나타납니다.")

# 채널 선택 딕셔너리 (채널명: 링크 주소)
channels = {
    "🎧 1번 채널: 락 밴드 방송": "https://www.youtube.com/watch?v=TDe1DqxwJoc",
    "🎧 2번 채널: 이모 힙합 방송": "https://www.youtube.com/watch?v=pgN-vvVVxMA",
    "🎧 3번 채널: 재즈 음악 방송": "https://www.youtube.com/watch?v=YCQS_8maM3E"
}

# 드롭다운 선택 상자
selected_channel = st.selectbox("들을 채널을 선택하세요:", list(channels.keys()))

# 버튼을 눌렀을 때 링크가 나타나게 설정
if st.button("🔗 링크 생성하기"):
    target_url = channels[selected_channel]
    
    st.success("선택하신 채널의 링크가 준비되었습니다!")
    
    # 화면에 텍스트 링크로 띄우기
    st.markdown(f"👉 **주소:** [{target_url}]({target_url})")
    
    # 바로 새 창으로 열 수 있는 버튼도 함께 제공
    st.link_button("🚀 이 링크 새 창으로 열기", target_url)