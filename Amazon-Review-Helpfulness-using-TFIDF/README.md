# Harnessing Helpfulness: Amazon Product Reviews to Elevate Marketplace Experience
<p align=center><img src="https://github.com/user-attachments/assets/09c7613b-01ed-4825-ac39-ad01fc3e65c5"> </img></p>


# Overview of Project

Reviews have become an essential part of the online shopping experience. Reviews serve as the means for customers to make well-informed decisions on the quality of the product and services offered after the purchasing of the product. The E-commerce experience is evolving in the digital era, transforming how purchase decisions are made after validating the reviews. There is a shift in the perception and behaviors of customers. Recent research suggests that 77% of shoppers explicitly seek out websites with reviews and ratings. Our research aims to smoothen the decision-making process by evaluating customer insights and understanding what they find most helpful about products based on reviews. In this study, we are attempting to classify the reviews as being helpful or not based on their content, metadata, sentiment, and relevance to the product. This study has dual benefits - insights about review helpfulness can benefit both stakeholders in the marketplace, i.e., buyers/customers and sellers.

# Data Overview

The dataset we focused on is a subset of the “Amazon Review Data (2018)” published by  Ni (2018), UCSD. The dataset contains a total of 233.3 million reviews and different categories, and these reviews are in the range of May 1996 to Oct 2018. For our project, we will consider the data from 2010-2018 and only the objective categories, including appliances, automotive, cell phones and accessories, and tools and home improvement.


# Data Preprocessing

Data pre-processing is a critical step in any data analysis or machine learning project. Methods like removing noise or irrelevant information, removing missing vsalues, cleaning data, and preparing data well for further analysis and modeling to get higher accuracy and correct predictions of helpfulness of reviews. Explore the notebooks for each category for further details.

# Data Transformation

Data transformation involves cleaning, integration, organizing, aggregation, and enriching the data for modeling. Since our data was large to process in limited computational resources, hence we used stratified sampling which is a representative of the overall data. For transformation on reviewTitle and reviewText the steps involved are determining number of words in the review, review length, analysis of sentiment polarity, identifying active reviewers, calculating age of the review. Additionally, we also performed tokenization, stop word removal, and lemmatization. TF-IDF vectorizer was created and distribution of top n-gram was visualized. Data transformation helps us improve the quality of the data which then can be used in modeling. Explore the notebooks for each category for further details on data transformation.

# Data Preparation 

Once we decided on the final modeling dataset, we split it into X and y. X contains all the features, while y contains the target. Preparing the data for modeling is essential, and we are creating three sets: a training dataset, a testing dataset, and a validation dataset. We split the transformed data into 70:15:15 for training, testing, and validation, respectively. This split will help us balance training, testing, and validation for modeling .

# Machine Learning

We attempted various models for classification, such as Logistic Regression, Support Vector Machine (SVM), as well as tree-based ensemble models like Random Forest and XGBoost on the training dataset
Our approach involved in building baseline models for all the algorithms for each of the chosen product categories. The baseline models will be built with default parameters to establish an initial benchmark, which will be improved in the next stage i.e. fine-tuned models. We will employed method like grid search to find the optimal hyperparameters for each model. Furthermore, we have fine-tuned the models based on the optimal hyperparameters obtained. Once we had our models, we can used our trained models to predict the target variable on the test data – this is done since we can compare the predicted and actual values of the target variable in the test dataset, which will help us compute the confusion matrix and various model performance metrics called accuracy, precision, recall, F1-score etc.
Finally, the best model <> was be chosen for each product category and analyzed, and the results were compared with all the other models for each category.

There were two approaches taken for modelling:
For Appliances, Automotive, and Cellphones & Accessories categories we used TF-IDF feature matrix with 1000 feature and metadata features were considered.Another approach we explored was to use sample weights to offset the imbalance in the “Tools & Home Improvement” category. First approach gave the better accuaracy and second apporach gave moderate recall and ROC. 

# Conclusion and Recommendations

Models for three categories “Appliances, Automotive and Cellphones & Accessories” have have high accuracy but low precision and recall, it can be attributed to the fact that our data is imbalanced and has high dimentionality. Our data has the majority class as “Not Helpful” with “Helpful” being the minority class. It's representative of real world data since helpful reviews are limited and exclusive. Since we are using metadata and TF-IDF features, we have a high number of dimensions. We can use dimensionality reduction techniques like PCA but the trade-off is that our model explainability will be limited. Additional features that we have not considered are likely features around human behavior that can’t be quantified, and hence, helpfulness is almost inherently unpredictable. We attempted iterations of the model with limited TF-IDF features (100), a larger TF-IDF feature matrix (2000), and another iteration with only metadata features however, the results did not change much across the iterations, indicating that our current set of features are not adequate to accurately predict helpfulness.

Another approach we explored was to use sample weights to offset the imbalance in the “Tools & Home Improvement” dataset. We were able to make the models focus more on the minority class that is “helpful” reviews. We were able to get decent recall values and an ROC score of more than 0.75, however, that was achieved at the cost of accuracy and precision. With this, we could interpret that Accuracy is not the only metric that should be considered for our use case, precision and recall are extremely important to determine whether the models are able to capture true positives. We noticed that with sample weights, we had to trade-off accuracy to allow models to capture more true positives while introducing some noise. Given these observations, we conclude that even though we were able to arrive at the helpfulness with a certain degree of accuracy, these models do not perform optimally. The takeaway is that it is difficult to clearly separate helpful vs. non-helpful reviews using multiple classification techniques that we attempted as the performance for our models was sub-optimal and did not strike a balance. 

# File Structure

`DataCollection_Amazon_Review.ipynb` : This file contains the details of the conversion of JSON data to CSV for each category

`Appliances_Textmining_Modeling_Final` : This file contains the Data preprocessing, data transformation, and modeling for appliances category

`Automotive_Textmining_Modeling_Final.ipynb` : This file contains the Data preprocessing, data transformation, and modeling for automotive category

`Cellphone_and_Accessories_Textmining_Modeling_Final.ipynb` : This file contains the Data preprocessing, data transformation, and modeling for cellphones & accesories category

`Tools_SuperSet_Textmining_Modeling_Final.ipynb` : This file contains the Data preprocessing, data transformation, and modeling for tools & home improvement category

`Appliances_Pickle_Files.zip` : Pickle files for appliances category

`Automotive_Pickle_Files.zip` : Pickle files for automotive category

`Cellphone_Pickle_Files.zip` : Pickle files for cellphone and accessories category

`Tools_SuperSet_Modeling_pickles.zip` : Pickle files for tools and home improvement category

`Demo_file_all_categories.ipynb` : This is a demo file to run the models using pickle files


# Contact Information
For inquiries or feedback, contact:

Eshita Gupta : eshita.gupta@sjsu.edu

Monica Lokare : monica.Lokare@sjsu.edu

Sneha Karri : sneha.karri@sjsu.edu

Veena Ramesh Beknal : veenaramesh.beknal@sjsu.edu


Explore the project and leverage insights from the Amazon product reviews data for specific catgories !
