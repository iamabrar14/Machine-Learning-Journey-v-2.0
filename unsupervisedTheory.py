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