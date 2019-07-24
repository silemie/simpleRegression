### 水位线线性拟合

这是一个简单的基于水位线与时间数据的进行线性回归计算的程序，基于Python 3.6实现。

**执行语句**

```
python3 regression.py <data_path> <outliers_command>
```

**输入**

- <data_path>
  输入数据文件路径，目前可支持`txt`文本格式输入

- <outliers_command>
  此为是否要移除特异值的指令，如果需要移除特异值，输入`yes`，否则输入`no`

- 输入示范

  ```
  python3 regression.py data.txt yes
  ```

**输出**

- 移除的特异值
- 最后一次记录时间预测的水位线
- 基于输入数据的散点图与拟合的回归直线（基于`matplotlib`包，可移除此部分）

**实现算法**

- 最小二乘法：
  实现公式

  ```latex
  \frac{\sum_{1}^{n}{x_i * y_i} - n * mean_x * mean_y}{\sum_{1}^{n}{{x_i}^2} - n * {mean_x}^2}
  ```

  其中`n`为数据的大小。

- 特异值移除：
  该程序使用区间值方法来移除特异值，通过计算水位线的均值与标准差，筛选出高于`mean + 2std` 与低于`mean - 2std`的水位值，将其标记为特异值并移除。



