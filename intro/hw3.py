import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pprint as p


data_df = pd.read_csv('/Users/keemsunguk/projects/intro/data/tr_eikon_eod_data.csv',
                      index_col=0, parse_dates=True)

#p.pprint(data_df)
print(data_df.shape)
data_df[list(data_df.columns)].plot(subplots=True, figsize=(5, 20))
plt.savefig('/Users/keemsunguk/projects/intro/data/hw3.png')
