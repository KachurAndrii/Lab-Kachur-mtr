import numpy as np

# Матриця виграшів F
F = np.array([
    [3, 8, 7, 9],
    [5, 6, 3, 8],
    [4, 9, 4, 4],
    [6, 4, 5, 4]
])

# Ймовірності для критерія середньоквадратичного відхилення
probabilities = np.array([0.25, 0.15, 0.4, 0.2])

# (1) Критерій середньоквадратичного відхилення
# Обчислюємо сподіваний виграш для кожного рішення
expected_values = F @ probabilities

# Обчислюємо середньоквадратичне відхилення для кожного рішення
squared_differences = (F - expected_values[:, None]) ** 2
variance = (squared_differences @ probabilities)
std_deviation = np.sqrt(variance)

# Знаходимо рішення з мінімальним середньоквадратичним відхиленням
min_std_deviation = np.argmin(std_deviation) + 1  # Додаємо 1 для нумерації з 1

# (2) Критерій Вальда
# Обчислюємо мінімальні виграші для кожного рішення
min_values = F.min(axis=1)

# Знаходимо рішення з максимальним мінімальним виграшем
wald_criterion = np.argmax(min_values) + 1  # Додаємо 1 для нумерації з 1

# (3) Компромісний критерій
# Вводимо ваги u1 = 1/3 і u5 = 2/3
u1 = 1 / 3
u5 = 2 / 3

# Обчислюємо компромісний критерій
compromise_values = u1 * (-std_deviation) + u5 * min_values
compromise_solution = np.argmax(compromise_values) + 1  # Додаємо 1 для нумерації з 1

# Виведення результатів
print("Результати:")
print(f"Мінімальне середньоквадратичне відхилення: x{min_std_deviation}")
print(f"Критерій Вальда: x{wald_criterion}")
print(f"Компромісне рішення: x{compromise_solution}")

# Побудова ієрархічної схеми
import networkx as nx
import matplotlib.pyplot as plt

# Побудова графу
G = nx.DiGraph()
G.add_edges_from([
    ("Мета", "Критерій 1: Мінімізація СКВ"),
    ("Мета", "Критерій 2: Вальда"),
    ("Критерій 1: Мінімізація СКВ", f"Оптимальне рішення: x{min_std_deviation}"),
    ("Критерій 2: Вальда", f"Оптимальне рішення: x{wald_criterion}"),
    ("Мета", f"Компромісне рішення: x{compromise_solution}")
])

# Візуалізація графу
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Ієрархічна схема вибору рішення")
plt.show()
