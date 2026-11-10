import streamlit as st
import pymysql

# 1. 페이지 제목 설정
st.title("🚗 다함께 차차차 - 데이터베이스 연동")

# 2. Streamlit Secrets에서 DB 접속 정보 가져오기
try:
    db_config = st.secrets["mysql"]
    
    # 3. 데이터베이스 연결 실행
    connection = pymysql.connect(
        host=db_config["host"],
        port=int(db_config["port"]),
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"],
        charset="utf8mb4"
    )
    
    st.success("🎉 데이터베이스(TiDB)와 성공적으로 연결되었습니다!")
    
    # 4. 간단한 테스트 쿼리 실행 (DB 버전 확인)
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION();")
        version = cursor.fetchone()
        st.write(f"현재 연결된 TiDB 버전: `{version[0]}`")
        
    # 연결 닫기
    connection.close()

except Exception as e:
    st.error(f"❌ 데이터베이스 연결 실패: {e}")
    st.warning("비밀번호나 호스트 주소가 올바른지 `.streamlit/secrets.toml` 파일을 다시 확인해 주세요.")