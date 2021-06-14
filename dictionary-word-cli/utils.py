import os
def create_data_folder():
    if not os.path.exists('data'):
        os.mkdir('data')
        print('data folder was created')