import matplotlib.pyplot as plt
import numpy as np

from set_up import save_figure, save_transparent_figure

# Данные для диаграммы рассеяния
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

# Построение графика
plt.scatter(x_scatter, y_scatter)
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')

save_figure('simple_scatter_plot')
save_transparent_figure('simple_scatter_plot_transparent')
plt.show()
