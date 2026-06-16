import streamlit as st

st.title("🧮 Tính thuế thu nhập cá nhân")

st.divider()

tong_thu_nhap= st.number_input("Nhập thu nhập của bạn ")
so_nguoi_phu_thuoc= st.number_input("số người phụ thuộc")
if tong_thu_nhap > 0:
    
    giam_tru_ban_than=15500000
    giam_tru_phu_thuoc=6200000*so_nguoi_phu_thuoc
    tong_giam_tru=giam_tru_ban_than + giam_tru_phu_thuoc
    a = tong_thu_nhap - tong_giam_tru
c=0
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
