---
tags:
  - 大气湍流
  - 随机场
aliases:
  - Kolmogorov Spectrum
  - -11/3 Power Law
related:
  - 空间谱
  - Kolmogorov湍流能谱定律
  - 折射率结构常数 Cn
---

# Kolmogorov 空间谱

## 定义

基于 [[Kolmogorov湍流能谱定律]] 导出的空间谱形式。

## 介电常数起伏谱（惯性子区）

$$\Phi_{\Delta\varepsilon_r}(K) = 0.033 C_{GA}^2 K^{-11/3}$$

## 折射率起伏谱（Tatarskii 谱）

### 惯性子区

$$\Phi_{\Delta n}(K) = 0.033 C_n^2 K^{-11/3} \quad \left(\frac{2\pi}{l_{outer}} \ll K \ll \frac{2\pi}{l_{inner}}\right)$$

### 耗散区（含截断）

$$\Phi_{\Delta n}(K) = 0.033 C_n^2 K^{-11/3} \exp\left(-\frac{K^2}{K_m^2}\right)$$

其中 $K_m = 5.91 / l_{inner}$。

## -11/3 幂律的由来

从 [[Kolmogorov湍流能谱定律|-5/3 能谱定律]] + 结构函数 2/3 幂律 → 傅里叶变换 → 空间谱 -11/3 幂律。

## 其他谱模型

- **布克谱**：$\Phi = Ar_0^3/[\pi^2(1+K^2r_0^2)^2]$
- **诺顿谱**：各向异性含克唐纳函数

## 相关概念

- [[空间谱]]
- [[折射率结构常数 Cn]]
- [[Kolmogorov湍流能谱定律]]
- [[结构函数]]
