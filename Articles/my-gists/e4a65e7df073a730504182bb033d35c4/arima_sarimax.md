# ARIMA (AutoRegressive Integrated Moving Average)

ARIMA is a statistical model used for time series data forecasting. It consists of three main components:

1. **AutoRegressive (AR) Component**: This part models the autocorrelation in the time series data. It can be represented by the equation:

$$\[X_t = c + \phi_1 X_{t-1} + \phi_2 X_{t-2} + \ldots + \phi_p X_{t-p} + \varepsilon_t\]$$

   Where:
   - $\(X_t\)$ is the value at time $\(t\)$.
   - $\(c\)$ is a constant.
   - $\(\phi_1, \phi_2, \ldots, \phi_p\)$ are the autoregressive coefficients.
   - $\(\varepsilon_t\)$ is white noise.

2. **Integrated (I) Component**: ARIMA aims to work with stationary data. If the original data is non-stationary, differencing is applied. This can be represented by the equation:

$$\[Y_t = (1 - L)^d X_t\]$$

   Where:
   - $\(Y_t\)$ is the differenced series.
   - $\(L\)$ is the lag operator.
   - $\(d\)$ is the order of differencing.

3. **Moving Average (MA) Component**: This part models the moving average of past error terms and can be represented by the equation:

$$\[X_t = \mu + \varepsilon_t - \theta_1 \varepsilon_{t-1} - \theta_2 \varepsilon_{t-2} - \ldots - \theta_q \varepsilon_{t-q}\]$$

   Where:
   - $\(\mu\)$ is the mean of the series.
   - $\(\theta_1, \theta_2, \ldots, \theta_q\)$ are the moving average coefficients.
   - $\(\varepsilon_t\)$ is the white noise error term.

ARIMA combines these components to model time series data and make predictions.

# SARIMAX (Seasonal AutoRegressive Integrated Moving Average with eXogenous regressors)

SARIMAX is an extension of ARIMA that includes seasonal components and external explanatory variables (exogenous regressors). Here's a more detailed explanation:

1. **Seasonal (S) Component**: SARIMAX takes into account seasonal patterns by introducing seasonal differences. This can be represented by the equation:

   $$\[Y_t = (1 - L)^d (1 - L^s) X_t\]$$

   Where:
   - $\(s\)$ is the seasonal period.
   - $\(L\)$ is the lag operator.
   - $\(d\)$ is the order of non-seasonal differencing.

2. **eXogenous Regressors (X) Component**: SARIMAX allows the inclusion of external variables that may influence the time series. This is particularly useful when there are other factors affecting the data. The model can be represented as:

   $$\[Y_t = (1 - L)^d (1 - L^s) X_t + \beta_1 Z_{1t} + \beta_2 Z_{2t} + \ldots + \beta_k Z_{kt} + \varepsilon_t\]$$

   Where:
   - $\(Z_{1t}, Z_{2t}, \ldots, Z_{kt}\)$ are the exogenous variables.
   - $\(\beta_1, \beta_2, \ldots, \beta_k\)$ are the corresponding coefficients.

SARIMAX is a versatile model for forecasting time series data with both seasonal patterns and external influences.
