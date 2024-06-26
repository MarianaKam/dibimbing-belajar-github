import pandas as pd

def read_user_file(file_path):

    with open(file_path, 'r') as file:
        data = pd.read_csv(file)
        return data
    
read_user_file('D:/Mariana/learning/dibimbing-belajar-github/username.csv')


