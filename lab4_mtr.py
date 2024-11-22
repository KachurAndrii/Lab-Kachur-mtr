import numpy as np
from scipy.optimize import minimize

# Вхідні дані
expected_returns = np.array([0.1, 0.2, 0.5])  # Сподівані норми прибутку
std_devs = np.array([0.02, 0.1, 0.2])  # Середньоквадратичні відхилення
correlations = np.array([
    [1.0, 0.0, 0.0],
    [0.0, 1.0, -0.6],
    [0.0, -0.6, 1.0],
])

# Обчислення ковараційної матриці
cov_matrix = np.outer(std_devs, std_devs) * correlations

# Функція для обчислення ризику портфеля
def portfolio_risk(weights):
    return np.sqrt(weights.T @ cov_matrix @ weights)

# Функція для обчислення дохідності портфеля
def portfolio_return(weights):
    return np.dot(weights, expected_returns)

# Обмеження: сума ваг = 1
def constraint_sum_weights(weights):
    return np.sum(weights) - 1

# Межі для ваг (0 <= w <= 1)
bounds = [(0, 1) for _ in range(len(expected_returns))]

# Початкове значення ваг
initial_weights = np.array([1/3, 1/3, 1/3])

# (a) Оптимальна структура для збереження капіталу (мінімізація ризику)
constraints = ({'type': 'eq', 'fun': constraint_sum_weights})
result_min_risk = minimize(portfolio_risk, initial_weights, bounds=bounds, constraints=constraints)
weights_min_risk = result_min_risk.x

# (b) Оптимальна структура для збільшення приросту капіталу при mc = 30%
mc = 0.3
constraints = (
    {'type': 'eq', 'fun': constraint_sum_weights},
    {'type': 'ineq', 'fun': lambda w: portfolio_return(w) - mc}  # Дохідність >= mc
)
result_target_return = minimize(portfolio_risk, initial_weights, bounds=bounds, constraints=constraints)
weights_target_return = result_target_return.x

# (c) Оптимальна структура для максимізації приросту капіталу при σc = 15%
sigma_c = 0.15
constraints = (
    {'type': 'eq', 'fun': constraint_sum_weights},
    {'type': 'ineq', 'fun': lambda w: sigma_c - portfolio_risk(w)}  # Ризик <= σc
)
result_max_return = minimize(lambda w: -portfolio_return(w), initial_weights, bounds=bounds, constraints=constraints)
weights_max_return = result_max_return.x

# (d) Обчислення сподіваної норми прибутку та ризику для всіх портфелів
results = {
    "Мінімізація ризику": weights_min_risk,
    "Збільшення приросту капіталу (mc = 30%)": weights_target_return,
    "Максимальний приріст капіталу (σc = 15%)": weights_max_return,
}

print("Результати оптимізації портфелів:\n")
for desc, weights in results.items():
    ret = portfolio_return(weights)
    risk = portfolio_risk(weights)
    print(f"{desc}:\n  Ваги: {weights.round(4)}\n  Сподівана норма прибутку: {ret:.4f}\n  Ризик: {risk:.4f}\n")
