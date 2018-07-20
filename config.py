import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45'}

# config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}

topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'

with open('exemple.ini', 'w') as configfile:
    config.write(configfile)