---
tags:
  - 电磁特性参数
aliases:
  - M
  - Modified Refractivity
related:
  - 折射指数 N
  - 大气波导
  - N单位与M单位
---

# 修正折射指数 $M$

## 定义

在[[折射指数 N]]基础上定义的物理量，用于便于描述大气的[[折射]]效应。

$$M(z) = \operatorname{Re}[N(z)] + 0.157z$$

- $z$：空间某点距离地面的高度 (m)
- 单位：[[N单位与M单位|M 单位]]

## 波导判据

$M$ 是判断[[大气波导]]的核心参数：

$$\frac{dM}{dh} < 0 \quad \Rightarrow \quad \text{大气波导}$$

等价于[[波导形成条件]]中 $\frac{dN_{Re}}{dh} < -0.157$ m⁻¹。

## 波导特征参数

- [[波导强度]] $\Delta M$：波导层内 $M$ 的取值范围
- [[穿透角]] $\theta_c = \sqrt{2 \times 10^{-6} \Delta M}$

## 相关概念

- [[折射指数 N]]
- [[大气波导]]
- [[波导形成条件]]
- [[N单位与M单位]]
