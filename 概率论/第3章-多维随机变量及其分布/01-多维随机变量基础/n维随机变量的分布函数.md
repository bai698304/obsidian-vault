# n维随机变量的分布函数

## 定义

对任意的 $n$ 个实数 $x_1, x_2, \cdots, x_n$，称 $n$ 元函数

$$
F(x_1, x_2, \dots, x_n) = P\{X_1 \leqslant x_1, X_2 \leqslant x_2, \dots, X_n \leqslant x_n\}
$$

为 $n$ 维随机变量 $(X_1, X_2, \cdots, X_n)$ 的**分布函数**或随机变量 $X_1, X_2, \cdots, X_n$ 的**联合分布函数**。

## 二维情况（$n = 2$）

对任意的实数 $x, y$，称二元函数

$$
F(x, y) = P\{X \leqslant x, Y \leqslant y\}
$$

为二维随机变量 $(X, Y)$ 的分布函数或 $X$ 和 $Y$ 的联合分布函数，记为 $(X, Y) \sim F(x, y)$。

> $F(x, y)$ 是事件 $A = \{X \leqslant x\}$ 与 $B = \{Y \leqslant y\}$ **同时发生**的概率。

## 性质（二维）

1. **单调性**：$F(x, y)$ 是 $x, y$ 的单调不减函数（固定一个变量，对另一个单调不减）

2. **右连续性**：$F(x, y)$ 是 $x, y$ 的右连续函数
   $$
   \lim_{x \to x_0^{+}} F(x, y) = F(x_0, y),\quad \lim_{y \to y_0^{+}} F(x, y) = F(x, y_0)
   $$

3. **有界性**：$F(-\infty, y) = F(x, -\infty) = F(-\infty, -\infty) = 0$，$F(+\infty, +\infty) = 1$

4. **非负性**：对任意的 $x_1 < x_2, y_1 < y_2$，有
   $$
   P\{x_1 < X \leqslant x_2, y_1 < Y \leqslant y_2\} = F(x_2, y_2) - F(x_2, y_1) - F(x_1, y_2) + F(x_1, y_1) \geqslant 0
   $$

## 相关概念

- [[n维随机变量]]
- [[边缘分布函数]]
- [[随机变量的相互独立性]]
