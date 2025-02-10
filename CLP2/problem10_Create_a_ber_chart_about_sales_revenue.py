import matplotlib.pyplot as plt

regions = ["North", "South", "East", "West", "Central"]
sales_revenue = [120, 150, 100, 180, 130]

plt.figure(figsize=(8, 5))
plt.bar (regions, sales_revenue, color= ['blue', 'green', 'red', 'purple', 'orange'])

plt.xlabel("Regions")
plt.ylabel("Sales Revenue (in $1000s)")
plt.title("Sales Revenue Comparison Across Regions")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
