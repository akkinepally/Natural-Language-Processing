import pandas as pd

customer_df = pd.read_csv('Mall_Customers.csv')
customer_df.Genre = customer_df.Genre.lower()
customer_df.head()[['Genre']]