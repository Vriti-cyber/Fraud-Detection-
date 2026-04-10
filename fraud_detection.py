
import pandas as pd                   
import xgboost as xgb                   
from sklearn.model_selection import train_test_split  
from sklearn.metrics import classification_report    
from blockchain import Blockchain       
import os  

print("STEP 1: Loading credit card transaction data...")
if not os.path.exists("creditcard.csv"):
    print("Dataset not found! Please download it and place it in the project folder.")
    exit()

transaction_data = pd.read_csv("creditcard.csv")

print("STEP 1: Loading credit card transaction data...")
transaction_data = pd.read_csv("creditcard.csv") 


features = transaction_data.drop("Class", axis=1)      
actual_labels = transaction_data["Class"]            

X_train, X_test, y_train, y_test = train_test_split(
    features, actual_labels, test_size=0.2, random_state=42  
)


fraud_count = actual_labels.sum()                  
total_transactions = len(actual_labels)           
normal_count = total_transactions - fraud_count      

print(f"Data Summary: {fraud_count} fraud cases out of {total_transactions} total transactions")
print(f"This means only {fraud_count/total_transactions*100:.2f}% are fraudulent!")


fraud_detector = xgb.XGBClassifier(
    n_estimators=300,        
    max_depth=7,             
    learning_rate=0.05,       
    subsample=0.8,            
    colsample_bytree=0.8,     
    random_state=42          
)


print("\nSTEP 2: Training the AI model... (please wait)")
fraud_detector.fit(X_train, y_train)  


print("STEP 3: Testing model on new transactions...")
predictions = fraud_detector.predict(X_test)


print("\n" + "="*60)
print("FINAL RESULTS: How well does our model perform?")
print("="*60)
print(classification_report(y_test, predictions))
print("="*60)

print("\nSTEP 4: Creating blockchain to track all model improvements...")
model_ledger = Blockchain()  

print("STEP 5: Recording updates from different teams...")
model_ledger.add_block("Client 1 - Added new fraud patterns from recent attacks")
model_ledger.add_block("Client 2 - Improved detection for international transactions")
model_ledger.add_block("Client 3 - Updated model with feedback from bank investigators")

print("\n" + "="*60)
print("BLOCKCHAIN LEDGER: Complete Update History (Tamper-Proof)")
print("="*60)
model_ledger.display_chain()
print("="*60)
print("\n✅ SYSTEM READY: Fraud detection model trained and all updates secured!")
print("   Every change to the model is now permanently recorded and cannot be altered.")