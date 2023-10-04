from logging import getLogger, StreamHandler, Formatter, INFO, DEBUG, \
    basicConfig

basicConfig(
    filename='/logs/log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=DEBUG
)
logger = getLogger("EmailServiceLogger")
logger.setLevel(INFO)

handler = StreamHandler()

formatter = Formatter(
    "%(asctime)s %(name)s(%(process)d):[%(levelname)s] %(message)s"
)
handler.setFormatter(formatter)

logger.addHandler(handler)
