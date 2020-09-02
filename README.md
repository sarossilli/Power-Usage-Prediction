# Daily Power Usage Forcaster
> A Time-Series Forcasting Project To Help Me Budget My Monthly Power Bill 

I decided to start this project to help me accurately budget my montly bills. My montly electric bill swings wildly each month, depending on the season and other factors such as the acedemic calendar. I wanted to build a forcast system to automatically tell me how much I should expect to spend each month on power.
<br>
<br>

## Development Process:
#### EDA:

You can see the high variance in my montly power usage with this weekly-usage chart:
![](img/readme_img/personal_power_usage.png)

In fact, the daily usage data has a variance of 116.44 kWh. In order to make this data have less variance, I used a 7 day moving average for my data.

To remove further variance and randomness, I decomposed the data into seasonality, trend, and noise/residule.

Here is the weekly seanonality:
![](img/readme_img/weekly_season.png)

And the general seasonality:
![](img/readme_img/season.png)

Due to a lack of data (Only being a resident for a year), I tested my modeling on a larger dataset, The AEP hourly power demand. I used this data to test a model. As more data becomes avaliable for my personal data, I will use the same process to build a personal model and have it updated montly with new data.

Here is the weekly demand plot:
![](img/readme_img/aep.png)

And the decomposition:
![](img/readme_img/AEP_decomp.png)

And the general seasonality:
![](img/readme_img/AEP_seasonality.png)

After removing seasonality and data from the data, the trend is the only value left to model:
![](img/readme_img/trend.png)

#### Data/Feature Engineering:


## Meta

Sam Rossilli – Sarossilli@gmail.com – Srossill@uccs.edu

[https://github.com/sarossilli/](https://github.com/sarossilli/)

## Using Your Own Data:

1. Fork it (<https://github.com/sarossilli/Power-Usage-Prediction/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

