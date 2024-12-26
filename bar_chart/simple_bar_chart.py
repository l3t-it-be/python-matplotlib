import matplotlib.pyplot as plt

from set_up import save_figure, save_transparent_figure

# Данные для столбчатой диаграммы
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

# Построение графика
plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

save_figure('simple_bar_chart')
save_transparent_figure('simple_bar_chart_transparent')
plt.show()
