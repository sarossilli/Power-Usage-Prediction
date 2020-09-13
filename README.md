[<img src="https://raw.githubusercontent.com/Sarossilli/Power-Usage-Prediction/master/img/readme_img/header.gif" alt="HEADER">]() 
### A Project to Forcast My Montly Power Usage And Bill

I decided to start this project to help me accurately budget my montly bills. My montly electric bill swings wildly each month, depending on the season and other factors such as the acedemic calendar. I wanted to build a forcast system to automatically tell me how much I should expect to spend each month on power.
## Project Overview:
- Created a tool thate forcasts my weekly and montly power usage in my apartment in order to help me budget and reduce my power bills.
- Utilized time series datasets including my personal daily power usage data from as well as AEP's hourly power demand dataset to test forcasting methods.
- Engineered data to fit requirements for the model
- Implemented an Auto Regressive Integrated Moving Average model for forcasting.

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, statsmodels, matplotlib, pickle  
**For Requirements:**  ```pip install -r requirements.txt```  

# Development Process:
### Data Collection:
I first downloaded my personal daily power consumption for the 2019-2020 year. You can see the raw usage data from my appartment here:

![](img/readme_img/personal_power_usage.png)

Due to a lack of data (Only being a resident in my appartment for a year), I tested my model and data manipulation on a larger dataset. I chose to test on The AEP hourly power demand which is
[avaliable through kaggle.](https://www.kaggle.com/robikscube/hourly-energy-consumption) 
I used this data to test a model. As more data becomes avaliable for my personal data, I will use the same process to build a personal model and have it updated montly with new data.

Here is the weekly AEP demand plot:

![](img/readme_img/aep.png)

And the general seasonality:

![](img/readme_img/season.png)

And the decomposition:

![](img/readme_img/AEP_decomp.png)

And the general seasonality:

![](img/readme_img/AEP_seasonality.png)

After removing seasonality and data from the data, the trend is the only value left to model:

![](img/readme_img/trend.png)

### Initial Model: ARIMA

The First initial attempt at modeling usage used an ARIMA model. This model requires a staionary trend dataset, so I spent time making the time series trend stationary.
To do this, I transformed my data into a difference in log scale weighted mean. The weighted mean in log scale was subtraced from the same shifted data to get a 'difference between times' dataset. After transformation the data looked like the following:
<br>
> ![](img/figures/mean_log.png)

After stationarizing the data, I used statmodels module to create an ARIMA model. 


The initial results are as follows.
The predicted power usage is in red, and the actual power usage is blue:
> ![](img/figures/ARIMA_Pred.png)

And the general trend forcast for the next 4 years are shown in blue here:

![](img/figures/forcast_ARIMA.png)

The benfits of this model is it was fast and simple to create. This model is somewhat limited though, since other variables like weather is dificult to incoperate in the model. In order to improve uppon this model, I explored several more modeling techniques

#### Second Model: Seq2Seq Network
Readme is a work in progress

### Meta

Sam Rossilli – Sarossilli@gmail.com – Srossill@uccs.edu

[https://github.com/sarossilli/](https://github.com/sarossilli/)


