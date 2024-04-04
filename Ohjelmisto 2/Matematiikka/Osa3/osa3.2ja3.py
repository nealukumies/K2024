#2. Kuvan oletuskoko 6.4 * 4.8 tuumaa. Haluat tehdä kuvaajan väliltä -3π - 3π.
# Levennä kuva kolminkertaiseksi ja vaihdä käyrien värit sekä piirtotyyli.
# Lisää myöskin kuvaan selite.
#3. Akselitkin ovat vähän tylsät. Aseta akselien tekstit muoton π, π/2 jne ...


import numpy as np
import matplotlib.pyplot as plt

pii = 3*np.pi

X = np.linspace(-pii, pii, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.figure(figsize=(3 * 6.4, 4.8))
plt.plot(X,C, color='pink', linewidth=5, label='Cos')
plt.plot(X,S, color='purple', linewidth=5, label='Sin')
plt.xticks(ticks=np.arange(-pii, pii+1, np.pi), labels=[r'$-3\pi$', r'$-2\pi$', r'$-\pi$', '0', r'$\pi$', r'$2\pi$', r'$3\pi$'])
plt.yticks(ticks=[-1, 0,  1])
plt.legend(loc='upper left')
plt.show()

