import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="24/7 나만의 웹 라디오 방송국", page_icon="📻", layout="wide")

# 2. 배경 및 스타일(CSS) 설정
page_bg_img = """
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?q=80&w=1000&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
.block-container {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 2.5rem;
    border-radius: 20px;
    margin-top: 2rem;
    box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# 3. 사이드바 메뉴 확장
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3076/3076785.png", width=80)
    st.title("📻 방송국 메인 메뉴")
    st.markdown("---")
    
    # 6개의 다양해진 메뉴 탭
    menu = st.radio(
        "이동할 창을 선택하세요:",
        [
            "🎧 ON AIR (실시간 채널)",
            "📅 방송 편성표",
            "✉️ 사연 & 신청곡 접수",    
            "💬 청취자 방명록",
            "ℹ️ 방송국 정보"
        ]
    )
    st.markdown("---")
    st.success("방송 상태: ON AIR 🟢")
    st.caption("현재 접속자: 1명 (나)")

# ---------------------------------------------------------
# Tab 1: 실시간 채널
# ---------------------------------------------------------
if menu == "🎧 ON AIR (실시간 채널)":
    st.title("🎧 ON AIR - 실시간 라디오")
    st.write("원하는 채널을 선택하고 플레이어 또는 새 창 링크로 음악을 감상하세요!")

    channels = {
        "🎧 1번 채널: 락 밴드 방송": {
            "url": "https://www.youtube.com/watch?v=TDe1DqxwJoc",
            "desc": "가슴이 뻥 뚫리는 강렬한 락 사운드 모음!",
            "genre": "Rock / Alternative"
        },
        "🎧 2번 채널: 이모 힙합 방송": {
            "url": "https://www.youtube.com/watch?v=pgN-vvVVxMA",
            "desc": "감성적이고 깊이 있는 이모 힙합 플레이리스트.",
            "genre": "Emo Hip-Hop / Lo-Fi"
        },
        "🎧 3번 채널: 재즈 음악 방송": {
            "url": "https://www.youtube.com/watch?v=YCQS_8maM3E",
            "desc": "카페에 온 듯한 편안하고 부드러운 재즈 선율.",
            "genre": "Jazz / Lounge"
        }
    }

    selected_name = st.selectbox("들을 채널을 선택하세요:", list(channels.keys()))
    current = channels[selected_name]

    col1, col2 = st.columns([1, 2])
    with col1:
        st.info(f"**장르:** {current['genre']}\n\n**설명:** {current['desc']}")
    with col2:
        if st.button("▶ 방송 열기 및 링크 생성", use_container_width=True):
            st.success("선택하신 채널이 재생 준비되었습니다!")
            st.video(current["url"])
            st.link_button("🚀 이 링크 새 창으로 열기", current["url"], use_container_width=True)

# ---------------------------------------------------------
# Tab 2: 방송 편성표
# ---------------------------------------------------------
elif menu == "📅 방송 편성표":
    st.title("📅 오늘의 라디오 편성표")
    st.write("24시간 언제나 함께하는 시간대별 라디오 프로그램 일정입니다.")

    schedule_data = [
        {"시간": "08:00 - 10:00", "프로그램": "☀️ 모닝 락 앤 로울", "DJ": "DJ Rock", "주요 장르": "신나는 락 음악"},
        {"시간": "12:00 - 14:00", "프로그램": "☕ 나른한 오후의 재즈", "DJ": "DJ Jazzman", "주요 장르": "클래식 & 재즈"},
        {"시간": "18:00 - 20:00", "프로그램": "🌆 퇴근길 감성 힙합", "DJ": "DJ Emo", "주요 장르": "이모 힙합 & 싱어송라이터"},
        {"시간": "22:00 - 02:00", "프로그램": "🌙 심야 로파이 심야식당", "DJ": "DJ Night", "주요 장르": "Lo-Fi & Ambient"}
    ]
    st.table(schedule_data)

# ---------------------------------------------------------
# Tab 3: 사연 & 신청곡
# ---------------------------------------------------------
elif menu == "✉️ 사연 & 신청곡 접수":
    st.title("✉️ 사연 & 신청곡 보내기")
    st.write("DJ에게 듣고 싶은 노래나 남기고 싶은 사연을 적어주세요!")

    with st.form("request_form"):
        name = st.text_input("청취자 이름 (또는 닉네임)")
        song = st.text_input("신청곡 (가수 - 곡 제목)")
        story = st.text_area("보내실 사연")
        
        submitted = st.form_submit_button("💌 사연 보내기")
        if submitted:
            if name and song:
                st.balloons() # 축하 풍선 애니메이션 효과
                st.success(f"'{name}'님의 사연과 신청곡 [{song}]이(가) DJ에게 전달되었습니다!")
            else:
                st.warning("이름과 신청곡 제목을 작성해주세요.")

# ---------------------------------------------------------
# ---------------------------------------------------------
# Tab 5: 청취자 방명록
# ---------------------------------------------------------
elif menu == "💬 청취자 방명록":
    st.title("💬 청취자 한마디")
    st.write("방송을 들으면서 자유롭게 출석 체크나 한마디를 남겨보세요!")

    with st.form("guestbook_form"):
        nickname = st.text_input("닉네임")
        message = st.text_input("한마디")
        submitted = st.form_submit_button("등록")
        if submitted and nickname and message:
            st.success(f"[{nickname}] {message}")

# ---------------------------------------------------------
# Tab 6: 방송국 정보
# ---------------------------------------------------------
elif menu == "ℹ️ 방송국 정보":
    st.title("ℹ️ 방송국 소개")
    st.markdown("""
    - **방송국명:** Music-Is-Good Radio Station
    - **기술 스택:** Python, Streamlit, GitHub, Streamlit Cloud
    - **특징:** 모바일 웹 환경 최적화, 24시간 언제 어디서나 접속 가능
    """)