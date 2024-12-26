import matplotlib.pyplot as plt

from set_up import save_figure, save_transparent_figure

# Данные для столбчатой диаграммы
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

# Построение графика с разными цветами для каждого столбца
colors = ['red', 'blue', 'green', 'orange']
plt.bar(categories, values, color=colors)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

save_figure('bar_chart_of_different_colors')
save_transparent_figure('bar_chart_of_different_colors_transparent')
plt.show()
