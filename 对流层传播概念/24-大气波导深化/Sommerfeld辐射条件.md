---
tags:
  - 波导深化
aliases:
  - Sommerfeld Radiation Condition
related:
  - 边界条件
  - 抛物型方程法
---

# Sommerfeld 辐射条件

## 定义

[[抛物型方程法]]中上边界的吸收边界条件。电磁波到达上边界时被**完全吸收**，不向计算区域内反射或透射出计算区域。

## 实现方式

通过窗函数平滑衰减：

**Cosine-taper (Tukey) 窗**：

$$WIND(z) = \begin{cases} 1 & (0 \leqslant z < 0.75 z_{max}) \\ 0.5 + 0.5\cos\left[\frac{4\pi(z-0.75z_{max})}{z_{max}}\right] & (0.75z_{max} \leqslant z \leqslant z_{max}) \end{cases}$$

物理意义：$0 \sim 3z_{max}/4$ 范围内场保持原值，$3z_{max}/4 \sim z_{max}$ 范围场幅平滑衰减至 0。

## 相关概念

- [[边界条件]]
- [[抛物型方程法]]
- [[混合边界条件]]
