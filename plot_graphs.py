import numpy as np
import matplotlib.pyplot as plt

# Delays data
hadoop_delays = [
    [11.711, 1.604, 1.354, 2.066, 1.517],
    [7.56, 1.79, 2.21, 2.676, 2.264],
    [7.013, 1.254, 1.785, 4.178, 3.745],
    [9.041, 1.543, 1.676, 1.714, 1.234],
    [9.845, 6.976, 4.599, 1.945, 1.705]
]

spark_delays = [
    [1.732, 0.479, 0.447, 0.425, 0.417],
    [2.460, 0.357, 0.350, 0.382, 0.370],
    [1.189, 0.776, 0.437, 0.415, 0.394],
    [8.116, 0.377, 0.344, 0.322, 0.302],
    [8.239, 0.604, 0.475, 0.461, 0.409]
]

# Plotting
fig, axs = plt.subplots(1, 5, figsize=(20, 5))
delay_types = ['Carrier', 'NAS', 'Weather', 'Aircraft', 'Security']
iterations = np.arange(1, 6)
bar_width = 0.35

for i in range(5):
    axs[i].bar(iterations, hadoop_delays[i], bar_width, label='Hive')
    axs[i].bar(iterations + bar_width, spark_delays[i], bar_width, label='Spark')
    axs[i].set_title(delay_types[i] + ' Delay')
    axs[i].set_xlabel('Iterations')
    axs[i].set_ylabel('Delay')
    axs[i].legend()

plt.tight_layout()
plt.show()
