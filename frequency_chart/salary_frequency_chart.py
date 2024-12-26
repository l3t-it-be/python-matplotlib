import matplotlib.pyplot as plt
import numpy as np

from set_up import save_figure, save_transparent_figure

# Генерация данных: зарплаты сотрудников в тыс. долларов
salaries = np.random.normal(
    50, 15, 1000
)  # Средняя зарплата = 50 тыс., стандартное отклонение = 15 тыс., 1000 сотрудников

# Построение гистограммы
plt.figure(figsize=(8, 6))
plt.hist(salaries, bins=30, edgecolor='black', color='skyblue', alpha=0.7)

# Добавление подписей
plt.title('Distribution of Salaries in a Company', fontsize=14)
plt.xlabel('Salary (in thousands of dollars)', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)

# Добавление средней линии для акцента
mean_salary = np.mean(salaries)
plt.axvline(
    mean_salary,
    color='red',
    linestyle='dashed',
    linewidth=1.5,
    label=f'Mean Salary: ${mean_salary:.2f}K',
)

# Легенда
plt.legend()

save_figure('salary_frequency_chart')
save_transparent_figure('salary_frequency_chart_transparent')
plt.show()
