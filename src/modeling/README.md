after training the models i found that both models performances are very similar in terms of metric scores and training time.
they have a bit of differences in the confusion matrix.
comparing the logistics regression and linear support vector machine confusion matrix side by side
[[456  96]      [[467  85]

 [ 44 619]]     [ 55 608]]

the support vector machine was better overall since its FP, FN and TN values are smaller than the logistic regression ones.
I'm guessing that svm is performing better even on linear data because logistic regression works in a worse way because it sets a probability
threshhold for all the data points and makes a condition and returns a probability value so the threhhold choice is not always optimal
however with svm it creates a boundary or a plane between the data points and tries to maximize the distance between those data points and that
boundary so its more accurate since you're not setting a certain value to begin with.