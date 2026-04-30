def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                # Split by comma and extract salary (second element)
                parts = line.split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(f"Warning: Invalid salary format in line: {line}")
                        continue
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        raise
    except Exception as e:
        print(f"Error reading file: {e}")
        raise

    if count == 0:
        average = 0
    else:
        average = total // count

    return total, average


if __name__ == "__main__":
    try:
        total, average = total_salary("files/salary.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception:
        print("Failed to calculate salaries.")
