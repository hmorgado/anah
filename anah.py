import logging
import sys
import configparser


class ConfigStuff:
    config = configparser.ConfigParser()
    config.read('example.ini')
    print(config.sections())

c = ConfigStuff()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

logging.debug('wont see')

def check(w1, w2):
    m1, m2 = {}, {}

    for i in w1:
        m1.update({i: w1.count(i)})

    logging.info("**".join(m1))

    for i in w2:
        m2.update({i: w2.count(i)})
    logging.info("**".join(m2))

    logging.critical("whoa")
    print(m1 == m2)

check("amor", "roma")