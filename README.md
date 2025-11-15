# Project Title:
*NASS Crop Yield Predictor and Analysis for Texas farms*

## Teammates
- Stephen Cox, ssj63
- Shazz Momin, wzu2

## Project Abstract
The goal of this project is to use past agricultural census to build a model that can predict crop yield for Texas farms and explore the meaning of what our model predicts

## Problem Statement
- Farmers in Texas are a very important part of our community. It is important to know what factors can effect the success of our farmers and their product since many people relay on Texas grown crops.

- What factors most deeply effect our farms success and can we predict if our farms will be succesful for the year.

- Benchmarks we will use are Mean Absolute Error, Root Mean Squared Error and R^2. Each of these scores we help us interpret different parts of the models accuracy/precision/recall since this is a regressive model

- The Data comes from US Department of Agriculture - National Agricultural Statistics Service census data which includes many different info points like: yield, land size and fertilizer... 

- Practical Interpretability, we hope to use this model to try and interpret correlations between farming factors and crop yield

- What we hope to achieve
    - Build a working NN regressor that predicts county-level crop yield for Texas using 2012/2017/2022 data.
    - Beat simple baselines (mean and linear reg.) by at least a measurable margin (lower MAE/RMSE).
    - Produce interpretable model explainers (SHAP or partial dependence) showing the most influential
