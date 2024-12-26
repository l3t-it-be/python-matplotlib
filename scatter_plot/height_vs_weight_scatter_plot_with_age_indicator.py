import matplotlib.pyplot as plt
import numpy as np

from set_up import save_figure, save_transparent_figure

# Реальные данные: рост (в см), вес (в кг) и возраст (в годах)
heights = [150, 160, 165, 170, 175, 180, 185, 190, 195, 200]
weights = [50, 55, 65, 70, 72, 75, 78, 85, 90, 95]
ages = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65]  # Возраст будет влиять на цвет

# Генерация размера точек для визуализации на основе веса
sizes = np.array(weights) * 10  # Пропорциональные размеры точек

# Построение диаграммы рассеяния
plt.scatter(heights, weights, s=sizes, c=ages, cmap='coolwarm', alpha=0.8)

# Добавление цветовой шкалы, отображающей возраст
plt.colorbar(label='Age (years)')

# Подписи
plt.title('Height vs Weight Scatter Plot with Age Indicator')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

save_figure('height_vs_weight_scatter_plot_with_age_indicator')
save_transparent_figure(
    'height_vs_weight_scatter_plot_with_age_indicator_transparent'
)

# Показ графика
plt.show()
