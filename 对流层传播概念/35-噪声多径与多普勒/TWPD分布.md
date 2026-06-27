---
tags:
  - 多径
  - TWPD
  - 包络PDF
  - 双波衰落
  - chapter6
date: 2026-05-27
source: 《对流层中的传播、散射特性及其对无线系统的影响》第6章 6.5节
---

# TWPD分布

**双波 + 漫射功率**（Two-Wave with Diffuse Power）分布，是 I-SLAC 模型中最广义的包络概率密度函数。

$$f(\rho) = \frac{2\rho}{P_{diff}} \exp\left(-\frac{\rho^2}{P_{diff}} - K\right) \cdot \Gamma(\rho, P_{diff}, K, \Delta)$$

- $K = \frac{V_1^2 + V_2^2}{P_{diff}}$：双波功率与漫射功率比
- $\Delta = \frac{2V_1 V_2}{V_1^2 + V_2^2}$：双波幅值比参数
- $\Gamma$：展开函数（含修正 Bessel 函数）

**特例退化**：
- $K \to 0$ → [[起伏场|瑞利分布]]
- $\Delta \to 0$（仅一个主波）→ [[沉降粒子多径信道包络PDF|莱斯分布]]
- $P_{diff} \to 0$（无漫射）→ 双波简单衰落

在[[沉降粒子多径信道包络PDF]]中，当双路径相干强度均远大于非相干强度时适用。