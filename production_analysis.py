# Production Data Analysis
# Weekly production analysis using Python

# -----------------------------
# 1. Production Data
# -----------------------------

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
production = [120, 145, 98, 160, 135, 110, 152]

# Combine days and production values
daily_production = list(zip(days, production))

print("Daily Production:")
print(daily_production)


# -----------------------------
# 2. Basic Production Metrics
# -----------------------------

total_production = sum(production)
maximum_production = max(production)
minimum_production = min(production)

average_production = round(
    total_production / len(production), 2
)

production_range = maximum_production - minimum_production

print("\nProduction Metrics:")
print("Total production:", total_production)
print("Maximum production:", maximum_production)
print("Minimum production:", minimum_production)
print("Average production:", average_production)
print("Production range:", production_range)


# -----------------------------
# 3. Identify High-Production Days
# -----------------------------

high_production = list(
    filter(lambda x: x > 130, production)
)

print("\nProduction above 130 units:")
print(high_production)


# -----------------------------
# 4. Convert Production to Hundreds
# -----------------------------

production_in_hundreds = list(
    map(lambda x: x / 100, production)
)

print("\nProduction in hundreds:")
print(production_in_hundreds)


# -----------------------------
# 5. Sort Production Values
# -----------------------------

ascending_production = sorted(production)
descending_production = sorted(production, reverse=True)

print("\nProduction - Ascending:")
print(ascending_production)

print("\nProduction - Descending:")
print(descending_production)
