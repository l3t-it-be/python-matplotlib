import matplotlib.pyplot as plt
import numpy as np

from set_up import save_figure, save_transparent_figure

# Данные для гистограммы
data = np.random.randn(1000)

# Построение графика
plt.hist(data, bins=30, alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

save_figure('simple_frequency_chart')
save_transparent_figure('simple_frequency_chart_transparent')
plt.show()
