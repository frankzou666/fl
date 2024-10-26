
class BaseConfig():
    HOST = "0.0.0.0"
    PORT = 5005


class DevConfig(BaseConfig):
    pass

class ProdConfig(BaseConfig):
    SECRET_KEY = 'helloabc'

    #mysql dbconfig
    MYSQL_USER = 'app'
    MYSQL_PWD = 'app123456'
    MYSQL_HOST = '192.168.1.146'
    MYSQL_PORT = '11337'
    MYSQL_DB = 'dp'




#当前使用哪个配置，ProdConfig，或是 DevConfig
class ConfigInfo(ProdConfig):
    pass
