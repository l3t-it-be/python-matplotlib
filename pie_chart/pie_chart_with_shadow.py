import matplotlib.pyplot as plt

from set_up import save_figure, save_transparent_figure

# Данные для круговой диаграммы
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [20, 30, 25, 25]
explode = (0, 0.1, 0, 0)  # Величина смещения для второго сектора
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode)
plt.title('Pie Chart with Shadow')

save_figure('pie_chart_with_shadow')
save_transparent_figure('pie_chart_with_shadow_transparent')
plt.show()
