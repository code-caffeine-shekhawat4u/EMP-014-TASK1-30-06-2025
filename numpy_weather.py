import numpy as np

np.random.seed(0)

days = np.arange(1, 8) 

temperature = np.random.normal(loc=30, scale=3, size=7)  

rainfall = np.random.exponential(scale=5.0, size=7)  

print("Day\tTemperature (°C)\tRainfall (mm)")
for i in range(7):
    print(f"{days[i]}\t{temperature[i]:.2f}\t\t\t{rainfall[i]:.2f}")
