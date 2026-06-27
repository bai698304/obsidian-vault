# max{X,Y} 和 min{X,Y} 的分布

## $\max\{X, Y\}$ 的分布

设 $(X, Y) \sim F(x, y)$，则 $Z = \max\{X, Y\}$ 的分布函数为

$$
F_{\max}(z) = P\{\max\{X, Y\} \leqslant z\} = P\{X \leqslant z, Y \leqslant z\} = F(z, z)
$$

当 $X$ 与 $Y$ **独立**时：

$$
F_{\max}(z) = F_X(z) \cdot F_Y(z)
$$

## $\min\{X, Y\}$ 的分布

设 $(X, Y) \sim F(x, y)$，则 $Z = \min\{X, Y\}$ 的分布函数为

$$
\begin{aligned}
F_{\min}(z) &= P\{\min\{X, Y\} \leqslant z\} \\
&= P\{X \leqslant z\} + P\{Y \leqslant z\} - P\{X \leqslant z, Y \leqslant z\} \\
&= F_X(z) + F_Y(z) - F(z, z)
\end{aligned}
$$

当 $X$ 与 $Y$ **独立**时：

$$
F_{\min}(z) = 1 - [1 - F_X(z)][1 - F_Y(z)]
$$

## 推广到 $n$ 个独立同分布变量

设 $X_i \stackrel{\mathrm{iid}}{\sim} F(x)$，概率密度为 $f(x)$：

$$
F_{\max}(x) = [F(x)]^{n}, \quad f_{\max}(x) = n[F(x)]^{n-1} f(x)
$$

$$
F_{\min}(x) = 1 - [1 - F(x)]^{n}, \quad f_{\min}(x) = n[1 - F(x)]^{n-1} f(x)
$$

## 相关概念

- [[多维随机变量函数的分布]]
- [[顺序统计量]]
