import pandas as pd
import matplotlib.pyplot as plt
from utils.constants import ANALYSIS_VARIED_FILE, ANALYSIS_FIXED_FILE

varied = pd.read_csv(ANALYSIS_VARIED_FILE).iloc[10:]
fixed = pd.read_csv(ANALYSIS_FIXED_FILE).iloc[10:]

varied['throughput'] = varied['size'] / varied['time']
fixed['throughput'] = fixed['size'] / fixed['time']

fig, ax = plt.subplots(1, figsize=(16, 9))

fig.suptitle('Varied vs Fixed')

# ax1.set_title("Varied")
# ax2.set_title("Fixed")

ax.plot(varied['du'], varied['throughput'])
ax.plot(fixed['du'], fixed['throughput'])

fig.savefig("throughput10.png")

plt.show()