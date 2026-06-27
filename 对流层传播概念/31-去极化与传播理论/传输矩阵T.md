---
tags:
  - 去极化
  - 传输矩阵
  - chapter6
date: 2026-05-27
source: 《对流层中的传播、散射特性及其对无线系统的影响》第6章 6.1.4节
---

# 传输矩阵T

[[去极化微分方程]] $dE/dz = ME$ 的解：

$$E = T E^0$$

$E^0$ 为 $z=0$ 处入射场，$T$ 的元素由[[特征极化传播常数]] $\lambda_1, \lambda_2$ 和特征极化倾角 $\phi$ 表示。

$$T_{11} = \cos^2\phi \, e^{\lambda_2 z} (G + \tan^2\phi)$$
$$T_{12} = T_{21} = -\cos^2\phi \, e^{\lambda_2 z} (1 - G) \tan\phi$$
$$T_{22} = \cos^2\phi \, e^{\lambda_2 z} (1 + G \tan^2\phi)$$

其中 $G = e^{(\lambda_1 - \lambda_2)z}$。

$T$ 矩阵直接决定[[交叉极化分辨率 XPD]]。