---
tags:
  - Weibull分布
  - 雨滴谱
  - 毫米波
date: 2026-05-27
source: "《对流层中的传播、散射特性及其对无线系统的影响》第三章"
---

# Weibull雨滴谱

Sekine 和 Lind 于 1982 年提出的雨滴尺寸分布模型。

表达式：
$$N(D) = N_0 \frac{\eta}{\sigma} \left(\frac{D}{\sigma}\right)^{\eta - 1} \exp\left[-\left(\frac{D}{\sigma}\right)^\eta\right]$$

其中：
- $N_0 = 1000\ m^{-3}$
- $\eta = 0.95 R^{0.14}$
- $\sigma = 0.26 R^{0.42}$

**适用性**：
- 30 GHz 以上毫米波的降雨[[衰减]]与实际测量结果吻合较好
- 用于雷达地杂波研究也有效
