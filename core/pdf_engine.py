import sys
import os
from pdf2docx import Converter

# Sửa lỗi hiển thị tiếng Việt trên Terminal Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

def convert_pdf_to_docx(pdf_path):
    pdf_path = os.path.abspath(pdf_path)
    if not pdf_path.lower().endswith('.pdf'):
        print("Vui lòng chọn file .pdf")
        return None
    
    docx_path = pdf_path.replace('.pdf', '.docx')
    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()
    
    print(f"--- Đã chuyển đổi PDF thành công tại: {docx_path} ---")
    return docx_path

if __name__ == "__main__":
    if len(sys.argv) > 1:
        convert_pdf_to_docx(sys.argv[1])
    else:
        print("Vui lòng cung cấp đường dẫn file .pdf")
