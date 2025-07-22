# **Intelligent Financial Transaction Fraud Detection**

![1673420](https://github.com/user-attachments/assets/29d2a2af-9509-4207-8f5a-fff9d2b9b57c)

## **Project Overview**
Fraudulent transactions pose a serious challenge to the financial industry, leading to significant financial losses and reputational damage. This project, FraudGuard, presents an end-to-end fraud detection system that leverages data analysis, feature engineering, and machine learning to predict and prevent fraudulent transactions effectively.

## **🎯 Problem Statement**

The goal of this project is to develop a robust machine learning model that can detect fraudulent transactions in a dataset of over 6 lakh records. The key challenges include:
1. Handling a highly imbalanced dataset.
2. Identifying patterns in transaction types, amounts, time of transactions, and factors responsible for fraud.
3. Building a predictive system capable of real-time fraud detection.
4. Deploying an interactive application for users to assess transaction risk.

## **Data Overview**

- **step**: Represents a unit of time in the real world. In this dataset, 1 step equals 1 hour. The total number of steps is 744, representing a 30-day simulation.

- **type**: Indicates the type of transaction. Possible values are: CASH-IN, CASH-OUT, DEBIT, PAYMENT, and TRANSFER.

- **amount**: The monetary value of the transaction in local currency.

- **nameOrig**: The customer who initiated the transaction.

- **oldbalanceOrg**: The sender's account balance before the transaction.

- **newbalanceOrig**: The sender's account balance after the transaction.

- **nameDest**: The customer who received the transaction.

- **oldbalanceDest**: The recipient’s account balance before the transaction.
Note: For recipients with names starting with "M" (Merchants), this information is not available.

- **newbalanceDest**: The recipient’s account balance after the transaction.
Note: For recipients with names starting with "M" (Merchants), this information is also not available.

- **isFraud**: Indicates whether the transaction was fraudulent. In this dataset, fraudulent agents attempt to take control of customer accounts and drain the funds by transferring them to another account and then cashing out.

- **isFlaggedFraud**: Identifies transactions flagged by the system for suspicious behavior. Specifically, any attempt to transfer more than 200,000 in a single transaction is flagged as potentially illegal.


