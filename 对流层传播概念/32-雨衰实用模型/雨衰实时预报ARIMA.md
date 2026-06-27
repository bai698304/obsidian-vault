---
tags:
  - 雨衰
  - 实时预报
  - ARIMA
  - 时间序列
  - GA-ARIMA
  - chapter6
date: 2026-05-27
source: 《对流层中的传播、散射特性及其对无线系统的影响》第6章 6.2.1.7节
---

# 雨衰实时预报ARIMA模型

ARIMA（单整自回归移动平均过程）用于雨衰实时动态预报。

**ARMA 模型**：
$$A_t = \sum_{i=1}^p \varphi_i A_{t-i} - \sum_{i=1}^q \theta_i \varepsilon_{t-i} + \varepsilon_t$$

**ARIMA 模型**（对非平稳序列 k 阶 r 次差分后应用 ARMA）：
$$\Delta_k^r A_t = \sum_{i=1}^p \varphi_i \Delta_k^r A_{t-i} - \sum_{i=1}^q \theta_i \varepsilon_{t-i} + \varepsilon_t$$

**GA-ARIMA**：遗传算法 + ARIMA，基于改进遗传算法自适应调整预报参数。可实现不同地区模型参数数据库**共享共用**。

建模三步：模型识别 → 参数估计 → 诊断检验。

**平稳性判据**：[[自相关函数]]快速衰减至 0 为平稳，否则需差分。

参见：[[雨衰时间序列获取方法]]