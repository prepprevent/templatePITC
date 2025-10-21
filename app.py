import streamlit as st
import pandas as pd
import json
from io import BytesIO

st.title("📄 Đổi file DB sang Excel để import vào HIV INFO - By SI Teams")

uploaded_file = st.file_uploader("Tải file JSON DB vào đây", type=["json"])

if uploaded_file:
    data = json.load(uploaded_file)
    df = pd.DataFrame(data)
    st.success("✅ Đã đọc file thành công!")
    st.dataframe(df.head())

    # Chuyển đổi
    df_new = pd.DataFrame({
        "STT": range(1, len(df) + 1),
        "Mã số": None,
        "Họ tên": df["Hoten"],
        "Giới tính": df["gioitinh"],
        "Năm sinh\n(yyyy)": df["Namsinh"],
        "Địa chỉ chi tiết": df["hk_sonha"],
        "Mã Phường xã thường trú": df["hk_xa_id"],
        "Mã Tỉnh/Thành phố thường trú": df["hk_tinh_id"],
        "Địa chỉ chi tiết": df["hk_sonha"],
        "Mã Phường xã hiện tại": df["dc_xa_id"],
        "Mã Tỉnh/Thành phố hiện tại": df["dc_tinh_id"],
        "Số CMND": df["CCCD"],
        "Số thẻ BHYT": df["sothe_bhyt"],
        "Đối tượng": df["ds_doituong_id"],
        "Đường lây truyền": df["duonglay_id"],
        "Cơ sở gửi mẫu": df["coso_name"],
        "Mã KH XN sàng lọc": df["Makh"],
        "Ngày lấy mẫu": df["xnsl_ngay"],
        "Kết quả XN sàng lọc": df["xnsl_ketqua"],
        "Chất lượng mẫu": "Đạt",
        "Ngày gửi mẫu\n(dd/MM/yy)": df["xnsl_ngay"],
        "Loại dịch vụ": "Cố định",
        "Ngày nhận mẫu\n(dd/MM/yy)": df["xnsl_ngay"],
        "Tên SP1": "NanoSign HIV 1/2 3.0",
        "Kết quả SP1": "Dương tính",
        "Ngày XN SP1\n(dd/MM/yy)": df["xnsl_ngay"],
        "Tên SP2": "NanoSign HIV 1/2 3.0",
        "Kết quả SP2": "Dương tính",
        "Ngày XN SP2\n(dd/MM/yy)": df["xnsl_ngay"],
        "Tên SP3": "NanoSign HIV 1/2 3.0",
        "Kết quả SP3": "Dương tính",
        "Ngày XN SP3\n(dd/MM/yy)": df["xnsl_ngay"],
        "Kết quả XN khẳng định": df["xnkd_ketqua"],
        "Ngày XN khẳng định\n(dd/MM/yy)": df["xnkd_ngayth"],
        "Mã số lưu mẫu": df["xnkd_ma"],
        "KQXN nhiễm mới bằng sinh phẩm nhanh": df["xnnm_qk_nhanh"],
        "Ngày XN mới nhiễm HIV\n(dd/MM/yy)": df["xnnm_ngay_nhanh"],
        "KQXN tải lượng vi rút": df["xnnm_ketluan"],
        "Ngày XN tải lượng vi rút\n(dd/MM/yy)": df["tlvr_ngayxn"],
        "Ngày trả kết quả XN khẳng định\n(dd/MM/yy)": df["xnkd_ngaykd"],
        "Cán bộ XN khẳng định": df["TVV_Sau_xn_id"]
    })

    buffer = BytesIO()
    df_new.to_excel(buffer, index=False, engine='openpyxl')
    buffer.seek(0)

    st.download_button(
        label="⬇️ Tải xuống file Excel",
        data=buffer,
        file_name="ketqua_chuyen_doi.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

