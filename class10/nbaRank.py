nbaTop20 = ('Boston', 'Phoenix', 'Golden State', 'Utah', 'Memphis', 'Miami', 'Milwaukee', 'Dallas', 'Philadelphia', 'Denver',
           'Minnesota', 'Brooklyn', 'Toronto', 'Atlanta', 'Cleveland', 'Charlotte', 'LA Clippers', 'New York', 'New Orleans', 'Chicago')

print('TOP 5 NBA TEAMS - 2022')
print('=' * 20)
print(nbaTop20[:5])
print('=' * 20)

print('BOTTOM 4')
print('-' * 20)
print(nbaTop20[-4:])

print('ALPHA-SORTED')
print('-' * 20)
print(sorted(nbaTop20))

print(f'\nChicago is on position: {nbaTop20.index("Chicago") + 1}')