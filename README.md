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

##  **Project Workflow**:

 - **Exploratory Data Analysis (EDA)**

      Uncovered patterns indicating that TRANSFER and CASH_OUT transactions are more prone to fraud.
      
      Fraud transactions often occur during the night.
      
      Distinction between Merchant (M) and Customer (C) accounts using prefixes in account names.

- **Feature Engineering**

     Amount to Balance Ratio: Indicates how much of the origin balance is being transacted.
     
     Origin & Destination Balance Change: Captures the actual balance movement.
     
     Hour of Day & Hour Category: Helps identify time-based fraud trends (Morning, Afternoon, Evening, Night).

     Flags for suspicious patterns, like when the amount equals the full balance change.

- **Modeling**

    Models trained:

     Logistic Regression
     Decision Tree Classifier
     Random Forest Classifier
     AdaBoost Classifier

     Class imbalance handled using SMOTE (Synthetic Minority Oversampling Technique).

- **Results**

    Achieved ~83% accuracy on the sampled dataset.
    
    Feature importance revealed transaction type, origin balance changes, and time of transaction as key predictors.

- **Deployment**

    Built a Streamlit App that enables users to input transaction details and get real-time fraud predictions.
    
    Backend intelligently calculates engineered features like balance ratios and flags based on minimal user inputs.

## **EDA**

1. **Distribution of Numerical Feature**
   <img width="1783" height="2042" alt="image" src="https://github.com/user-attachments/assets/18a78f73-4eda-47b7-a859-23416909ff06" />

   - Most transactions are small to medium, but a few large ones stand out—potential signs of fraud.
   - Senders usually have low balances, but some accounts show sudden large changes, hinting at draining or dumping of funds.
   - Fraud and flagged transfers are rare, but the few that exist involve large amounts, suggesting the system catches some but misses others.
   - Most balance changes are minor, but occasional big jumps may signal fraudulent activity.
   Typically, transactions are a small part of the sender’s balance, but some unusually large ratios suggest risky or suspicious behaviour.

2. **Distribution of Categorical Feature**
   <img width="1784" height="919" alt="image" src="https://github.com/user-attachments/assets/75269e42-2547-42a8-9a8e-89166da291e5" />

   - Most transactions are CASH-OUT and PAYMENT, with TRANSFER and CASH-IN next, and DEBIT is the least common. This shows cash movements and payments dominate activity.
   - Almost all transactions are non-fraudulent (0), with very few marked as fraudulent (1). Fraud is super rare here.
   - Almost all senders are customers (C), with no significant merchant (M) activity. Customers drive most transactions.
   - Most recipients are customers (C), but some are merchants (M), showing money often goes to both.
   - Transactions peak in the Afternoon and Evening, with Morning next, and Night is the least busy. Activity follows daily patterns!
  
3. **Which Transaction Types are Most Common in Frauds**
   <img width="784" height="484" alt="image" src="https://github.com/user-attachments/assets/45750b5f-5d9e-46ed-90a0-b0bdb6ef335b" />
   Most fraudulent transactions are CASH-OUT and Transfer , with a count around 4000, showing fraudsters love to pull money out after taking control.

4. **How Much Money is Moved in Frauds?**
   <img width="984" height="484" alt="image" src="https://github.com/user-attachments/assets/e844d6a5-e58c-457d-93e3-32bf70bbf293" />
   This insight suggests that while fraud can occur at any amount, fraud detection systems should be particularly attentive to both small frequent transactions and rare high-value transactions, as both are    common in fraud patterns.

5. **How Do Balances Change in Frauds?**
   <img width="1184" height="484" alt="image" src="https://github.com/user-attachments/assets/40cf311e-f647-4086-9b11-f6c87b7029d4" />

   - **Origin**: Most fraudulent transactions cause a significant reduction in the origin balance, typically matching the transaction amount.
   - **Destination**: The destination balance often shows a negative or negligible change, indicating that the credited balance may not reflect the transaction fully (e.g., immediate withdrawal, intermediary accounts).
     
6. **Top 10 Most Frequent Fraudulent Accounts**
   <img width="984" height="484" alt="image" src="https://github.com/user-attachments/assets/5f14a123-485d-4711-a3ba-112433a66ba3" />

7. **What is the distribution of fraud across different time categories (Hour_Category) — like Night, Morning, Evening, etc.?**
   <img width="784" height="484" alt="image" src="https://github.com/user-attachments/assets/b2eaa836-47e3-4b04-ab1e-17e0e1eb83ec" />
   Night and Morning have the highest fraud occurrences.
   Fraud is less frequent in the Evening and Afternoon.
   Fraudsters are more active during night hours, possibly due to reduced monitoring.













