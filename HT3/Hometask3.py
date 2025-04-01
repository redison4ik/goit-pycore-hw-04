from pathlib import Path
import sys
from colorama import init, Fore, Style

init() 

def print_dir_tree(path: Path, indent: str = ""): # вибір кольорів
    for item in sorted(path.iterdir()):
        if item.is_dir(): # для папок
            print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
            print_dir_tree(item, indent + "    ")
        else: # для файлів
            print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до папки як аргумент.")
        print("Приклад: python dir_tree.py C:\\Users\\Тест\\Desktop\\main_folder")
        return

    folder_path = Path(sys.argv[1])

    if not folder_path.exists() or not folder_path.is_dir(): # перевірка шляху
        print(f"Шлях не існує або не є директорією: {folder_path}")
        return

    print_dir_tree(folder_path)

if __name__ == "__main__":
    main()
