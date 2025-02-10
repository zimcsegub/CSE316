import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [22, 24, 21, 23, 25, 26, 24]

plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b', linewidth=2, markersize=6, label="Temperature (°C)")

plt.xlabel("Days of the Week")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")
plt.legend()
plt.grid(True)

plt.show()
