---
tags:
  - 大气噪声
aliases:
  - G/T
  - Antenna Gain to Noise Temperature Ratio
related:
  - 噪声温度
  - 大气气体辐射噪声
---

# G/T

## 定义

天线增益与系统噪声温度的比值（dB/K），是衡量通信链路质量的核心指标。

$$G = G_{vac} - A_{gas}$$

$$T = T_{vac} + T_{gas}$$

## 大气引起的变化量

$$\Delta(G/T) = -A_{gas}(dB) - 10\lg\left(\frac{T_{vac} + T_{gas}}{T_{vac}}\right)$$

## 系统影响

大气同时降低 G 并增加 T → G/T 下降 → 影响传输速率和误码率。

## 相关概念

- [[噪声温度]]
- [[大气气体辐射噪声]]
- [[大气吸收衰减]]
