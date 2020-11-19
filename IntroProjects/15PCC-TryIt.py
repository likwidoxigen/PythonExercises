import matplotlib.pyplot as plt

count = range(1, 700)
plotit = [v**3 for v in count]
plt.style.use('bmh')
fig, ax = plt.subplots()

ax.scatter(count, plotit, linewidth=3, c=plotit, cmap=plt.cm.BuGn, s=40)
ax.set_title("Squares", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squared Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14)
plt.show()

# [
#     'grayscale', 'seaborn-ticks', 'seaborn-colorblind', 'seaborn-talk',
#     'seaborn-white', 'seaborn-bright', 'fast', 'seaborn-poster',
#     'dark_background', 'classic', 'seaborn-paper', 'seaborn-pastel',
#     'seaborn-deep', '_classic_test', 'tableau-colorblind10', 'seaborn',
#     'ggplot', 'fivethirtyeight', 'seaborn-notebook', 'seaborn-darkgrid',
#     'seaborn-whitegrid', 'bmh', 'seaborn-muted', 'seaborn-dark-palette',
#     'seaborn-dark', 'Solarize_Light2'
# ]
