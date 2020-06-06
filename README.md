# AOS1_TP
PCA / Regularization / Kernel / Time Series / Bayesian regularization

### PCA 
Band reduction in multispectral images. More generally a multispectral image of size N × M with P spectral bands can be stored as a N × M ×P array. 
There are N × M pixels living in R<sup>p</sup>.  
When the number of spectral bands P is too large, it is desirable to somehow reduce that number ultimately to 3 for viewing purposes. This process is called band reduction.  
Propose a method using the PCA performing a band reduction to 3 bands and use it on the provided multispectral image.  

multispectral images are from:  
- [http://lesun.weebly.com/hyperspectral-data-set.html](http://lesun.weebly.com/hyperspectral-data-set.html)  

### Regularization
Make elastic net outshine the lasso. The elastic net regression was invented to compensate for the lack of robustness of the lasso regression. 
The elastic net especially outshines the lasso when some variables are highly correlated and on the same scale.  
Design a regression dataset in which we want to select variables and where the elastic net gives better results in terms of stability of the set of selected variables.  

### Kernel
Implement the paper. The paper by Burges and Schölkopf[1] is investigating a method the improve the accuracy and speed of SVM.
First train a SVM with the same dataset (MNIST) with the kernel and the hyperparameter C they are suggesting.  

References:  
- [1][Chris J.C. Burges and Bernhard Schölkopf. “Improving the Accuracy and Speed of Support Vector Machines”.](https://papers.nips.cc/paper/1253-improving-the-accuracy-and-speed-of-support-vector-machines.pdf)

### Time series
The dataset in the file data/debitcards.csv stores the monthly retail debit card usage in Iceland (million ISK) from january 2000 to august 2013. 
Give an estimate of the cumulated debit card usage during the rest of the year (4 months).  
Particular care should be taken with the frequency of time series, its nature, the choice of the model and its validation.  

### Bayesian regularization
The Gaussian-inverse-Wishart prior can be interpreted as information provided by “virtual data” ; they should make it possible to make model estimation more robust without involving any information 
regarding the actual distribution of the data (remember that while with simulated data the actual distribution is known, this will not be the case for real datasets).  

We imagine a way to provide meaningful estimates using only the observed training data at the disposal. We test various values for the shrinkage parameter and degrees of freedom and analyze the influence on the results.



