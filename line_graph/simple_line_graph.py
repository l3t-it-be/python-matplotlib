from matplotlib import pyplot as plt

from set_up import save_figure, save_transparent_figure

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y)

# Добавление подписей к осям
plt.xlabel('X ось')
plt.ylabel('Y ось')

# Заголовок
plt.title('Простой линейный график')

save_figure('simple_line_graph')
save_transparent_figure('simple_line_graph_transparent')

# Показать график
plt.show()
