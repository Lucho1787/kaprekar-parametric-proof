# Kaprekar's Routine Complexity Optimization

## Overview
This repository contains the verification algorithm for the research paper: **"Optimización de la complejidad en los pasos de Kaprekar: Reducción a 9 clases paramétricas"**.

The script mathematically validates the **Parametric Dominance Hypothesis**, demonstrating that verifying the Kaprekar's constant convergence for 4-digit numbers does not require checking 30 graph trajectories (Nishiyama, 2006), but only **9 parametric classes** based on the alpha difference ($\alpha = a - d$).

## Contents
* `kaprekar_verification.py`: Python 3 script that performs an exhaustive search over the domain $D = [0000, 9999]$, filtering repdigits and classifying convergence steps by $(\alpha, \beta)$ parameters.

## Usage
To replicate the results presented in Table 1 of the paper:

```bash
python kaprekar_verification.py
