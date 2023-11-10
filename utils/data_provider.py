import json
import os

resources_dir = os.path.join(os.getcwd(), 'resources')


class DataProvider:

    @staticmethod
    def get_file(filename):
        file_path = os.path.join(resources_dir,
                                 filename)
        return open(file_path, "r")


    @staticmethod
    def get_user_data(username) -> dict:
        users_file = DataProvider.get_file('users.json')
        data = json.load(users_file)
        users_file.close()
        return data[username][0]
