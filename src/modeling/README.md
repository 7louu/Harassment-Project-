after training the models i found that both models performances are very similar in terms of metric scores and training time.
they have a bit of differences in the confusion matrix.
comparing the logistics regression and linear support vector machine confusion matrix side by side
[[456  96]      [[467  85]

 [ 44 619]]     [ 55 608]]

the support vector machine was better overall since its FP, FN and TN values are smaller than the logistic regression ones.
