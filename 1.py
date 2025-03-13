print("Визначення оцінки студента")
print("=" * 42)

while True:
    try:
        score = int(input("Введіть кількість балів (0-100): "))

        if score < 0 or score > 100:
            print("Некоректний бал. Введіть число від 0 до 100.")
        elif score <= 49:
            print("Незадовільно")
        elif score <= 69:
            print("Задовільно")
        elif score <= 89:
            print("Добре")
        else:
            print("Відмінно")

    except ValueError:
        print("Помилка! Введіть ціле число.")

    ans = input("Продовжити? (1 - так, 2 - ні): ").strip()
    while ans != "1":
        print("Будь ласка, введіть 1 для продовження або 2 для виходу.")
        ans = input("Продовжити? (1 - так, 2 - ні): ")
    if ans == "2":
        break

print("Програма закінчена")
