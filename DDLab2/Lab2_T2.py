salary = 5000
spend = 6000
months = 10
increase = 0.03

money_capital = int(sum(max(spend*(1 + increase)**month - salary, 0) for month in range(months)))

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)