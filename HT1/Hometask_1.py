from pathlib import Path

def total_salary(path: Path):
    if not path.exists(): # чи існує файл
        print("Файл не знайдено:", path)
        return

    with path.open('r', encoding='utf-8') as fh:# відкрити для читання
        lines = [line.strip() for line in fh if line.strip()]

    total = 0
    for line in lines:# відділяємо необхідні значення
        try:
            name, salary = line.split(',')
            total += int(salary)
        except ValueError:
            print(f"Невірний формат рядка: {line}")

    average = total / len(lines) if lines else 0 # середнє значення

    print(f"Загальна сума: {total}")
    print(f"Середня сума: {average}")

file_path = Path(__file__).parent / "Salary" / "Salary.txt" # шлях
total_salary(file_path) # виклик функції