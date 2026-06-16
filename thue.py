import streamlit as st

st.title("🧮 Tính thuế thu nhập cá nhân")

st.divider()

a = st.number_input("Nhập thu nhập tính thuế của bạn ")

if a > 0:
    c = 0.0  

    if a <= 10000000:
        c = a * 0.05
        
    elif a <= 30000000:
        c = (a * 0.10) - 500000
        
    elif a <= 60000000:
        c = (a * 0.20) - 3500000
        
    elif a <= 100000000:
        c = (a * 0.30) - 9500000
        
    else:
        c = (a * 0.35) - 14500000

    st.divider()
    st.subheader("KẾT QUẢ TÍNH THUẾ")
    st.success(f"💵 Tiền thuế phải nộp:\n### {c:,.0f} VNĐ")
