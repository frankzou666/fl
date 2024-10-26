

from fl import  create_app
from config import ConfigInfo

def main():
    # production:ProdConfig, dev: DevConfig
    config = ConfigInfo
    app = create_app(config)
    app.run(host= config.HOST,port=config.PORT)


if __name__ == '__main__':
    main()