from configparser import ConfigParser

cp = ConfigParser()
cp.read(".\\configurations\\config.ini")


class GetProperties:

    @staticmethod
    def getURL():

        url = cp.get('common values','base_URL')
        return url

    @staticmethod
    def getID():

        user_id = cp.get('common values','id')
        return user_id

    @staticmethod
    def getPassword():

        password = cp.get('common values','pass')
        return password

