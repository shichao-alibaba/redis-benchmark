import numpy as np
import pandas as pd

size = 10000000

mu, sigma = 0, 1
key = np.random.normal(mu, sigma, size)
# formatting 
key = np.around((key + 5) * size / 10).astype(int)
key_title = 'keys total:' + str(size)

dataframe = pd.DataFrame({key_title:key})
dataframe.to_csv("gauss_data.csv", index=False)