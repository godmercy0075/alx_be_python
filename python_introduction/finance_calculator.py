# Personal Finance Calculator
# This script helps users calculate their monthly budget, savings, and investment growth.
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
# Add 5% interest on savings
#simple annual interest = 0.05
# annual_savings = monthly_savings * 12
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
# Display results
print(f"Your monthly savings are  ${monthly_savings:.2f}")
print(f"Your projected savings after one year, with interest is ${projected_savings:.2f}")