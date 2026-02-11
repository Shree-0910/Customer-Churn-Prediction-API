import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

churn = pd.read_csv('/churn.csv')

churn

churn['Churn'].value_counts()

churn.shape

churn.info()

churn.describe()

le = LabelEncoder()

churn['Contract'] = le.fit_transform(churn['Contract'])
churn['InternetService'] = le.fit_transform(churn['InternetService'])

X = churn.drop('Churn',axis=1)
Y = churn['Churn']

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

model = RandomForestClassifier()

model.fit(X_train,Y_train)

pred_rf = model.predict(X_test)

accuracy_rf = accuracy_score(Y_test,pred_rf)
print('Accuracy of Random Forest: ',accuracy_rf)

joblib.dump(model,'model.pkl')
joblib.dump(scaler,'scaler.pkl')