# Модуль для роботи з математичними операціями
import math

# Дані для двох фірм
companies = [
    {"name": "Company 1", "probability_1": 0.7, "profit_1": 9000, "probability_2": 0.3, "profit_2": 7000},
    {"name": "Company 2", "probability_1": 0.4, "profit_1": 13000, "probability_2": 0.6, "profit_2": 7500}
]

# Функція для обчислення середнього прибутку
def average_profit(data):
    avg_profit = (data['probability_1'] * data['profit_1']) + (data['probability_2'] * data['profit_2'])
    return avg_profit

# Функція для оцінки ризику через дисперсію та відхилення
def calculate_standard_deviation(data, avg_profit):
    variance = (data['probability_1'] * (data['profit_1'] - avg_profit) ** 2) + \
               (data['probability_2'] * (data['profit_2'] - avg_profit) ** 2)
    std_deviation = math.sqrt(variance)
    return std_deviation

# Обчислюємо результати для кожної компанії
company_results = []
for company in companies:
    avg_profit = average_profit(company)
    risk = calculate_standard_deviation(company, avg_profit)
    company_results.append({"name": company["name"], "avg_profit": avg_profit, "risk": risk})

# Виводимо результати для кожної компанії
for result in company_results:
    print(f"{result['name']}: Середній прибуток = {result['avg_profit']} грн, Ризик = {result['risk']} грн")

# Знаходимо компанію з найменшим ризиком
lowest_risk_company = min(company_results, key=lambda x: x['risk'])
print(f"\nНайменший ризик у компанії: {lowest_risk_company['name']}")
