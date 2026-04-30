def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                # Split by comma to get id, name, age
                parts = line.split(',')
                if len(parts) == 3:
                    cat_dict = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats_info.append(cat_dict)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        raise
    except Exception as e:
        print(f"Error reading file: {e}")
        raise

    return cats_info


if __name__ == "__main__":
    try:
        cats_info = get_cats_info("files/cats.txt")
        print(cats_info)
    except Exception:
        print("Failed to get cats info.")
