import matplotlib.pyplot as plt
import numpy as np

from set_up import save_figure, save_transparent_figure

# Данные для столбчатой диаграммы
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

# Нормализуем значения для использования в цветовой карте (значения от 0 до 1)
norm_values = np.array(values) / max(values)

# Используем colormap для задания цвета в зависимости от значения
colors = plt.cm.viridis(
    norm_values
)  # Можно использовать другие colormap, например, 'plasma', 'inferno', 'coolwarm'

# Построение графика
plt.bar(categories, values, color=colors)
plt.title('Bar Chart with Gradient Colors')
plt.xlabel('Categories')
plt.ylabel('Values')

save_figure('bar_chart_with_gradient_colors')
save_transparent_figure('bar_chart_with_gradient_colors_transparent')
plt.show()
