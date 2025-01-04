# Analyse simple de consommation d'énergie
import matplotlib.pyplot as plt

# Données fictives
jours = ["Lun", "Mar", "Mer", "Jeu", "Ven", "Sam", "Dim"]
consommation = [120, 150, 180, 170, 200, 220, 190]

# Visualisation
plt.figure(figsize=(8,5))
plt.bar(jours, consommation, color='skyblue')
plt.title("Consommation d'énergie hebdomadaire (kWh)")
plt.xlabel("Jour")
plt.ylabel("Consommation (kWh)")
plt.show()
