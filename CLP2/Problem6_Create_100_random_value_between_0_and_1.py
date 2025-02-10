import numpy as np

random_array = np.random.rand(100)

normalized_array = (random_array - np.min(random_array)) / (np.max(random_array) - np.min(random_array))
print("First 10 values:", normalized_array[:10])
