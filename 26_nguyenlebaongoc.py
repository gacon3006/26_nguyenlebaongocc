# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Thêm sinh viên vào danh sách.
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

# --- Phần kiểm tra ---
if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")
    
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")
