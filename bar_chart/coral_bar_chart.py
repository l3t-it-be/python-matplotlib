import matplotlib.pyplot as plt

from set_up import save_figure, save_transparent_figure

# Данные для столбчатой диаграммы
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

# Построение графика с указанием цвета столбцов
plt.bar(
    categories, values, color='coral'
)  # Можно указать любой цвет, например, 'green', 'red', 'blue', и т.д.
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

save_figure('coral_bar_chart')
save_transparent_figure('coral_bar_chart_transparent')
plt.show()
