import streamlit as st
import os
from core.pdf_engine import convert_pdf_to_docx

# --- CONFIG ---
st.set_page_config(page_title="TEXO PDF Decoder", page_icon="🧲", layout="wide")

# --- STYLE PREMIUM ---
st.markdown("""
<style>
    /* --- TỐI ƯU HÓA CSS CHO CẢ 2 CHẾ ĐỘ --- */
    h1, h2, h3, h4, .main-header { color: #FFD700 !important; }
    
    .main-header { 
        font-weight: 800; 
        font-size: 32px; 
        text-align: center; 
        border-bottom: 2px solid #FFD700; 
        padding-bottom: 10px; 
        margin-bottom: 20px; 
    }
    
    .stButton>button { 
        background: linear-gradient(135deg, #152A4A 0%, #1e3a8a 100%) !important; 
        color: #FFD700 !important; 
        border: 1px solid #FFD700 !important; 
        border-radius: 12px; 
        font-weight: bold; 
        height: 3.5em; 
        width: 100%; 
    }
    .stButton>button:hover { 
        background: #FFD700 !important; 
        color: #0A1931 !important; 
        transform: scale(1.02); 
        transition: 0.2s; 
    }
    
    .footer { text-align: center; color: #888; font-size: 12px; margin-top: 50px; border-top: 1px solid rgba(255, 215, 0, 0.1); padding-top: 20px; }
</style>
""", unsafe_allow_html=True)

# --- AUTH ---
def check_password():
    if "authenticated" not in st.session_state: st.session_state.authenticated = False
    if st.session_state.authenticated: return True
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<h2 style='text-align: center; color: #FFD700;'>🏦 TEXO PDF DECODER</h2>", unsafe_allow_html=True)
        pwd = st.text_input("Mật khẩu truy cập:", type="password")
        if st.button("XÁC THỰC"):
            if pwd == "texo2026":
                st.session_state.authenticated = True
                st.rerun()
            else: st.error("❌ Truy cập không hợp lệ.")
    return False

if not check_password(): st.stop()

# --- MAIN ---
st.markdown("<div class='main-header'>🧲 OCR: GIẢI MÃ PDF KỸ THUẬT</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Tải tệp nguồn")
    pdf_file = st.file_uploader("Tải tệp PDF", type=["pdf"])

with col2:
    st.markdown("### 🚀 Thực thi giải mã")
    if pdf_file:
        st.info(f"Đã nhận tệp: **{pdf_file.name}**")
        if st.button("🚀 KHỞI CHẠY GIẢI MÃ OCR"):
            with st.spinner("Đang thực hiện bóc tách dữ liệu..."):
                try:
                    pdf_path = "temp_source.pdf"
                    with open(pdf_path, "wb") as f:
                        f.write(pdf_file.getbuffer())
                    
                    res_path = convert_pdf_to_docx(pdf_path)
                    
                    if res_path and os.path.exists(res_path):
                        st.success("🎊 Đã bóc tách thành công.")
                        st.balloons()
                        with open(res_path, "rb") as fw:
                            st.download_button("📥 TẢI VỀ BẢN WORD", fw, f"Decoded_{pdf_file.name.replace('.pdf', '.docx')}")
                    
                    # Cleanup after download (optional)
                    if os.path.exists(pdf_path): os.remove(pdf_path)
                except Exception as e:
                    st.error(f"❌ Lỗi giải mã: {e}")
    else:
        st.markdown("<div style='text-align: center; color: #64748b; font-weight: 500; padding: 100px 20px;'>Hệ thống đang sẵn sàng... <br>Vui lòng tải tệp PDF ở cột bên trái để AI bắt đầu giải mã.</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>TEXO Engineering Department | Version 2.0 (Standalone) | Hoàng Đức Vũ</div>", unsafe_allow_html=True)
