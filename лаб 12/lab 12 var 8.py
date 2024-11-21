import random
import cylinder_module  # Імпорт модуля для роботи з циліндрами

# 1. Функції для серійних номерів
def generate_serial_numbers(count=10):
    """Генерує випадкові серійні номери"""
    for _ in range(count):
        serial = '-'.join([''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4)) for _ in range(3)])
        print(serial)

def generate_serials_starting_with_q(count=12):
    """Генерує серійні номери, що починаються з 'Q'"""
    for _ in range(count):
        serial = 'Q' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3)) + \
                 '-'.join([''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4)) for _ in range(2)])
        print(serial)

# 2. Функція для підрахунку голосних у тексті
def count_vowels_in_line(line):
    """Рахує кількість голосних у рядку"""
    vowels = 'аеєиіїоуюяАЕЄИІЇОУЮЯ'
    count = sum(1 for char in line if char in vowels)
    return count

# Основна програма
if __name__ == "__main__":
    # Виклик функцій для серійних номерів
    print("10 випадкових серійних номерів:")
    generate_serial_numbers()

    print("\n12 серійних номерів, які починаються з 'Q':")
    generate_serials_starting_with_q()

    # Робота з текстом
    n = int(input("\nВведіть кількість рядків тексту: "))
    print("Введіть текст:")
    for _ in range(n):
        line = input()
        vowels_count = count_vowels_in_line(line)
        print(f"Кількість голосних у рядку: {vowels_count}")

    # Робота з модулем для циліндра
    radius = float(input("\nВведіть радіус циліндра: "))
    height = float(input("Введіть висоту циліндра: "))

    total_area = cylinder_module.total_surface_area(radius, height)
    lateral_area = cylinder_module.lateral_surface_area(radius, height)
    volume = cylinder_module.cylinder_volume(radius, height)

    print(f"Повна площа поверхні: {total_area:.2f}")
    print(f"Площа бічної поверхні: {lateral_area:.2f}")
    print(f"Об'єм циліндра: {volume:.2f}")
