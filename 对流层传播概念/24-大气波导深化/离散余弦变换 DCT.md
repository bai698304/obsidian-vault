---
tags:
  - 波导深化
aliases:
  - Discrete Cosine Transform
  - DCT
related:
  - 初始场确定
  - 离散正弦变换 DST
  - 抛物型方程法
---

# 离散余弦变换 DCT

## 定义

将垂直极化初始场从 P 空间变换到 Z 空间的离散变换。

## 正变换 (DCT)

$$F_C(i\Delta p) = \sum_{m=1}^{N-1} \omega_C(m\Delta z) \cos\left(\frac{\pi i m}{N}\right)$$

## 逆变换 (IDCT)

$$\omega_C(m\Delta z) = \frac{2}{N} \sum_{m=1}^{N-1} F_C(i\Delta p) \cos\left(\frac{\pi i m}{N}\right)$$

## 应用

[[初始场确定|垂直极化初始场]]的 P 空间 → Z 空间转换。

## 相关概念

- [[初始场确定]]
- [[离散正弦变换 DST]]
- [[抛物型方程法]]
