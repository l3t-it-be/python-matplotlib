import matplotlib.pyplot as plt
import numpy as np

from set_up import save_figure, save_transparent_figure

# Генерация случайных данных 10x12
data = np.random.rand(10, 12)

# Построение тепловой карты
plt.figure(figsize=(8, 6))
plt.imshow(data, cmap='coolwarm', aspect='auto')

# Добавление цветовой шкалы
plt.colorbar(label='Value')

# Подписи к графику
plt.title('Heatmap using Matplotlib')
plt.xlabel('X axis')
plt.ylabel('Y axis')

save_figure('heatmap_using_matplotlib')
save_transparent_figure('heatmap_using_matplotlib_transparent')
plt.show()
