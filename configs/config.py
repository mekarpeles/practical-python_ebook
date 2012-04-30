import ConfigParser

config = ConfigParser.ConfigParser()
config.read('configs/book.cfg')
DEBUG_MODE = bool(config.get("server", "debug"))
