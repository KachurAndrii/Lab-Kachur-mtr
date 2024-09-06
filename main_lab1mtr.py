def calculate_utility(sunny_home, rainy_home, sunny_forest, rainy_forest, rain_chance):
    
    home_utility = rain_chance * rainy_home + (1 - rain_chance) * sunny_home

    forest_utility = rain_chance * rainy_forest + (1 - rain_chance) * sunny_forest

    print(f"Оцінка комфортності залишитися вдома: {home_utility}")
    print(f"Оцінка комфортності прогулянки в лісі: {forest_utility}")

    if home_utility > forest_utility:
        return "Рекомендація: Залишайся вдома і насолоджуйся комфортом!"
    elif home_utility == forest_utility:
        return "Рекомендація: Обидва варіанти однаково хороші!"
    else:
        return "Рекомендація: Вирушай до лісу, природа на тебе чекає!"

sunny_home = float(input("Як ти почуваєшся вдома в сонячний день? (1-10): "))
rainy_home = float(input("Як ти почуваєшся вдома під час дощу? (1-10): "))

sunny_forest = float(input("Як ти почуваєшся в лісі в сонячний день? (1-10): "))
rainy_forest = float(input("Як ти почуваєшся в лісі під час дощу? (1-10): "))
rain_chance = float(input("Яка ймовірність дощу? (0-1): "))

decision = calculate_utility(sunny_home, rainy_home, sunny_forest, rainy_forest, rain_chance)
print(decision)
