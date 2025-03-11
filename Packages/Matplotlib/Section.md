### Draw Section using matplotlib
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(0, 0, color='red', s=100, label='Center Of Gravity')
ax.add_patch(plt.Circle((0, 0), 1, color='blue', fill=False, label='Earth'))
ax.add_patch(plt.Rectangle((-1, -1), 2, 2, color='green',
             fill=False, label='Spacecraft'))
ax.add_line(plt.Line2D((-1, 1), (0, 0), color='black', label='Diameter'))
ax.annotate("", xy=(0, 1), xytext=(0, -1),
            arrowprops=dict(arrowstyle="<->", color='black'))
ax.text(0.1, 0.5, 'Height=1', rotation=0, color='black')
plt.show()

```
