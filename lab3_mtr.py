import numpy as np

# Функція корисності
def utility(x):
    return (x + 5) ** 2 / 15

# Дані з таблиці
profits = {
    "I": [10, -5, -5],
    "II": [-5, -5, 10],
    "III": [1.5, 1.5, 0],
    "IV": [0, 0, 0],
}
probabilities = [0.5, 0.1, 0.4]  # Ймовірності

# Обчислення очікуваної корисності для кожного рішення
expected_utilities = {}

for decision, outcomes in profits.items():
    utilities = [utility(x) for x in outcomes]
    expected_utility = np.dot(utilities, probabilities)  # Скалярний добуток
    expected_utilities[decision] = expected_utility

# Визначення найкращого рішення
best_decision = max(expected_utilities, key=expected_utilities.get)

# Результати
print("Очікувані корисності для кожного рішення:")
for decision, eu in expected_utilities.items():
    print(f"{decision}: {eu:.4f}")

print(f"\nНайкраще рішення: {best_decision}")
