from pathlib import Path

file_path = Path(__file__).parent / "Salary" / "Salary.txt"

with open(file_path, 'r', encoding='utf-8') as fh:
    lines = [line.strip() for line in fh if line.strip()]  # прибираємо порожні рядки

total_salary = 0
for line in lines:
    name, salary = line.split(",")
    total_salary += int(salary)

average_salary = total_salary / len(lines)

print(f"Загальна сума: {total_salary}")
print(f"Середня сума: {average_salary}")