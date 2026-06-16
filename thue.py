import streamlit as st

st.title("🧮 Tính thuế thu nhập cá nhân")
st.divider()

tong_thu_nhap = st.number_input("Nhập thu nhập của bạn", min_value=0.0, step=1000000.0)
so_nguoi_phu_thuoc = st.number_input("Số người phụ thuộc", min_value=0, step=1)

bao_hiem_xa_hoi_bat_buoc = 0.15*tong_thu_nhap
giam_tru_ban_than = 11000000.0
giam_tru_phu_thuoc = 4400000.0 * so_nguoi_phu_thuoc
tong_giam_tru = giam_tru_ban_than + giam_tru_phu_thuoc + bao_hiem_xa_hoi_bat_buoc
a = 0.0
c = 0.0

if tong_thu_nhap > 0:
    bao_hiem_xa_hoi_bat_buoc = 0.15 * tong_thu_nhap
    a = tong_thu_nhap - tong_giam_tru - bao_hiem_xa_hoi_bat_buoc

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
