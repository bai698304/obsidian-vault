---
tags:
  - 波导深化
aliases:
  - Split-Step Fourier Transform
  - SSFT
related:
  - 抛物型方程法
  - 窄角抛物型方程
  - 宽角抛物型方程
---

# 分步傅里叶变换法 SSFT

## 定义

求解[[抛物型方程法|抛物型方程]]最常用的数值方法，由 Hardin 和 Tappert 于 1973 年提出。适用于理想光滑导体为下边界的情况。

## 宽角 SSFT 结果

$$q(x+\Delta x, z) = \exp[jk(n-2)\Delta x] \,\mathcal{F}^{-1}\left[ \exp(j\Delta x \sqrt{k^2 - p^2}) P_q(x,p) \right]$$

## 窄角 SSFT 结果

$$q(x+\Delta x, z) = \exp\left(jk(n^2-1)\frac{\Delta x}{2}\right) \mathcal{F}^{-1}\left[ \exp\left(\frac{j\Delta x p^2}{2k}\right) P_q(x,p) \right]$$

## 实现

可用 **FFT** 或快速正弦/余弦变换实现。

## DMFT 变体

Dockery 和 Kuttler 在 SSFT 基础上提出的**混合离散傅里叶变换法**（DMFT）。

## 需要注意

当下边界条件不是理想光滑导体或 $\partial n/\partial z \neq 0$ 时 SSFT 会带来误差。

## 相关概念

- [[抛物型方程法]]
- [[窄角抛物型方程]]
- [[宽角抛物型方程]]
- [[离散正弦变换 DST]]
- [[离散余弦变换 DCT]]
