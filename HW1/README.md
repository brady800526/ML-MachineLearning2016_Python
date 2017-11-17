ML #1
=====

#### HW1 uses weather records from FengYuan Station, Taiwan which are divided into train set and test set. 

!["Predict PM2.5 Example"](http://i68.tinypic.com/dewhas.png "Predict PM2.5 Example")

- **train.csv**: Complete data in the first 20 days of each month.

![train.csv](http://i68.tinypic.com/14n37s8.png "train.csv")

- **test_X.csv**: Random sample the data from the rest of the month. Each data contains 10 hours in a row as a single datum. Use the first 9 hours as the features to predict the 10 th hour data. There will be 240 unique data, please predict these 240 data based on there feature.

![test_X.csv](http://i66.tinypic.com/x581l3.png "test_X.csv")

## Submission format

predict the 240 data in the test set and upload to Kaggle

- The format shoud be .csv
- First row should be is, value
- Start from second row, each row is id and predicted value separate by comma.

Example format: 

![Submission format](http://i65.tinypic.com/1688mee.png "Submission format")

## Kaggle

1. https://inclass.kaggle.com/c/ml2016-pm2-5-prediction
2. Upload 5 times each day
3. Test set including 240 data are divided into two set，120 public data, 120 private data
4. Leaderboard will show the score of public set, you can select two set of score of private set result
5. The final score depends on the private set

## HW rules

1. Please implement linear regression by using **Gradient Descent**
2. Please compare the performance of different **learning rate**
3. Please compare the performance of **regularization**
4. You can use other method but also has to use Gradient Descent
5. Cannot use third-party package, but you can use **numpy**, **scipy** or something else to process data like **pandas**

## Submission format

In the Github, ML2016/hw1/ should include Report.pdf, linear_regression.sh, kaggle_best.sh，and all of the required files(train.csv, test_X.csv)

Usage:
```
./linear_regression.sh 輸出:linear_regression.csv 
./kaggle_best.sh 輸出:kaggle_best.csv
```