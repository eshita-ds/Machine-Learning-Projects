## Iot Devices Network Anomany Detection using Machine Learning


As the proliferation of smart devices and the Internet continues, the Internet of Things (IoT) has become an integral part of our daily lives and industrial operations. IoT technologies enable manufacturing companies to monitor the
status of machines in real-time, assess product quality, and track environmental conditions within production facilities. This capability not only reduces the risk of damage and loss but
also empowers managers to make informed decisions from
a comprehensive perspective. Moreover, IoT has transformed
consumer lifestyles and behaviors, with an increasing reliance
on IoT devices and services. However, the presence of anomalies
in IoT networks can pose significant security and safety
challenges, necessitating robust mechanisms for their detection
and resolution to prevent potential damages. In this paper, we
propose an advanced approach using machine learning (ML)
techniques to enhance the security framework of IoT networks.
Our methodology involves the deployment of multiple ML models,
including Logistic Regression,Naive Bayes, Random Forest,
Support Vector Machines, Multi-Layer Perceptron and XG Boost
to detect and classify anomalous traffic behaviors within IoT
networks effectively. The experimental analysis is conducted
using the IoT Network Intrusion Dataset-Hk Security, focusing
on model efficiency and the identification of optimal strategies
for real-time anomaly detection. We aim to demonstrate the
effectiveness of these models in improving IoT network security,
thereby mitigating risks and enhancing operational reliability

## Introduction

The Internet of Things (IoT) connects devices through sensors, software, and the internet, enabling real-time data exchange across industries. However, as the number of connected devices grows, IoT systems face significant security vulnerabilities. Traditional security methods, designed for static networks, struggle to address the dynamic and resource-limited nature of IoT environments, increasing the risk of sophisticated cyber-attacks.

Machine learning (ML) offers a transformative solution for enhancing IoT security by detecting anomalies in real time. ML algorithms can identify unusual patterns, preventing breaches before they cause harm. Predictive models, powered by ML, anticipate future attack vectors, improving proactive security measures. Despite the challenges of resource-constrained IoT devices, research is focused on lightweight ML models that are computationally efficient and tailored for edge computing environments, processing data locally to reduce latency and improve security responsiveness.

## Methodology

The proposed model classifies IoT network traffic as either normal or malicious using a dataset split into 70% training, 15% validation, and 15% testing. Machine learning algorithms like Logistic Regression, Naive Bayes, Decision Trees, Random Forest, Multi-Layer Perceptron, Support Vector Machines, and XGBoost are employed to address the high-dimensional and complex nature of IoT data.

The IoT Environment Dataset, stored in PCAP files, provides detailed network traffic data for analysis. Models are optimized during training and validation phases, with configurations adjusted as needed to improve performance. Final evaluation metrics, including accuracy, precision, recall, and F1-score, identify the most effective model for deployment.

Successful models are integrated into IoT infrastructures using multi-core CPU systems for real-time processing. The proposed solution is scalable, efficient, and adaptive, enabling high accuracy in threat detection while accommodating diverse IoT environments and resource constraints.

<img width="670" alt="image" src="https://github.com/user-attachments/assets/50168474-80d2-4228-b13e-8f4029b2d628" />

## Dataset

The IoT Environment Dataset, accessible via iot-environment-dataset, contains detailed network traffic data captured from diverse IoT setups. The raw PCAP files include attributes like source/destination IPs, packet lengths, protocol types, timestamps, and payload data. For machine learning purposes, these files are **converted to CSV format using the CIC FlowMeter tool, aligning the data with IEC 60870-5-104 protocols.**

The dataset includes **over 82 feature columns,** with a critical subset selected to optimize modeling and computational efficiency. **The target variable, defined as Normal or Anomaly**, is converted into binary format for classification. Each instance is meticulously labeled with attack categories and subcategories, providing a robust foundation for IoT security analysis.

### Original Raw Dataset Link
https://ocslab.hksecurity.net/Datasets/iot-environment-dataset

### OneDrive - Dataset Link (Transformed CSVs)
https://sjsu0-my.sharepoint.com/:f:/g/personal/eshita_gupta_sjsu_edu/EiHofOROEeBMtwQWZ2kyRNMBAC9X7zoHPp5WFgm1xpDTsg?e=y8Qtaa

### Code Walkthrough
https://youtu.be/nMrNFKnjgoE
