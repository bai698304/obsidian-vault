---
tags:
  - 湍流深化
aliases:
  - Rytov Approximation
related:
  - Born近似
  - 弱起伏与强起伏
  - 信道衰落系数
  - 对数幅度起伏
---

# Rytov 近似

## 定义

求解[[弱起伏与强起伏|弱起伏]]湍流媒质中波动方程的方法，精度高于[[Born近似]]，将场量表示为指数级数形式：

$$U(r) = e^{[\psi_0(r) + \psi_1(r) + \psi_2(r) + \dots]}$$

## 各阶求解

- $\psi_0(r)$：无折射率起伏解，$\nabla^2 \psi_0 + (\nabla \psi_0)^2 + k^2 = 0$
- $\psi_1(r)$：一阶扰动，$\nabla^2 \psi_1 + 2\nabla \psi_0 \cdot \nabla \psi_1 = -(\nabla \psi_1 \cdot \nabla \psi_1 + k^2 \Delta n)$
- $\psi_2(r)$：由 $\psi_2 = \frac{U_2}{U_0} - \frac{1}{2}[\frac{U_1}{U_0}]^2$ 求得

## 应用

Rytov 近似解用于描述湍流对视距传播接收信号**幅度和相位统计特性**。

## 相关概念

- [[Born近似]]
- [[弱起伏与强起伏]]
- [[信道衰落系数]]
- [[对数幅度起伏]]
