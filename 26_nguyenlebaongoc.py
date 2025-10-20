# Tính năng 3: Tìm kiếm sinh viên
def search_student(search_name):
    """
    YÊU CẦU 3: Tìm sinh viên theo tên.
    """
    print("--- KET QUA TIM KIEM ---")
    search_name_lower = search_name.lower()
    results = [s for s in student_list if search_name_lower in s['name'].lower()]
    if not results:
        print("Khong tim thay sinh vien nao.")
    else:
        for s in results:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")

# --- Phần kiểm tra ---
if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")
    
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    print("\n3. Tim kiem sinh vien theo ten 'an':")
    search_student("an")

    print("\nTim kiem sinh vien theo ten 'Dung':")
    search_student("Dung")
