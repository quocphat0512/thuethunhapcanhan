import streamlit as st

st.title("🧮 Tính thuế thu nhập cá nhân")
st.divider()

muc_luong = st.number_input("Nhập lương của bạn ")
thuong = st.number_input("Nhập thưởng của bạn")
so_nguoi_phu_thuoc = st.number_input("Số người phụ thuộc")

bao_hiem_xa_hoi_bat_buoc = 0.0
giam_tru_ban_than = 15500000.0  
giam_tru_phu_thuoc = 6200000.0 * so_nguoi_phu_thuoc
a = 0.0
c = 0.0

if tong_thu_nhap > 0:
    muc_tran_bhxh_bhyt = 46800000.0  
    muc_tran_bhtn = 99200000.0       
    
    phi_bhxh_bhyt = min(muc_luong, muc_tran_bhxh_bhyt) * 0.095
    phi_bhtn = min(muc_luong, muc_tran_bhtn) * 0.01
    
    bao_hiem_xa_hoi_bat_buoc = phi_bhxh_bhyt + phi_bhtn
    muc_luong_sau_bhxh = thuong - bao_hiem_xa_hoi_bat_buoc

    tong_giam_tru = giam_tru_ban_than + giam_tru_phu_thuoc
    a = thuong - tong_giam_tru - muc_luong_sau_bhxh

if a > 0:
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
else:
    a = 0.0
    c = 0.0

if a > 0:
    st.write(f"**Thu nhập tính thuế:** {a:,.0f} VNĐ")
    st.success(f"💵 Tiền thuế phải nộp:\n### {c:,.0f} VNĐ")
else:
    st.write("**Thu nhập tính thuế:** 0 VNĐ")
    st.success("💵 Tiền thuế phải nộp:\n### 0 VNĐ")
