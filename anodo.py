import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Surface roughness data at 500x and 2000x magnifications
data_500x = np.array([22.91, 21.17, 25.43, 24.32, 25.11])
data_2000x = np.array([26.17, 23.28, 23.09, 22.52, 24.50])

# Calculate the means and standard deviations for each magnification
mean_500x = np.mean(data_500x)
std_dev_500x = np.std(data_500x, ddof=1)
mean_2000x = np.mean(data_2000x)
std_dev_2000x = np.std(data_2000x, ddof=1)

# Calculate the mean absolute error and the standard deviation of the error
absolute_errors = np.abs(np.concatenate([data_500x, data_2000x]) - 20)
mean_absolute_error = np.mean(absolute_errors)
std_dev_absolute_error = np.std(absolute_errors, ddof=1)

# Bar plot for each magnification
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.bar(range(len(data_500x)), data_500x, color='skyblue')
plt.axhline(y=20, color='r', linestyle='--', label='Ideal Value')
plt.xlabel('Region')
plt.ylabel('Roughness')
plt.title('Roughness at 500x Magnification')
plt.legend()

plt.subplot(1, 2, 2)
plt.bar(range(len(data_2000x)), data_2000x, color='lightgreen')
plt.axhline(y=20, color='r', linestyle='--', label='Ideal Value')
plt.xlabel('Region')
plt.ylabel('Roughness')
plt.title('Roughness at 2000x Magnification')
plt.legend()

plt.tight_layout()
plt.show()

# Print the results
print("Roughness analysis results:")
print(f"Mean at 500x magnification: {mean_500x:.2f}")
print(f"Standard deviation at 500x magnification: {std_dev_500x:.2f}")
print(f"Mean at 2000x magnification: {mean_2000x:.2f}")
print(f"Standard deviation at 2000x magnification: {std_dev_2000x:.2f}")
print(f"Mean absolute error: {mean_absolute_error:.2f}")
print(f"Standard deviation of absolute error: {std_dev_absolute_error:.2f}")

