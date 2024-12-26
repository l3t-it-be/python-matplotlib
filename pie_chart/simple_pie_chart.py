import matplotlib.pyplot as plt

from set_up import save_figure, save_transparent_figure

# Данные для круговой диаграммы
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [20, 30, 25, 25]

# Построение графика
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

save_figure('simple_pie_chart')
save_transparent_figure('simple_pie_chart_transparent')
plt.show()
