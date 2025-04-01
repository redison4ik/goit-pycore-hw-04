from pathlib import Path

def get_cats_info(path: Path) -> list[dict]: # список[ключ:значення]
    if not path.exists(): # чи існує файл
        print("Файл не знайдено:", path)
        return

    cats = [] # список котів
    with path.open('r', encoding='utf-8') as fh:# відкрити для читання
         for line in fh:
            line = line.strip()
            if not line:
                continue  # перевірка на порожні рядки

            try:
                cat_id, name, age = line.split(',') # відділяємо необхідні значення
                cats.append({ # створюємо ключі та значення
                    "ID": cat_id,
                    "Name": name,
                    "Age": int(age)
                })
            except ValueError:
                print(f"⚠️ Проблема з рядком: {line}")

    return cats

file_path = Path(__file__).parent / "Cats" / "Cats.txt" # шлях
Cats_list = get_cats_info(file_path) # виклик функції

for cat in Cats_list:
    print(cat)
    
