import streamlit as st

# 1. 초기 데이터 설정 (세션 상태를 이용해 대여 상태 유지)
if "books" not in st.session_state:
    st.session_state.books = ["엔트로피", "변신", "문제집", "만화책"]

if "status" not in st.session_state:
    # 모든 책의 초기 상태를 "대여 가능"으로 설정
    st.session_state.status = ["대여 가능"] * len(st.session_state.books)

# 2. UI 타이틀
st.title("📚 도서 대여 시스템")
st.subheader("원하는 도서의 대여 버튼을 눌러주세요.")
st.divider()

# 3. 도서 목록 출력 및 대여 로직
for i in range(len(st.session_state.books)):
    book_name = st.session_state.books[i]
    book_status = st.session_state.status[i]
    
    # 가로로 정렬하기 위해 컬럼 분할 (책 이름, 상태, 대여 버튼)
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        # 오류가 있던 부분 수정 완료! ###이 문자열 안으로 들어갔습니다.
        st.markdown(f"### **{i+1}. {book_name}**")
    
    with col2:
        if book_status == "대여 가능":
            st.success(book_status)
        else:
            st.error(book_status)
            
    with col3:
        # 이미 대여 중인 책은 버튼을 비활성화(disabled) 처리
        if st.button("대여하기", key=f"btn_{i}", disabled=(book_status == "대여 중")):
            st.session_state.status[i] = "대여 중"
            st.toast(f"🎉 '{book_name}' 대여가 완료되었습니다!")
            st.rerun()  # 화면을 새로고침하여 상태 반영

st.divider()

# 4. 반납 기능
st.subheader("🔄 도서 반납하기")
borrowed_books = [st.session_state.books[i] for i in range(len(st.session_state.books)) if st.session_state.status[i] == "대여 중"]

if borrowed_books:
    selected_return = st.selectbox("반납할 책을 선택하세요", borrowed_books)
    if st.button("반납하기"):
        idx = st.session_state.books.index(selected_return)
        st.session_state.status[idx] = "대여 가능"
        st.toast(f"👍 '{selected_return}' 반납이 완료되었습니다.")
        st.rerun()
else:
    st.info("현재 대여 중인 도서가 없습니다.")