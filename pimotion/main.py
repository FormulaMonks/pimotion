from pimotion import PiMotion
from cloudapp import CloudAppAPI
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read('settings.cfg')


def callback(path):
    api = CloudAppAPI(Config.get('cloudapp', 'username'), Config.get('cloudapp', 'password'))
    url = api.upload(path)
    print 'Public URL: ' + url

motion = PiMotion(verbose=True, post_capture_callback=callback)
motion.start()
