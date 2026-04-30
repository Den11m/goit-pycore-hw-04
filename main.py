from hw01 import total_salary
from hw02 import get_cats_info


try:
    total, average = total_salary("files/salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except Exception:
    print("Failed to calculate salaries.")

try:
    cats_info = get_cats_info("files/cats.txt")
    print(cats_info)
except Exception:
    print("Failed to get cats info.")
