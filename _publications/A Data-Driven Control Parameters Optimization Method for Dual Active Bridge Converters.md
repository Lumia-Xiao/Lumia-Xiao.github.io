---
title: "A Data-Driven Control Parameters Optimization Method for Dual Active Bridge Converters"
collection: publications
category: manuscripts
permalink: /publication/A Data-Driven Control Parameters Optimization Method for Dual Active Bridge Converters
excerpt: >-
  Conventional optimization approaches for dual active bridge converters (DAB) involve separate analysis and experimental verification stages, which may lead to suboptimal experiment results due to unaccounted parameters. This article presents a data-driven...
date: 2024-03-19
venue: 'IEEE Transactions on Industrial Electronics'
paperurl: 'https://doi.org/10.1109/TIE.2024.3370950'
citation: 'Z. Xiao, Y. Jiang, F. Deng, Z. Yao, and Y. Tang, "A Data-Driven Control Parameters Optimization Method for Dual Active Bridge Converters," in IEEE Transactions on Industrial Electronics, vol. 71, no. 11, pp. 14054-14066, Nov. 2024, doi: 10.1109/TIE.2024.3370950.'
---

## Abstract

Conventional optimization approaches for dual active bridge converters (DAB) involve separate analysis and experimental verification stages, which may lead to suboptimal experiment results due to unaccounted parameters. This article presents a data-driven control parameters optimization method for DAB. The theoretical analysis and experimental verification of power loss serve as the source and target domains, respectively. By employing a large-scale set of simulation samples, we train an artificial neural network to evaluate power loss under various operating conditions. The insights gleaned from the pretrained source domain model are subsequently transferred to a target domain model (TDM) through transfer learning fine-tuning on a small scale of experiment samples. The TDM is utilized within a mathematical software to explore optimal control parameters, striking a balance between precision and calculation complexity. Experimental results from a 2.4-kW 400-V DAB prototype demonstrate that the proposed peak efficiency searching method progressively enhances the accuracy of the power loss model through the accumulation of experimental data. Outperforming conventional AI-based optimization methods, our approach utilizes a TDM based on real-world experimental data, effectively guiding the search for optimal control parameters, and ensuring the attainment of actual peak efficiency.

<figure class="publication-figure">
  <img src="/images/A Data-Driven Control Parameters Optimization Method for Dual Active Bridge Converters.webp" loading="lazy" decoding="async" alt="A Data-Driven Control Parameters Optimization Method for Dual Active Bridge Converters">
</figure>
