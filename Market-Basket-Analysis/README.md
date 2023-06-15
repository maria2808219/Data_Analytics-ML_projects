# Customer Segmentation using RFM Analysis and K means Algorithm

### RFM Analysis

RFM (Recency, Frequency, Monetary) analysis is a widely utilized technique in marketing and customer relationship management for effective customer segmentation. It enables businesses to understand customer behavior and identify valuable customer segments.

RFM analysis takes into account three primary metrics:

Recency: This metric measures the time since a customer's last purchase. It provides insight into how recently a customer has interacted with the business.

Frequency: The frequency metric indicates how often a customer makes purchases within a specific timeframe. It helps businesses understand customer loyalty and engagement levels.

Monetary: The monetary metric represents the value of a customer's purchases. It quantifies the amount of money a customer has spent, providing insights into their overall value to the business.

By analyzing these three metrics together, businesses can gain a comprehensive understanding of customer segments, enabling them to tailor their marketing strategies and customer experiences more effectively.

### KMeans clustering
K-means clustering is an extensively utilized unsupervised machine learning technique employed for dividing data into separate groups or clusters. Its main objective is to reduce the total sum of squares within each cluster by iteratively assigning data points to clusters based on their similarity to the centroids of the clusters.

### Dataset Description
The Online Retail Data Set contains a wealth of information about customer transactions. It includes details such as the invoice date and invoice no. of the transaction, the items purchased, the quantity, and the customer's ID. The dataset allows us to explore the purchasing patterns of customers and identify the relationships between different products.
All the necessary data cleaning have already been done in this [notebook](https://github.com/maria2808219/Data_Analytics-ML_projects/blob/main/Market-Basket-Analysis/Basket_Analysis_of_the_Online_Retail_Dataset_Apriori.ipynb). However, other transformation(s) that needed to be done for the clustering was done.

### Methodology and Result

1. The data contained transactions bewteen 2010-12-01 and 2011-12-09. For the rfm analysis, the next day of the last transaction day in the dataset was used as the cutoff(we worked with 10th of December, 2011 as the cutoff date for the analysis). Recency, Frequency and Monetary values for each customer was obtained in the following ways:

    Recency- The difference in days from cutoff date and the last transaction date of a customer

    Frequency- The count of all the unique invoice(s) for transactions for a customer

    Monetary value- The sum of the total amount spent by customer until cutoff date 

2. After RFM values for each customer was obtained, Customer segmentation into segments was done using the Kmeans clustering algorithm.
3. Elbow curve and silhoutte score was used to choose optimum value of k. The optimum value for k is 2.

![choosing-right-k](https://github.com/maria2808219/Data_Analytics-ML_projects/blob/main/Market-Basket-Analysis/Images/1.png)

Even though the optimum cluster numbers is 2, because the online retail market is diverse, with customers exhibiting a wide range of preferences, buying behaviors, and demographics, By using 3 clusters, we can capture more distinct customer segments, gain deeper insights into their specific needs and preferences and also develop more personalized marketing strategies for each segment. The segmentation details based on 3 clusters is shown in the table below:

![3-clusters-details](https://github.com/maria2808219/Data_Analytics-ML_projects/blob/main/Market-Basket-Analysis/Images/2.png).

From the segmentation result shown above, we can deduce and recommend the following:

Cluster 0: These customers have a relatively recent purchase history but lower frequency and monetary value, They are responsible for nearly 24% of total revenue. To increase their engagement and loyalty, consider implementing targeted promotions, personalized offers, or loyalty programs to encourage more frequent and higher-value purchases.

Cluster 1: These customers are the most valuable, since they have a high frequency of purchases and significant monetary value. They are active and valuable customers. Focus on providing personalized recommendations, exclusive deals, and premium services to enhance their experience and maintain their loyalty.

Cluster 2: These customers have a longer recency period(mean recency is more than 5 months), lower frequency, and lower monetary value, and are most likely on the verge of churning.They account for about 5% of total revenue. It is important to adopt special strategies to prevent losing them. They may require additional incentives or reminders to make purchases. Consider implementing win-back campaigns, re-engagement strategies, or special discounts to reactivate their interest and encourage more frequent purchases.


A snake plot for the segmentation is shown below:

![snake-plot](https://github.com/maria2808219/Data_Analytics-ML_projects/blob/main/Market-Basket-Analysis/Images/3.png)

