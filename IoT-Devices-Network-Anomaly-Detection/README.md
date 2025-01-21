# Iot Devices Network Anomany Detection using Machine Learning
<p align=center><img width="650" height="200" alt="image" src="https://github.com/user-attachments/assets/8269c152-175b-4404-8dc1-33fa57f6d708" /></p>

## Introduction

The Internet of Things (IoT) connects devices through sensors, software, and the internet, enabling real-time data exchange across industries. However, as the number of connected devices grows, IoT systems face significant security vulnerabilities. Traditional security methods, designed for static networks, struggle to address the dynamic and resource-limited nature of IoT environments, increasing the risk of sophisticated cyber-attacks.

Machine learning (ML) offers a transformative solution for enhancing IoT security by detecting anomalies in real time. ML algorithms can identify unusual patterns, preventing breaches before they cause harm. Predictive models, powered by ML, anticipate future attack vectors, improving proactive security measures. Despite the challenges of resource-constrained IoT devices, research is focused on lightweight ML models that are computationally efficient and tailored for edge computing environments, processing data locally to reduce latency and improve security responsiveness.

## Methodology

The proposed model classifies IoT network traffic as either normal or malicious using a dataset split into 70% training, 15% validation, and 15% testing. Machine learning algorithms like Logistic Regression, Naive Bayes, Decision Trees, Random Forest, Multi-Layer Perceptron, Support Vector Machines, and XGBoost are employed to address the high-dimensional and complex nature of IoT data.

The IoT Environment Dataset, stored in PCAP files, provides detailed network traffic data for analysis. Models are optimized during training and validation phases, with configurations adjusted as needed to improve performance. Final evaluation metrics, including accuracy, precision, recall, and F1-score, identify the most effective model for deployment.

Successful models are integrated into IoT infrastructures using multi-core CPU systems for real-time processing. The proposed solution is scalable, efficient, and adaptive, enabling high accuracy in threat detection while accommodating diverse IoT environments and resource constraints.

<img width="800" alt="image" src="https://github.com/user-attachments/assets/f853d177-2203-4efb-8cd7-900f461fb9ae" />

## Dataset

The IoT Environment Dataset, accessible via iot-environment-dataset, contains detailed network traffic data captured from diverse IoT setups. The raw PCAP files include attributes like source/destination IPs, packet lengths, protocol types, timestamps, and payload data. For machine learning purposes, these files are **converted to CSV format using the CIC FlowMeter tool, aligning the data with IEC 60870-5-104 protocols.**

The dataset includes **over 82 feature columns,** with a critical subset selected to optimize modeling and computational efficiency. **The target variable, defined as Normal or Anomaly**, is converted into binary format for classification. Each instance is meticulously labeled with attack categories and subcategories, providing a robust foundation for IoT security analysis.

-  **Original Raw Dataset Link**
  - https://ocslab.hksecurity.net/Datasets/iot-environment-dataset

- **OneDrive - Dataset Link (Transformed CSVs)**
  - https://sjsu0-my.sharepoint.com/:f:/g/personal/eshita_gupta_sjsu_edu/EiHofOROEeBMtwQWZ2kyRNMBAC9X7zoHPp5WFgm1xpDTsg?e=y8Qtaa

- **Code Walkthrough**
  - https://youtu.be/nMrNFKnjgoE

## Preprocessing
<img width="613" alt="image" src="https://github.com/user-attachments/assets/272e57a9-3b4c-4a85-8fc6-40a2583b3389" />

- **Raw Data Capture:** Network traffic data (normal and malicious) is captured in PCAP format using Wireshark, containing details like source/destination IPs, packet lengths, protocol types, and timestamps.
- **Filtering:** PCAP files are filtered to separate normal from malicious traffic, ensuring tailored feature extraction for anomaly detection.
- **Feature Extraction:** CIC FlowMeter extracts 82+ features (e.g., byte sizes, packet intervals, flags) to enhance dataset descriptiveness.
- **Format Conversion:** Extracted features are converted to a standardized CSV format, compatible with data science tools.
- **Dataset Merging:** Individual CSV files are unified into a comprehensive dataset, including a label column (Normal or Attack) for supervised learning.
- **Feature Selection**: Feature selection involved removing low-impact columns such as timestamps, IP addresses, ports, and UDP protocol data, scaling numerical features while analyzing outliers, and reducing redundancy by dropping highly correlated features using a correlation matrix. The Shapiro-Wilk test validated that 45% of the features followed a normal distribution. These steps ensure the chosen features improve model accuracy and performance, providing a strong basis for anomaly detection in IoT environments.

**Outcome:** The structured and feature-rich dataset ensures optimal readiness for machine learning anomaly detection models.

## Modeling
This study presents a machine learning model for classifying IoT network packets as normal or malicious. Using a PCAP-based dataset split into training, validation, and testing, algorithms like Logistic Regression, Random Forest, and XGBoost are evaluated for accuracy, precision, recall, and F1-score. Optimized models are deployed on multi-core CPUs for real-time IoT security, offering scalable, adaptive, and cost-effective threat detection. Continuous re-training ensures the model remains accurate and effective across diverse IoT environments.

- **Naive Bayes**
  - Achieved an overall accuracy of 89.65% with precision of 0.85, recall of 0.996, and F1 score of 0.916
  - Hyperparameter tuning using grid search optimized the model with priors set to [0.5, 0.5], though this occasionally led to misclassification of normal traffic as attacks
- **Logistic Regression**
  - Demonstrated excellent performance with 97.91% accuracy, 0.967 precision, 0.997 recall, and 0.982 F1 score
  - Optimal parameters were identified through grid search, including C=10, max_iter=10000, multi_class=ovr, penalty=l1, and solver=liblinear
- **Support Vector Machine (SVM)**
  - Achieved strong results with 96.98% accuracy, 0.952 precision, 0.996 recall, and 0.974 F1 score
  - Grid search optimization identified optimal parameters including C=500, dual=False, max_iter=10000, and penalty='l1'
- **Decision Trees**
  - Demonstrated exceptional performance with 99.73% accuracy, 0.997 precision, 0.998 recall, and 0.998 F1 score
  - Achieved perfect performance metrics (1.00) for both normal and attack classes without requiring hyperparameter tuning
- **Random Forest**
  - Showed outstanding results with 99.79% accuracy and consistent scores of 0.998 for precision, recall, and F1
  - Baseline model performed so well that hyperparameter tuning was deemed unnecessary
- **Multi-Layer Perceptron (MLP)**
  - Achieved 91.97% accuracy with 0.998 precision, 0.859 recall, and 0.924 F1 score
  - Demonstrated high performance across all metrics with scores above 0.85 for both normal and attack classes
- **XGBoost**
  - Exhibited exceptional performance with 99.80% accuracy and 0.998 scores for precision, recall, and F1
  - Achieved perfect scores (1.00) for both normal and attack classes without requiring hyperparameter tuning

**Model Comparison & Results**

<img width="779" alt="image" src="https://github.com/user-attachments/assets/a806345a-f527-4fad-ae9e-56fe390f73f2" />

## Conclusion
The experiment compares various algorithms using precision-recall curves, ROC curves, and performance metrics, focusing on accuracy and execution time. XGBoost was the top-performing baseline model with 99.8% accuracy, while Logistic Regression was the best-tuned model at 97.9%. A detailed comparison of metrics such as AUC, TPR, FPR, and final score reveals XGBoost's superior performance, achieving a balanced score of 0.9981. Overall, XGBoost is identified as the best model for anomaly detection in IoT environments, demonstrating high accuracy, precision, recall, and F1-score for reliable security.

|Precision-Recall Curves for Best Models|Comparing Metrics & Final Scores|
|---|---|
|<img width="387" alt="image" src="https://github.com/user-attachments/assets/dfe0206b-1132-430b-ad3d-85de52d3615f" />|<img width="417" alt="image" src="https://github.com/user-attachments/assets/4fc420cd-2bc7-4dde-aee2-5328455274a4" />| 

## Project Extensions & Future Scope
- **Extended Dataset Testing:** Future work should involve testing more datasets from different environments to fur- ther clarify the performance, time cost, and comparison between the methods used in this study. This can provide a broader understanding of the models’ generalizability and robustness.
- **Enhanced Feature Engineering:** Continued focus on feature engineering could yield even better performance. Exploring additional features and refining the selection process can further improve model accuracy.
- **Advanced Hyperparameter Tuning:** Employing more sophisticated hyperparameter tuning techniques, such as Bayesian optimization, could further enhance the perfor- mance of the models.
- **Real-time Implementation:** Developing real-time anomaly detection systems based on the findings could provide practical insights into the deployment and effectiveness of these models in live IoT environments.

## License
MIT License

Copyright (c) 2024 Eshita Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
