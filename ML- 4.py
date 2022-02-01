#!/usr/bin/env python
# coding: utf-8

# # Machine Learning Assignment 4

# ## 1. What are the key tasks involved in getting ready to work with machine learning modeling?

# In[ ]:


# 1) Data Collection
# 2) Data preparation and cleaning
# 3) Model building
# 4) Model Training and evaluation
# 5) parameter estimation and testing


# ## 2. What are the different forms of data used in machine learning? Give a specific example for each of them.

# In[ ]:


# The problem is, machine learning algorithms at their core operate on numeric data. They take numbers as input and
# predict a number as output. All data is seen as vectors and matrices, using the terminology from linear algebra


# ## 3. Distinguish:
# ## 1. Numeric vs. categorical attributes
# ## 2. Feature selection vs. dimensionality reduction

# In[ ]:


# 1) Categorical data is a type of data that is used to group information with similar characteristics while 
# Numerical data is a type of data that expresses information in the form of numbers

# 2) Feature selection is simply selecting and excluding given features without changing them.
# Dimensionality reduction transforms features into lower dimensions


# ## 4. Make quick notes on any two of the following:
# ## 1. The histogram
# ## 2. Use a scatter plot
# ## 3.PCA (Personal Computer Aid)

# In[ ]:


# A histogram is a graphical representation that organizes a group of data points into user-specified ranges. 
# Similar in appearance to a bar graph, the histogram condenses a data series into an easily interpreted visual 
# by taking many data points and grouping them into logical ranges or bins.

#A scatter plot (aka scatter chart, scatter graph) uses dots to represent values for two different numeric variables
#The position of each dot on the horizontal and vertical axis indicates values for an individual data point. 
# Scatter plots are used to observe relationships between variables.


# ## 5. Why is it necessary to investigate data? Is there a discrepancy in how qualitative and quantitative data are explored?

# In[ ]:


# Quantitative research deals with numbers and statistics, while qualitative research deals with words and meanings.
# Quantitative methods allow you to systematically measure variables and test hypotheses.
# Qualitative methods allow you to explore concepts and experiences in more detail.


# ##  6. What are the various histogram shapes? What exactly are ‘bins&#39;?

# In[ ]:


# Bins are the numerical ranges into which you'll group the data. In presentation histograms your bins should all
# be the same size and should encompass all of the data. In addition the boundaries should generally occur at nice
# round numbers. To choose the bin sizes, first find the smallest and largest data point.


# ## 7. How do we deal with data outliers?

# In[ ]:


# drop them out, try to transform or cap the values


# ## 8. What are the various central inclination measures? Why does mean vary too much from median in certain data sets?

# In[ ]:


# The mean is the arithmetic average of a set of numbers, or distribution. It is the most commonly used measure of
# central tendency of a set of numbers. ... A mean is computed by adding up all the values and dividing that score 
# by the number of values. The Median is the number found at the exact middle of the set of values.


# ## 9. Describe how a scatter plot can be used to investigate bivariate relationships. Is it possible to find outliers using a scatter plot?

# In[ ]:


# The scatter diagram graphs pairs of numerical data, with one variable on each axis, to look for a relationship
# between them. If the variables are correlated, the points will fall along a line or curve. The better the
# correlation, the tighter the points will hug the line.
# If there is a regression line on a scatter plot, you can identify outliers.


# ## 10. Describe how cross-tabs can be used to figure out how two variables are related.

# In[ ]:


# To describe the relationship between two categorical variables, we use a special type of table called a 
# cross-tabulation (or "crosstab" for short). In a cross-tabulation, the categories of one variable determine
# the rows of the table, and the categories of the other variable determine the columns.

