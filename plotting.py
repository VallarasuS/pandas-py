import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [100, 150, 130, 180],
})

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# ax.plot(np.random.randn(100))
# ax.scatter(df.Month, df.Sales)
ax.bar(df.Month, df.Sales)
# df.plot.area()

plt.savefig("chart.png")
plt.show()

# color
# linestyle
