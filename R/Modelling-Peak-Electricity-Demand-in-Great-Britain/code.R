# ---------------------------
# Data Import and Initial Inspection
# ---------------------------
# Load required packages
library(ggplot2)
library(patchwork)
library(tidyverse)
library(lubridate)
library(lme4)
library(knitr)
library(dplyr)
library(kableExtra)
library(car)         # For calculating Variance Inflation Factor (VIF)
library(quantreg)    # Quantile regression
library(caret)       # Cross-validation
library(glmnet)      # Regularized regression
library(broom)       # Tidy up model outputs
theme_set(theme_bw())

# Load data sets
demand_modelling <- read.csv("/Users/jacksu/Desktop/CODE/R/Modelling-Peak-Electricity-Demand-in-Great-Britain/SCS_demand_modelling.csv", stringsAsFactors = FALSE) %>%
  mutate(Date = as.Date(Date))   # Ensure the date format is correct
hourly_temp <- read.csv("/Users/jacksu/Desktop/CODE/R/Modelling-Peak-Electricity-Demand-in-Great-Britain/SCS_hourly_temp.csv", stringsAsFactors = FALSE) 

# Check structure
str(demand_modelling)
summary(demand_modelling)
print(head(demand_modelling))
str(hourly_temp)
summary(hourly_temp)


# ---------------------------
# Data Cleaning
# ---------------------------
# Check date format in the main dataset
class(demand_modelling$Date)
head(demand_modelling$Date)

# Check date format in the temperature dataset
class(hourly_temp$Date)
head(hourly_temp$Date)

# Convert hourly_temp$Date from "DD/MM/YYYY HH:MM" character to Date class
hourly_temp <- hourly_temp %>%
  mutate(
    DateTime = dmy_hm(Date),        # First parse as datetime with day-month-year-hour-minute
    Date = as.Date(DateTime),       # Then extract just the date portion
    Hour = hour(DateTime)
  ) %>%
  select(Date, Hour, temp_hour = temp)


# 1. Check for missing values
colSums(is.na(demand_modelling)) 
colSums(is.na(hourly_temp))   # All 0s indicate no missing values

demand_clean <- demand_modelling %>%
  # Remove rows with completely missing values
  filter(!is.na(demand_gross))


# 2. Check for duplicate records
duplicates <- duplicated(demand_modelling)
if(sum(duplicates) > 0) {
  print(paste("Duplicates found, removing them. Number of duplicates:", sum(duplicates)))
  demand_clean <- demand_clean[!duplicates, ]
} else {
  print("No duplicate records found")
}


# View summary of cleaned data
summary(demand_clean)


# ---------------------------
# Data Inspection
# ---------------------------
# Check variable types
glimpse(demand_modelling)

# Display head of demand_modelling dataset
demand_head <- head(demand_modelling)
kable(demand_head, caption = "Head of Demand Modelling Dataset") %>%
  kable_styling(bootstrap_options = "striped", full_width = FALSE)

# Display head of hourly_temp dataset
hourly_temp_head <- head(hourly_temp)
kable(hourly_temp_head, caption = "Head of Hourly Temperature Dataset") %>%
  kable_styling(bootstrap_options = "striped", full_width = FALSE)


# Histograms (upper-tail distribution)
demand_modelling %>% 
  ggplot(aes(x = demand_gross)) +
  geom_histogram(bins = 30) +
  labs(title = "Distribution of Peak Demand")


# Temperature-demand scatter plot (merging hourly temperature with daily demand)
# Shows temperature impact on demand and weekend effect
merged_temp <- hourly_temp %>%
  filter(Hour == 18) %>%  # Align with daily peak hour
  inner_join(demand_modelling, by = "Date")

ggplot(merged_temp, aes(x = temp, y = demand_gross)) +
  geom_point(aes(color = ifelse(wdayindex %in% c(0,6), "Weekend", "Weekday")), alpha = 0.6) +
  geom_smooth(aes(color = ifelse(wdayindex %in% c(0,6), "Weekend", "Weekday")), 
              method = "lm", se = FALSE) +  
  geom_smooth(method = "lm", se = FALSE, color = "black", linetype = "dashed", size = 1) +  # Global fit
  scale_color_manual(values = c("Weekday" = "#1F77B4", "Weekend" = "#FF7F0E")) +
  labs(
    title = "Temperature vs Peak Demand: Weekday, Weekend & Global Fit",
    x = "Temperature (°C)", y = "Demand (MW)", color = "Day Type"
  )


# Calendar plot of extreme demand days
# Identify peak periods (e.g., cold spells)
extreme_days <- demand_modelling %>% 
  mutate(
    date = as.Date(Date),
    is_extreme = as.integer(demand_gross > quantile(demand_gross, 0.95, na.rm = TRUE)),
    month = month(date)
  )
extreme_days$is_extreme <- as.factor(extreme_days$is_extreme)

ggplot(extreme_days, aes(x = as.factor(month), fill = factor(is_extreme))) +
  geom_bar(position = "dodge") +
  scale_fill_manual(values = c("0" = "grey80", "1" = "#E45756"), name = "Extreme Demand Days") +
  facet_wrap(~year, ncol = 3) +
  labs(title = "The Distribution of Extreme Demand Days", x = "Month", y = "Number of Extreme Demand Days") +
  theme_minimal()

# Filter for years 2001–2010
extreme_days <- demand_modelling %>% 
  mutate(
    date = as.Date(Date),
    year = year(date),
    month = month(date),
    is_extreme = as.integer(demand_gross > quantile(demand_gross, 0.95, na.rm = TRUE))
  ) %>%
  filter(year >= 2001 & year <= 2010) %>% 
  group_by(year, month) %>%
  summarise(
    extreme_count = sum(is_extreme),     # Number of extreme demand days per month
    avg_temp = mean(TE, na.rm = TRUE)    # Average monthly temperature(TE)
  ) %>%
  ungroup()


# Overlay temperature data to indicate extreme weather events
# Bars = number of extreme demand days, line = temperature trend
ggplot(extreme_days, aes(x = factor(month))) +
  geom_bar(aes(y = extreme_count, fill = "Extreme Demand Days"), 
           stat = "identity", position = "dodge") +
  geom_line(aes(y = avg_temp * max(extreme_days$extreme_count) / max(extreme_days$avg_temp), 
                group = year, color = "Temperature"), size = 1) +
  scale_fill_manual(values = c("Extreme Demand Days" = "#E45756")) +
  scale_color_manual(values = c("Temperature" = "blue")) +
  scale_y_continuous(
    name = "Extreme Demand Days",
    sec.axis = sec_axis(~ . * max(extreme_days$avg_temp) / max(extreme_days$extreme_count), 
                        name = "Average Temperature (°C)")
  ) +
  facet_wrap(~year, ncol = 2) +
  labs(title = "Extreme Demand Days & Temperature Trends (2001–2010)", x = "Month") +
  theme_minimal()


# Monthly demand trend plot
# Shows seasonal variation and weekend effect
monthly_demand <- demand_modelling %>%
  mutate(
    # Ensure monthindex is in the range 0–11
    monthindex = pmax(0, pmin(11, monthindex)),
    
    # Create month factor (1–12 mapped to Jan–Dec)
    month = factor(
      monthindex + 1,
      levels = 1:12,
      labels = month.abb
    ),
    month = factor(month,
                   levels = c("Nov", "Dec", "Jan", "Feb", "Mar"),
                   ordered = TRUE),
    
    # Weekday/Weekend classification
    day_type = ifelse(wdayindex %in% c(0, 6), "Weekend", "Weekday")
  ) %>%
  group_by(month, day_type) %>%
  summarise(
    avg_demand = mean(demand_gross, na.rm = TRUE),
    .groups = "drop"
  )

ggplot(monthly_demand, aes(x = month, y = avg_demand, group = day_type, color = day_type)) +
  geom_line(size = 1.2) +
  geom_point(size = 3) +
  scale_color_manual(values = c("Weekday" = "#2CA02C", "Weekend" = "#D62728")) +
  labs(title = "Monthly Demand Trend", 
       x = "Month", y = "Average Demand (MWh)")


# Demand variation over years
# Plot demand over time to detect trends and anomalies
ggplot(demand_modelling, aes(x = Date, y = demand_gross)) +
  geom_smooth(method = "loess", color = "blue", size = 1) +
  geom_vline(xintercept = as.Date("2006-01-01"), linetype = "dashed", color = "red") +
  labs(title = "Peak Demand Over Time", x = "Year", y = "Demand (MW)") +
  scale_x_date(
    labels = scales::date_format("%Y"), 
    breaks = "1 year"
  ) +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) 


# Quantile Regression Analysis of Renewable Energy
library(quantreg)

# Build quantile regression model
rq_model <- rq(
  demand_gross ~ wind + solar_S,
  data = demand_modelling,
  tau = c(0.1, 0.5, 0.9)  # Analyze 10th, 50th, 90th percentiles
)

# Visualize regression coefficients
tidy(rq_model) %>%
  filter(term != "(Intercept)") %>%
  ggplot(aes(x = factor(tau), y = estimate, color = term)) +
  geom_point(size = 3) +
  geom_errorbar(aes(ymin = conf.low, ymax = conf.high), width = 0.2) +
  scale_color_manual(
    values = c("wind" = "#1f77b4", "solar_S" = "#ff7f0e"),
    labels = c("Wind", "Solar PV")
  ) +
  labs(
    title = "Quantile Regression Coefficient Analysis",
    x = "Demand Quantile",
    y = "Coefficient Estimate (MW/Capacity Factor)",
    color = "Energy Type"
  ) +
  geom_hline(yintercept = 0, linetype = "dashed") +
  theme_minimal()


# ---------------------------
# Feature Engineering
# ---------------------------
# Convert categorical variables into factors (dummy variables),
# fix factor order and labels, and add new response variables.
demand_features <- demand_clean %>%
  mutate(
    # Month (only winter months)
    monthindex = factor(monthindex, 
                        levels = c(0, 1, 2, 10, 11),
                        labels = c("Jan", "Feb", "Mar", "Nov", "Dec")),
    # Day of the week
    wdayindex = factor(wdayindex, 
                       levels = c(0, 1, 2, 3, 4, 5, 6),
                       labels = c("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")),
    
    # Weekend indicator (based on corrected wdayindex)
    is_weekend = ifelse(wdayindex %in% c("Mon", "Tue", "Wed", "Thu", "Fri"), 0, 1),
    is_weekend = as.factor(is_weekend),
    
    # Year effects
    trend_pre = ifelse(year <= 2006, year - 2006, 0),
    trend_post = ifelse(year > 2006, year - 2006, 0)
  )

# Check month levels
levels(demand_features$monthindex)
# Check weekday levels
levels(demand_features$wdayindex)


# Scatter plot and regression line of demand vs. temperature
ggplot(demand_features, aes(x = temp, y = demand_gross)) +
  geom_point(alpha = 0.5) +
  geom_smooth(method = "lm", se = FALSE) +
  labs(title = "Temperature vs Net Demand Relationship",
       x = "Temperature (°C)", y = "Net Demand (MW)")


# Polynomial temperature terms
demand_modelling <- demand_modelling %>% 
  mutate(temp_sq = temp^2)

# Fit a model with a nonlinear (quadratic) term
model_nonlinear <- lm(demand_gross ~ temp + temp_sq + wind + solar_S, data = demand_modelling)
summary(model_nonlinear)
# Since p-value for temp_sq = 0.00694 < 0.05 ---> indicates nonlinearity exists, so we include temp^2

# Plot nonlinear effect curve
demand_modelling %>% 
  ggplot(aes(x = temp, y = demand_gross)) +
  geom_point(alpha = 0.1) +
  geom_smooth(
    method = "lm", 
    formula = y ~ x + I(x^2),  # explicitly include quadratic term
    color = "red",
    se = TRUE
  ) +
  labs(
    title = "Non-linear Effect of Temperature on Demand",
    subtitle = "Quadratic term (temp²) is statistically significant (p = 0.0069)",
    x = "Temperature (°C)",
    y = "Peak Demand (MW)"
  )


# Daily min/max temperature (using hourly_temp.csv)
temp_daily <- hourly_temp %>%
  group_by(Date) %>%
  summarise(
    temp_avg = mean(temp_hour),     # Daily average temperature
    temp_min = min(temp_hour),      # Daily minimum temperature
    temp_max = max(temp_hour),      # Daily maximum temperature
  )

# Merge with main dataset
demand_features <- demand_features %>%
  left_join(temp_daily, by = "Date")

# Check feature correlation
cor(demand_features %>% select(demand_gross, temp, temp_min, temp_max), use = "complete.obs")
# --> Not recommended to combine (due to high correlation)


# ---------------------------
# Building the model 
# ---------------------------
 
# Random allocating training set and testing set
set.seed(123) 
idx_est <- sample(demand_features$X,
                  size = round(nrow(demand_features) * 0.8),
                  replace = FALSE)
# Create training set
train_data <- demand_features %>% filter(X %in% idx_est)
# Create testing set
test_data <- demand_features %>% filter(!(X %in% idx_est))

# Testify allocating ratio
cat("Training set sample num:", nrow(train_data), "\nTesting set sample num:", nrow(test_data))


#---Choosing temperature variable(temp,TO,TE,average temperature)-----------
# TE and demand_gross scatter plot + non-linear fitting
te_plot <- demand_features %>%
  ggplot(aes(x = TE, y = demand_gross)) +
  geom_point(alpha = 0.3, color = "#1f77b4") +
  geom_smooth(
    method = "lm", 
    formula = y ~ poly(x, 2),  # Polynoimal Fitting
    color = "#ff7f0e", 
    se = TRUE
  ) +
  labs(
    title = "TE vs Peak Demand",
    subtitle = "Quadratic regression shows non-linear relationship",
    x = "TE (°C)",
    y = "Peak Demand at 6pm (MW)"
  ) +
  theme_minimal()

# Compare temp and TE
temp_plot <- demand_features %>%
  ggplot(aes(x = temp, y = demand_gross)) +
  geom_point(alpha = 0.3, color = "#1f77b4") +
  geom_smooth(
    method = "lm", 
    formula = y ~ poly(x, 2),
    color = "#2ca02c", 
    se = TRUE
  ) +
  labs(
    title = "Temperature vs Peak Demand",
    x = "population-weighted average temperature (°C)",
    y = "Peak Demand at 6pm (MW)"
  )

# Display align horizontally
library(patchwork)
te_plot + temp_plot + plot_layout(ncol = 2)

# MODEL 1: Using TE only
m_te <- lm(demand_gross ~ poly(TE, 2), data = demand_features)

# MODEL 2: Using temp only
m_temp <- lm(demand_gross ~ poly(temp, 2), data = demand_features)

# MODEL3: Using TO Only
m_to <- lm(demand_gross ~ poly(TO, 2) , data = demand_features)

# MODEL4: Using temp_avg only
m_avg <- lm(demand_gross ~ poly(temp_avg, 2), data = demand_features)

# MODEL 5: TE and temp
m_both <- lm(demand_gross ~ poly(TE, 2) + poly(temp, 2), data = demand_features)

# Compute every model MSE and DS
model_comparison_temp <- list(
  "TE" = m_te,
  "Temp" = m_temp,
  "TO" = m_to,
  "average temperature" = m_avg,
  "TE+Temp" = m_both
) %>%
  purrr::map_dfr(function(model) {
    # Extracting predicting value, residuals, sigma
    fitted <- predict(model)
    residuals <- residuals(model)
    sigma <- sigma(model)
    n <- nobs(model)
    
    # Compute MSE and DS
    MSE <- mean(residuals^2)
    DS <- sum((residuals / sigma)^2) + 2 * n * log(sigma)
    
    # Return result
    glance(model) %>%
      select(adj.r.squared) %>%
      mutate(MSE = MSE, DS = DS)
  }, .id = "Model")

# Display Result
knitr::kable(model_comparison_temp, digits = 3)


#-----------Adding year as a variable-------------------
## odel 1: Set year as constant variable
m_year <- lm(demand_gross ~ wind + solar_S + temp + wdayindex + monthindex + 
               year, data = demand_features)

## Model 2: add Weight for years
# Compute base year (1991) average demand
base_year <- 1991
base_demand <- mean(demand_features$demand_gross[demand_features$year == base_year])

# Compute each year gamma_t
year_effect <- demand_features %>%
  group_by(year) %>%
  summarise(mean_demand = mean(demand_gross)) %>%
  mutate(gamma_t = mean_demand / base_demand)

# Combine and return original data
demand_adjusted <- demand_features %>%
  left_join(year_effect, by = "year") %>%
  mutate(demand_scaled = demand_gross / gamma_t)

m_weight <- lm(
  demand_scaled ~ wind + solar_S + temp + wdayindex + monthindex,
  data = demand_adjusted
)


## Model 3: Using multiple section trends
m_trend <- lm(
  demand_gross ~ wind + solar_S + temp + wdayindex + monthindex + trend_pre + trend_post,
  data = demand_features
)


# Compute each model MSE and DS
model_comparison_year <- list(
  "Year as constant variable" = m_year,
  "Year weight" = m_weight,
  "Section trend" = m_trend
) %>%
  purrr::map_dfr(function(model) {
    fitted <- predict(model)
    residuals <- residuals(model)
    sigma <- sigma(model)  
    n <- nobs(model)    
    
    # Compute MSE and DS
    MSE <- mean(residuals^2)
    DS <- sum((residuals / sigma)^2) + 2 * n * log(sigma)
    
    # Return result
    glance(model) %>%
      select(adj.r.squared) %>%
      mutate(MSE = MSE, DS = DS)
  }, .id = "Model")

# Display result
knitr::kable(model_comparison_year, digits = 3)

# Construct based model M0
model_M0 <- lm(demand_gross ~ 1 + wind + solar_S + temp + wdayindex + monthindex, data = demand_features)
summary(model_M0)

# Model M1: Construct year, temperature, is_weekend
M1_formula <- demand_gross ~ 1 +
  wind + solar_S +            # Reusable resources
  wdayindex +                 # week day type effect
  monthindex +                # monthly type effect
  temp + I(temp^2) + TE + I(TE^2) +    # temperature effect
  I(year > 2006)+             # based demand after 2006
  trend_pre + trend_post +    # cross validation trend
  is_weekend                  # weekly effect

model_M1 <- lm(M1_formula, data = demand_features)   
summary(model_M1)

#----> Remove 'temp' because its corresponding p-value is >0.05, and remove 'is_week_end' because it has strong collinearity with 'wdayindex'. The model output result is NA
M1_optimized <- update(model_M1, . ~ . - temp - is_weekend, data = demand_features)   
summary(M1_optimized)

# Likelihood Ratio Test
aic_bic_table <- data.frame(
  Model = c("model_M1", "M1_optimized"),
  AIC = c(AIC(model_M1), AIC(M1_optimized)),
  BIC = c(BIC(model_M1), BIC(M1_optimized))
)

kable(aic_bic_table, 
      caption = "Model Comparison (AIC/BIC)",
      digits = 1,
      col.names = c("Model", "AIC", "BIC"),
      align = c("l", "c", "c")) %>%
  kable_styling(bootstrap_options = "striped",
                full_width = FALSE,
                position = "center")


# Add interaction terms
M2_formula <- demand_gross ~ 1 +
  wind + solar_S +            # Renewable energy
  wdayindex +                 # Main effect of day of the week
  monthindex +                # Main effect of month
  I(temp^2) + TE + I(TE^2) +  # Temperature effect
  I(year > 2006) +            # Change in baseline demand after 2006 (intercept)
  trend_pre + trend_post +    # Orthogonalized segmented trends
  TE:trend_post +             # Interaction between temperature and time trend (post)
  TE:trend_pre +
  TE:monthindex +             # Interaction between temperature and time period
  TE:wind +                   # Interaction between renewable energy and temperature
  TE:solar_S +
  trend_pre:is_weekend +      # Interaction between time trend and periodic effect
  trend_post:is_weekend +
  trend_post:monthindex


model_M2 <- lm(M2_formula, data = demand_features)   
summary(model_M2)

#-----> Remove independent variables with p-value > 0.05
M2_optimized <- update(model_M2, . ~ . - TE:monthindex - TE:wind - trend_post:monthindex, data = demand_features)   
summary(M2_optimized)


# Compare models
# Define a generic function to calculate model performance metrics
calculate_model_metrics <- function(model, data, demand_var = "demand_gross") {
  # Compute basic residuals
  residuals <- residuals(model)
  
  # Compute standard performance metrics
  metrics <- list(
    R2 = summary(model)$r.squared %>% round(3),
    Adj_R2 = summary(model)$adj.r.squared %>% round(3),
    RMSE = sqrt(mean(residuals^2)) %>% round(1),
    MAE = mean(abs(residuals)) %>% round(1)
  )
  
  # Compute metrics for extreme days (95th percentile)
  extreme_threshold <- quantile(data[[demand_var]], 0.95, na.rm = TRUE)
  extreme_days <- data[[demand_var]] >= extreme_threshold
  metrics$Extreme_MAE <- mean(abs(residuals[extreme_days])) %>% round(1)
  
  # Compute VIF (excluding intercept)
  vif_values <- tryCatch({
    car::vif(model) %>% 
      as.data.frame() %>% 
      rownames_to_column("term") %>% 
      filter(term != "(Intercept)") %>% 
      pull(GVIF)
  }, error = function(e) NA)
  
  metrics$Max_VIF <- ifelse(all(is.na(vif_values)), NA, max(vif_values, na.rm = TRUE)) %>% round(1)
  
  return(metrics)
}

# Calculate metrics for each model
metrics_M0 <- calculate_model_metrics(model_M0, demand_features)
metrics_M1 <- calculate_model_metrics(M1_optimized, demand_features)
metrics_M2 <- calculate_model_metrics(M2_optimized, demand_features)

# 1. Build comparison table
performance_table <- bind_rows(
  metrics_M0 %>% as_tibble() %>% add_column(Model = "M0 (Baseline)", .before = 1),
  metrics_M1 %>% as_tibble() %>% add_column(Model = "M1 (Optimized)", .before = 1),
  metrics_M2 %>% as_tibble() %>% add_column(Model = "M2 (Final)", .before = 1)  
) %>% 
  select(Model, R2, Adj_R2, RMSE, MAE, Extreme_MAE, Max_VIF)

# Generate styled performance table
kable(performance_table, 
      align = c("l", rep("c", 6)),
      col.names = c("Model", "R²", "Adjusted R²", "RMSE (MW)", "MAE (MW)", "Extreme Day MAE (MW)", "VIF (max)"),
      caption = "Model Performance Comparison Table") %>%
  kable_styling(
    bootstrap_options = c("striped", "hover", "condensed"),
    full_width = FALSE,
    position = "center"
  ) %>%
  add_header_above(c(" " = 1, "Goodness of Fit" = 2, "Prediction Error" = 3, "Diagnostics" = 1)) %>%
  footnote(
    general = "Note: All error metrics are in megawatts (MW); extreme days are defined as the top 5% of demand values.",
    general_title = ""
  )

# Extreme Day Residual Distribution Plot  
# Calculate residuals
residuals <- residuals(model_M1)

# RMSE
RMSE <- sqrt(mean(residuals^2))

# MAE
MAE <- mean(abs(residuals))

# Extreme Day Forecasting Error (MAE of 95th Percentile Day)
high_demand_threshold <- quantile(demand_adjusted$demand_gross, 0.95)
extreme_days <- demand_adjusted$demand_gross >= high_demand_threshold
MAE_extreme <- mean(abs(residuals[extreme_days]))

# Plot a histogram and save the results
hist_result <- hist(residuals[extreme_days], 
                    breaks = 30, 
                    main = "Residual distribution on extreme days", 
                    xlab = "Residual values")
# Extract bin boundaries and calculate bin width
hist_breaks <- hist_result$breaks
bin_width <- diff(hist_breaks)[1]
# Add a normal distribution curve (adjust the amplitude to match the frequency).
curve(dnorm(x, 
            mean = mean(residuals[extreme_days]), 
            sd = sd(residuals[extreme_days])) * 
        length(residuals[extreme_days]) * bin_width,
      col = "red", 
      lwd = 2, 
      add = TRUE)


# 2. Residual Diagnostics
par(mfrow = c(2,2))
plot(model_M1)

# Upper-tail residuals
## Select data where `demand_gross` is greater than the 95th percentile.
demand_high <- demand_features %>%
  filter(demand_gross > quantile(demand_gross, 0.95)) %>%
  droplevels()

demand_high <- demand_high %>%
  mutate(is_weekend = as.numeric(is_weekend))

# Refit the M1 formula on the filtered data.
model_M1_95 <- lm(M1_formula, data = demand_high)

# Extract residuals.
residuals_M1_95 <- residuals(model_M1_95)

# Draw a Q-Q plot.
ggplot(data.frame(sample = residuals_M1_95), aes(sample = sample)) +
  stat_qq(distribution = qnorm) +
  stat_qq_line(distribution = qnorm) +
  labs(title = "Upper-Tail Q-Q Plot (95% Data)", x = "Theoretical Quantiles", y = "Sample Quantiles") +
  theme_minimal()


# 3. Variable importance (standardized coefficients).
std_coef <- data.frame(
  variable = names(coef(model_M1)),
  effect = coef(model_M1) * apply(model.matrix(model_M1), 2, sd)
) %>% arrange(desc(abs(effect)))

# Create formatted table
std_coef %>%
  rename(`Standardized Effect` = effect) %>%
  kable(
    caption = "Standardized Coefficients (Variable Importance)",
    align = c("l", "r"),
    digits = 3,
    row.names = FALSE  # Key adjustment: Disable row name output.
  ) %>%
  kable_styling(
    bootstrap_options = c("striped", "hover"),
    full_width = FALSE,
    position = "center"
  ) %>%
  column_spec(2, background = "#f7f7f7") %>%
  footnote(
    general = "Effects calculated as coefficients multiplied by predictor SD",
    general_title = "Note:"
  )


# 4. Extreme value prediction ability verification (95th percentile day).
extreme_days <- demand_features %>% 
  filter(demand_gross > quantile(demand_gross, 0.95))

extreme_pred <- predict(model_M1, newdata = extreme_days)
extreme_mape <- mean(abs(extreme_days$demand_gross - extreme_pred)/extreme_days$demand_gross)

# Plot the relationship between variables and residuals.
car::residualPlots(model_M1) 

final_formula <- demand_gross ~ 1 +
  wind + solar_S +
  wdayindex +
  monthindex +         
  I(temp^2) + TE + I(TE^2) + 
  I(year > 2006)+     
  trend_pre + trend_post + 
  
  TE:trend_post +
  TE:trend_pre +
  TE:solar_S +
  trend_pre:is_weekend +
  trend_post:is_weekend 


final_model <- lm(final_formula, data = demand_features)
summary(final_model)


# ---------------------------  
# Analyze the changes in the maximum annual demand during the winter of 2013-14 under different historical weather conditions  
# ---------------------------  
## 1. Data Preparation and Weather Scenario Construction  
# Define the baseline winter (2013-14)
base_winter <- demand_features %>%
  filter(
    Date >= as.Date("2013-11-01"),
    Date <= as.Date("2014-03-31")
  ) %>%
  select(-temp, -TE, -wind, -solar_S)  # Remove weather variable

# Determine the date range for the winter of 2013-14 (assuming winter is from November to March of the following year).
base_dates <- seq(as.Date("2013-11-01"), as.Date("2014-03-31"), by = "day")

# Extract the baseline data (excluding weather variables).
base_data <- demand_modelling %>%
  filter(Date %in% base_dates) %>%
  select(-temp, -wind, -solar_S)  # Remove weather variables, which will be replaced with historical weather data later.

# Extract historical weather data.
historical_winters <- list(
  winter_1991 = seq(as.Date("1991-11-01"), as.Date("1992-03-31"), by = "day"),
  winter_1992 = seq(as.Date("1992-11-01"), as.Date("1993-03-31"), by = "day"),
  winter_1993 = seq(as.Date("1993-11-01"), as.Date("1994-03-31"), by = "day"),
  winter_2005 = seq(as.Date("2005-11-01"), as.Date("2006-03-31"), by = "day")
)

# Extract weather variables for each winter (retain alignment with DSN).
weather_data <- lapply(historical_winters, function(dates) {
  demand_features %>%
    filter(Date %in% dates) %>%
    mutate(DSN = DSN) %>%  # Use the original DSN for alignment
    select(DSN, temp, TE, wind, solar_S)
})

# Construct a weather scenario dataset.
scenarios <- lapply(weather_data, function(weather) {
  base_winter %>%
    left_join(weather, by = "DSN") %>%  # Align strictly by DSN.
    filter(!is.na(temp))  # Remove dates without weather data.
})

## 2. Demand Forecasting and Extreme Value Analysis
# Predict demand for each scenario. 
predict_scenario <- function(scenario_data) {
  scenario_data %>%
    mutate(
      pred_demand = predict(final_model, newdata = .),
      # Calculate temperature-related metrics.
      temp_bin = cut(temp, breaks = c(-Inf, 0, 5, 10, Inf)),
      TE_squared = TE^2
    )
}

scenario_results <- lapply(scenarios, predict_scenario)

# Extract the maximum annual demand.
max_demands <- sapply(scenario_results, function(df) {
  max(df$pred_demand, na.rm = TRUE)
})

# Construct a results table. 
results_table <- data.frame(
  Scenario = names(historical_winters),
  MaxDemand_MW = max_demands,
  AvgTemp = sapply(scenario_results, function(df) mean(df$temp, na.rm = TRUE)),
  AvgTE = sapply(scenario_results, function(df) mean(df$TE, na.rm = TRUE)),
  MinTemp = sapply(scenario_results, function(df) min(df$temp, na.rm = TRUE)),
  MinTE = sapply(scenario_results, function(df) min(df$TE, na.rm = TRUE)),
  Wind_Avg = sapply(scenario_results, function(df) mean(df$wind, na.rm = TRUE)),
  Solar_Avg = sapply(scenario_results, function(df) mean(df$solar_S, na.rm = TRUE)),
  Wind_Max = sapply(scenario_results, function(df) max(df$wind, na.rm = TRUE)),
  Solar_Max = sapply(scenario_results, function(df) max(df$solar_S, na.rm = TRUE))
) 


# Assume the actual data for the original 2013-14 winter.
original_2013 <- data.frame(
  Scenario = "Original 2013-14 Winter",
  MaxDemand_MW = max(demand_features$demand_gross[demand_features$Date %in% base_dates]),
  AvgTemp = mean(demand_features$temp[demand_features$Date %in% base_dates]),
  AvgTE = mean(demand_features$TE[demand_features$Date %in% base_dates], na.rm = TRUE),
  MinTemp = min(demand_features$temp[demand_features$Date %in% base_dates]),
  MinTE = min(demand_features$TE[demand_features$Date %in% base_dates], na.rm = TRUE),
  Wind_Avg = mean(demand_features$wind[demand_features$Date %in% base_dates]),
  Solar_Avg = mean(demand_features$solar_S[demand_features$Date %in% base_dates]),
  Wind_Max = max(demand_features$wind[demand_features$Date %in% base_dates]),
  Solar_Max = max(demand_features$solar_S[demand_features$Date %in% base_dates])
)

# Merge the original data into the results table.
final_table <- rbind(original_2013, results_table) %>%
  arrange(MaxDemand_MW)  # Sort by demand in descending order.

## 3. Output visualization.
# Use `kable` to output an aesthetically pleasing table.
final_table %>%
  kable(
    format = "html",
    align = "c",
    digits = 2,
    col.names = c("Scenario", "Max Demand (MW)", "Avg Temp (°C)", "Avg TE", 
                  "Min Temp (°C)", "Min TE", "Wind Avg", "Solar Avg", 
                  "Wind Max", "Solar Max"),
    caption = "Analysis of the Changes in the Maximum Demand during the 2013-14 Winter under Different Historical Weather Conditions析",
    row.names = FALSE  # Key Fix: Disable the display of the row number column.
  ) %>%
  kable_styling(
    bootstrap_options = c("striped", "hover", "condensed"),
    full_width = FALSE,
    font_size = 12
  ) %>%
  add_header_above(
    c(" " = 1,                # The first column (Scenario) is not grouped.
      "Temperature Metrics" = 5,  # Temperature-related columns (Avg Temp, Avg TE, Min Temp, Min TE).
      "Renewables Metrics" = 4   # Renewable energy columns (Wind Avg, Solar Avg, Wind Max, Solar Max).）
    )
  ) %>%
  row_spec(which(final_table$Scenario == "Original 2013-14 Winter"), 
           bold = TRUE, color = "white", background = "#2c3e50")

# Extract the number of all scenarios.
all_scenarios <- bind_rows(scenario_results, .id = "Scenario")

# Plot the relationship between the temperature quadratic term and demand.
ggplot(all_scenarios, aes(x = TE, y = pred_demand)) +
  geom_point(aes(color = TE), alpha = 0.6) +
  geom_smooth(
    method = "lm", 
    formula = y ~ poly(x, 2), 
    color = "red",
    se = FALSE
  ) +
  scale_color_viridis_c(name = "TE (3-6PM Average temperature)") +
  labs(
    title = "The relationship between the temperature quadratic term and predicted demand.",
    x = "Temperature (°C)",
    y = "Predicted demand (MW)"
  ) +
  facet_wrap(~ Scenario, scales = "free")


# ---------------------------  
# Cross-validation: Evaluate by splitting data by month  
# ---------------------------  
# Grouped cross-validation by month  

# Evaluate model performance by month (supports multiple models)  
# Wrap the prediction function
model_predict <- function(model, newdata) {
  pred <- predict(model, newdata = newdata)
  return(data.frame(
    actual = newdata$demand_gross,
    predicted = pred,
    month = newdata$monthindex
  ))
}


# Predictions for all models
pred_m0 <- model_predict(model_M0, demand_features) %>% mutate(model = "M0")
pred_m1 <- model_predict(M1_optimized, demand_features) %>% mutate(model = "M1")
pred_final <- model_predict(final_model, demand_features) %>% mutate(model = "Final")

# Merge all predictions
pred_all <- bind_rows(pred_m0, pred_m1, pred_final)

# Calculate monthly MSE
monthly_mse <- pred_all %>%
  group_by(model, month) %>%
  summarise(
    mse = mean((actual - predicted)^2),
    .groups = "drop"
  )


# Model prediction function
lm_prediction <- function(data, model, newdata) {
  if (model == "M0") {
    fit <- lm(demand_gross ~ wind + solar_S + temp + wdayindex + monthindex, data = data)
  } else if (model == "M1") {
    fit <- model_M1 <- lm(M1_formula, data = data)
  } else if (model == "Final") {
    fit <- lm(final_formula, data = data)
  } else {
    stop("Unknown model type.")
  }
  
  # Predictions and intervals
  pred <- predict(fit, newdata, interval = "prediction")
  result <- data.frame(
    predicted.mean = pred[, "fit"],
    predicted.sd = (pred[, "upr"] - pred[, "lwr"]) / (2 * qt(0.975, df = fit$df.residual)),
    predicted.lwr = pred[, "lwr"],
    predicted.upr = pred[, "upr"]
  )
  
  return(result)
}


# Cross-validation function
kfold_validate <- function(data, model_type, k = 10) {
  folds <- caret::createFolds(factor(data$monthindex), k = k, list = TRUE)
  
  map_dfr(1:k, function(i) {
    test_idx <- folds[[i]]
    train_set <- data[-test_idx, ]
    test_set <- data[test_idx, ]
    
    tryCatch({
      pred <- lm_prediction(train_set, model_type, test_set)
      cbind(test_set, pred, fold = i)
    }, error = function(e) NULL)
  })
}

# Model evaluation function
compute_scores <- function(pred_df) {
  pred_df %>% 
    mutate(
      demand_gross = as.numeric(demand_gross),
      pred_mean = as.numeric(predicted.mean),
      pred_sd = as.numeric(predicted.sd),
      MSE = (demand_gross - pred_mean)^2,
      DS = ifelse(is.na(pred_sd), NA,
                  ((demand_gross - pred_mean)/pred_sd)^2 + 2 * log(pred_sd))
    ) %>% 
    group_by(model, fold) %>% 
    summarise(
      MSE = mean(MSE, na.rm = TRUE),
      DS = mean(DS, na.rm = TRUE),
      .groups = "drop"
    )
}

# Run cross-validation and evaluate  
# Perform cross-validation
cv_results <- map_dfr(c("M0", "M1", "Final"), ~{
  results <- tryCatch(
    kfold_validate(train_data, model_type = .x, k = 10),
    error = function(e) NULL
  )
  if (!is.null(results)) mutate(results, model = .x)
})

# Evaluation calculation
model_scores <- compute_scores(cv_results)

# Summarize evaluations
final_scores <- model_scores %>% 
  group_by(model) %>% 
  summarise(
    MSE_mean = mean(MSE),
    MSE_se = sd(MSE) / sqrt(n()),
    DS_mean = mean(DS),
    DS_se = sd(DS) / sqrt(n()),
    .groups = "drop"
  )

# Output as a table
final_table <- final_scores %>% 
  transmute(
    Model = model,
    MSE = sprintf("%.1f ± %.1f", MSE_mean, MSE_se),
    DS = sprintf("%.1f ± %.1f", DS_mean, DS_se)
  )

final_table %>%
  kbl(
    format = "html", # Choose "html" or "latex" based on the output type
    caption = "Cross-validation Performance Comparison (Mean ± Standard Error)",
    col.names = c("Model", "MSE (Mean ± SE)", "Dawid-Sebastiani Score"),
    align = c("l", "c", "c")  # Column alignment
  ) %>%
  kable_styling(
    bootstrap_options = c("striped", "hover", "condensed"),
    full_width = FALSE,
    font_size = 13,
    position = "center"
  ) %>%
  add_header_above(c(" " = 1, "Performance Metrics" = 2)) %>%  # Add grouped table headers
  column_spec(1, bold = TRUE, width = "6em") %>%  # Bold the model column
  column_spec(2:3, width = "10em") %>%  # Width of the metric columns
  row_spec(which.min(final_scores$MSE_mean),  # Highlight the model with the lowest MSE
           bold = TRUE, 
           color = "white",
           background = "#2c3e50"
  ) %>%
  footnote(
    general = "Explanation of evaluation metrics:",
    number = c(
      "MSE = Mean Squared Error (the smaller the better)",
      "DS = Dawid-Sebastiani score (the smaller the better)"
    ),
    footnote_as_chunk = TRUE
  )

# Plot predictions vs. actual values
plot_pred_vs_actual <- function(df, model_name, color) {
  df %>%
    filter(model == model_name) %>%
    ggplot(aes(x = demand_gross, y = predicted.mean)) +
    geom_point(alpha = 0.5, color = color) +
    geom_abline(slope = 1, intercept = 0, linetype = "dashed") +
    labs(
      title = paste("Predicted vs Actual -", model_name),
      x = "Actual Demand (MW)",
      y = "Predicted Demand (MW)"
    ) +
    theme_minimal()
}


# PLOT GRAPH
p_m0 <- plot_pred_vs_actual(cv_results, "M0", "#1f77b4")
p_m1 <- plot_pred_vs_actual(cv_results, "M1", "#ff7f0e")
p_final <- plot_pred_vs_actual(cv_results, "Final", "#2ca02c")

# DISPLAY GRAPH
p_m0 + p_m1 + p_final + patchwork::plot_layout(ncol = 3)


monthly_mse %>% 
  mutate(month = factor(month, levels = 1:12)) %>% 
  ggplot(aes(x = month, y = mse, color = model, group = model)) +
  geom_line(linewidth = 1) +
  geom_point(size = 3) +
  scale_color_manual(values = c("M0" = "#1f77b4", "M1" = "#ff7f0e", "Final" = "#2ca02c")) +
  labs(title = "Monthly Prediction Accuracy Comparison",
       subtitle = "Mean Squared Error (MSE) by Month",
       x = "Month Index",
       y = "MSE",
       color = "Model") +
  theme_minimal() +
  theme(plot.title = element_text(face = "bold", size = 14),
        legend.position = "bottom")

monthly_mse_table <- monthly_mse %>% 
  pivot_wider(names_from = model, values_from = mse) %>% 
  mutate(
    Month = month.name[month],  # First, create a column for month names
    Month = factor(Month, levels = month.name)  # Convert to an ordered factor
  ) %>% 
  select(Month, M0, M1, Final) %>% 
  arrange(Month)  # Sort by factor order

# Add explicit formatting parameters (HTML or LaTeX)
monthly_mse_table %>%
  kbl(
    format = "html",  # Choose "html" or "latex" based on the output type
    digits = 1,
    caption = "Monthly MSE Comparison Across Models",
    col.names = c("Month", "M0", "M1", "Final")
  ) %>%
  kable_styling(
    bootstrap_options = c("striped", "hover"),
    full_width = FALSE
  )

