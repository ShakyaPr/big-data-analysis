import matplotlib.pyplot as plt
import numpy as np

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

queries = np.array(["YearlyCarrierDelay", "YearlyNASDelay", "YearlyWeatherDelay", "YearlyLateAircraftDelay", "YearlySecurityDelay"])
hive_delays = np.array([np.mean(hadoop_delays[0]), np.mean(hadoop_delays[1]), np.mean(hadoop_delays[2]), np.mean(hadoop_delays[3]), np.mean(hadoop_delays[4])])
spark_delays = np.array([np.mean(spark_delays[0]), np.mean(spark_delays[1]), np.mean(spark_delays[2]), np.mean(spark_delays[3]), np.mean(spark_delays[4])])

# Round the values to two decimal places
rounded_hive_delays = np.round(hive_delays, 2)
rounded_spark_delays = np.round(spark_delays, 2)
# Create a figure and axis
fig, ax = plt.subplots()

# Create a table with data
table_data = np.vstack((queries, rounded_hive_delays, rounded_spark_delays)).T
table = plt.table(cellText=table_data, colLabels=["Queries", "Hive Delays", "Spark Delays"],
                  cellLoc='center', loc='center', colColours=['#f5f5f5']*3, cellColours=[['#f5f5f5']*3]*len(queries))

# Hide the axes
ax.axis('off')

# Adjust the table layout
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

# Show the plot
plt.show()


