import pandas
dataframe = pandas.read_csv('sample.csv') 
print(dataframe["Usernames"])
print("Username: ", dataframe["Usernames"][1], " | ", "Password: ", dataframe["Passwords"][1])
	
print(dataframe.sort_values('Usernames'))
print(dataframe.sort_values('Passwords', ascending=False))