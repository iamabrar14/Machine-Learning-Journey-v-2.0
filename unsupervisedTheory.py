""" Unsupervised learning is a type of machine learning where the model is trained on data 
without labeled responses. In unsupervised learning, the algorithm tries to find patterns, 
groupings, or structure within the data on its own, without being told the "correct answer" 
for any data point.

Common unsupervised learning tasks include:

Clustering: Grouping similar data points together (e.g., customer segmentation).
Dimensionality Reduction: Reducing the number of variables/features in the data (e.g., PCA).
Anomaly Detection: Identifying unusual data points.

"""
""" Supervised learning: You teach the model with example questions and answers.
Unsupervised learning: The model finds structure and relationships in data on its own,
without being told the right answers.

"""

""" 
Mean
The mean (often called the average) is a measure of central tendency of a set of numbers.
It’s calculated by summing all the values and dividing by the number of values:

Mean
=
x
1
+
x
2
+
⋯
+
x
n
n

Example:
For numbers 2, 4, 6, the mean is ((2 + 4 + 6)/3 = 4).

In clustering (like k-means), the centroid of a cluster is a point that represents the mean 
position of all the data points in that cluster.
In a dataset with multiple features, the centroid is a point whose coordinates are the means 
of the respective features.

Example:
For points ((2, 3)), ((4, 7)), and ((6, 1)), the centroid is:
(
2
+
4
+
6
3
,
3
+
7
+
1
3
)
=
(
4
,
3.67
)


"""

""" Euclidean distance is the straight-line distance between two points in Euclidean space.
For two points

Role in Unsupervised ML
Clustering (e.g., k-means): Euclidean distance is used to measure the similarity between data 
points and centroids. 
Points closer together (smaller distance) are considered more similar and grouped into the 
same cluster.
Anomaly Detection: Outliers are data points that are far from the majority (large Euclidean
distance from cluster centroids).

"""

""" Variance
Variance measures how far data points are spread out from the mean (average) value.

High variance: Data points are widely spread out from the mean.
Low variance: Data points are close to the mean.

In unsupervised ML:
Variance helps to understand the diversity or heterogeneity of a dataset. 
For example, in clustering, variance within clusters is minimized
to ensure that similar data points are grouped together.



Spread
Spread is a general term for how much the data values vary. It refers to the range or 
dispersion of the data.

Common measures of spread:
Range: Difference between the largest and smallest values.
Interquartile range (IQR): Range of the middle 50% of values.
Standard deviation: The square root of variance, also measures spread.
In unsupervised ML:
Understanding the spread of data helps in:

Deciding the number of clusters.
Identifying outliers or anomalies.
Choosing appropriate distance metrics.
"""