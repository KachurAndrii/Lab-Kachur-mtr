import numpy as np

# Матриця прибутків (тис. дол.)
F = np.array([
    [45, 32, 16],  # x1
    [15, 8, 10],   # x2
    [20, 18, 14],  # x3
    [30, 23, 7]    # x4
])

# Ймовірності попиту
probabilities = np.array([0.5, 0.3, 0.2])  # Наприклад, великий, середній, низький попит

# Критерій Байєса (сподіваний прибуток)
expected_profits = F @ probabilities

# Мінімаксний критерій (мінімізація втрат)
min_profits = F.min(axis=1)

# Критерій Ходжеса-Лемана
def hodges_lehmann(lambda_value):
    return lambda_value * expected_profits + (1 - lambda_value) * min_profits

# Аналіз для λ в [0; 1] з кроком 0.1
lambdas = np.linspace(0, 1, 11)
results = []

for lambda_value in lambdas:
    hl_values = hodges_lehmann(lambda_value)
    best_choice = np.argmax(hl_values) + 1  # Нумерація варіантів (x1, x2, x3, x4)
    results.append((lambda_value, best_choice, hl_values))

# Виведення результатів
print("Результати аналізу:")
for lambda_value, best_choice, hl_values in results:
    print(f"λ = {lambda_value:.1f}: Найкращий вибір = x{best_choice}, Значення HL = {hl_values.round(2)}")
