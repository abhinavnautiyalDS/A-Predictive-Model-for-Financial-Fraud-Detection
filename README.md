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

## **Data Preprocessing**

The data preprocessing phase involved multiple essential steps to prepare the dataset for effective fraud prediction modeling. Initially, missing values, especially in balance-related columns, were handled by replacing them with zeros to maintain data integrity and ensure consistent calculations. From the nameOrig and nameDest columns, I extracted the first character to create new features Orig_Type and Dest_Type, which indicate whether an account is a customer or merchant. This helped in understanding the nature of the transaction parties.

To capture the time dynamics of transactions, I derived the Hour_of_day feature by converting the step column into a 24-hour clock using modulo operation. Additionally, I categorized each transaction hour into distinct periods of the day like Morning, Afternoon, Evening, and Night to identify time-based fraud patterns. I calculated org_balance_change and dest_balance_change to quantify the actual change in balances due to transactions, providing direct indicators of suspicious fund movements.

Another crucial feature was the AmountToBalanceRatio_Orig, representing the ratio of transaction amount to the origin account's balance, highlighting cases where almost the entire balance is being transacted. Based on these calculations, I also created flag variables such as flag_org_balance_change, flag_dest_balance_change, and flag_AmountToBalanceRatio_Orig to signal potentially risky behaviors like when the entire balance is transferred or when the ratio is unusually high.

Categorical features such as transaction type, account types, and time categories were encoded using label encoding and one-hot encoding to convert them into machine-readable formats. Numerical features were scaled using Min-Max Scaling to bring them into a uniform range, enhancing model convergence and performance.

Finally, to address the critical issue of class imbalance where fraud cases were significantly fewer than non-fraud cases, I applied SMOTE (Synthetic Minority Oversampling Technique). SMOTE helped generate synthetic fraud examples based on existing minority class data, effectively balancing the dataset. This step was crucial in ensuring that the machine learning models do not become biased towards the non-fraudulent class and can better identify fraudulent activities.

<img width="1183" height="527" alt="image" src="https://github.com/user-attachments/assets/f38fc437-0d91-4025-a5d2-3cd06154064d" />


## **Model Building**


After preprocessing and engineering the data, I proceeded to build and evaluate multiple machine learning models to detect fraudulent transactions. The goal was to compare different algorithms and select the one that best captures the patterns distinguishing fraud from legitimate transactions.

I trained four classification models: Logistic Regression, Decision Tree, Random Forest, and AdaBoost Classifier. Each model was trained on the preprocessed and balanced dataset obtained after applying SMOTE to address the class imbalance between fraud and non-fraud cases.

The Logistic Regression model served as a baseline due to its simplicity and interpretability. The Decision Tree Classifier was used for its ability to capture non-linear relationships and provide feature importance insights. I also trained a Random Forest Classifier, which builds multiple decision trees and aggregates their outputs, reducing overfitting and improving generalization. Lastly, I used the AdaBoost Classifier, which combines multiple weak learners in sequence, focusing more on incorrectly classified instances at each step, thus improving the model’s accuracy.

After training, I evaluated all models based on their accuracy, precision, recall, and F1-score, specifically focusing on how well they detect fraudulent transactions. Despite working on a sampled dataset due to processing constraints, the models performed well, with Random Forest and AdaBoost giving the best performance. The highest accuracy achieved was around 83%, indicating that the model could effectively distinguish between fraudulent and non-fraudulent transactions.

This multi-model approach not only provided a comparative analysis of different algorithms but also ensured that the final selection was backed by robust evaluation across multiple metrics, critical for a fraud detection system where the cost of misclassification is high.
<img width="1273" height="696" alt="image" src="https://github.com/user-attachments/assets/72002265-e3ef-4b7c-8401-f88c2a7c39d4" />

## **Model Deployment**

Once the models were trained and evaluated, I proceeded to deploy the best-performing model using a Streamlit web application. The objective of deployment was to make the fraud detection system accessible and interactive, allowing users to input transaction details and receive real-time predictions on whether a transaction is fraudulent.


![ezgif com-video-to-gif-converter (1)](https://github.com/user-attachments/assets/5d41f058-e0d6-415d-b041-fa855eb72c2b)

## **Future Enhancements**

- Scale model to handle the entire 6 lakh+ rows efficiently.
- Integrate advanced models like XGBoost and LightGBM.
- Implement real-time fraud detection on streaming data pipelines.
= Deploy the app with APIs for integration into banking systems.



## **Conclusion**

In this project, I developed a comprehensive Fraud Detection System by performing deep exploratory data analysis, feature engineering, and training multiple machine learning models on a large financial transaction dataset.
To handle the sheer volume of data (around 6 lakh rows), I extracted a sample of the population for my analysis and modeling. This was essential due to computational limitations on my processor. This sampling might have slightly impacted the model's generalization, resulting in an achieved accuracy of 83% — which is still promising given the data constraints.

**Summary of Work Done**

Performed thorough EDA revealing that fraudulent transactions are primarily associated with TRANSFER and CASH_OUT transaction types.
Identified that frauds mostly occur via corporate (C) accounts and during night hours.
Engineered key features such as:

- Amount to Balance Ratio
- Origin Balance Change
- Destination Balance Change
- Hour of Day Categorization

**Models Trained**
I trained and evaluated four machine learning models:
- Logistic Regression
- Random Forest Classifier
- AdaBoost Classifier
- Decision Tree Classifier
Among these, models like Logistic Regression and Decision Tree performed well on the sample data, with an accuracy of up to 83%.

**Deployment**
I built an interactive Streamlit web application where users can input transaction details and get real-time fraud predictions, powered by the trained machine learning model. The app also features a custom-designed dark-themed background for better visibility.

**Impact**
This system is designed to help financial institutions:

- Detect fraudulent activities promptly.
- Prevent financial losses.
- Strengthen security protocols based on transaction patterns.





















