times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians', 'Internacional', 'Fluminense', 'Athletico-PR', 'América-MG', 'Cuiabá', 'Ceará', 'Santos', 'São Paulo', 'Atlético-GO', 'Bahia', 'Juventude', 'Sport', 'Grêmio', 'Chapecoense')

print('Os 5 primeiros times são:',times[:5])
print('Os 4 últimos times são:',times[len(times)-4:])
print('Os times em ordem alfabética são:',sorted(times))
print('A Chapecoense está em',times.index('Chapecoense')+1,'º lugar')
