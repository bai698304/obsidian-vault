---
tags:
  - 去极化
  - XPD预报
  - CPA
  - Nowland
  - ITU-R
  - Van de Kamp
  - chapter6
date: 2026-05-27
source: 《对流层中的传播、散射特性及其对无线系统的影响》第6章 6.3.1.2节
---

# 基于CPA的XPD预报模型

利用[[同极化衰减 CPA]]（$A_p$）估算[[交叉极化分辨率 XPD]]的半经验模型族。

**通用形式**：$\mathrm{XPD}_p = U - V \lg A_p + C_\tau + C_\theta + C_\sigma$

| 模型 | 适用频段 | 特征 |
|------|---------|------|
| **Nowland** (1977) | 8~35 GHz | 奠基性模型，$V = 20/23$ |
| **Chun** (1980/1982) | <10 GHz / 通用 | 引入 $C_\tau, C_\beta, C_\sigma, C_x$ |
| **Flock** (1983) | >10 GHz | 简化形式 $\mathrm{XPD} = 5.8 - 13.4\lg A_p$ |
| **ITU-R** | 8~35 GHz | $V = 12.8 f^{0.19}$ 或 $22.6$ |
| **Dissanayake** | 9~30 GHz | 最精细的参数化 |
| **Stuzman-Runyon** (1984) | — | 引入非球形雨滴轴比率 r |
| **Nowland-Sharofsky-Olsen** | 8~35 GHz | 含路径长度 L |
| **Van de Kamp** (1999) | 11~30 GHz | $\mathrm{XPD} = 20\lg f - 16.3\lg A_p - ...$ |
| **ITU-R 2008** | 8~35 GHz | 最新标准 $\mathrm{XPD} = 30\lg f - V\lg A_p + C_\tau + C_\theta + C_\sigma$ |

参见：[[去极化建模三种思路]]