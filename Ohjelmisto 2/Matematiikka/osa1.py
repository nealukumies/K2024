import numpy as np

#1. Muunna asteiksi
print("Tehtävä 1")
a = 2.493
b = 0.911
print(f"2,493 rad = {np.degrees(a):.2f} astetta")
print(f"0,911 rad = {np.degrees(b):.2f} astetta")
print("------------------")
#2. Muunna radiaaneiksi
print("Tehtävä 2")
a = 137.7
b = 62.3
print(f"137,7 astetta = {np.radians(a):.2f} rad")
print(f"62,3 astetta = {np.radians(b):.2f} rad")
print("------------------")

# 3. Laadi taulukko, josta esittää seuraavat kulmat radiaaneina
print("Tehtävä 3")
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in A:
  print(f"{i} astetta = {np.radians(i)} rad")
print("------------------")

# 4. Laske suorakulmaisen kolmion hypotenuusa kun
# kateetit  1,6m ja 2,3m
print("Tehtävä 4")
print(f"Suorakulmaisen kolmion hypotenuusa on {np.hypot(1.6, 2.3):.2f} m.")

