import configparser

config = configparser.ConfigParser()
config.sections()

config.read('example.ini')

print(config.sections())

for key in config['bitbucket.org']: print(key)
