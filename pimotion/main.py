from pimotion import PiMotion
from cloudapp import CloudAppAPI
from m2x.client import M2XClient
import ConfigParser


Config = ConfigParser.ConfigParser()
Config.read('settings.cfg')


def callback(path):
    api = CloudAppAPI(Config.get('cloudapp', 'username'), Config.get('cloudapp', 'password'))
    url = api.upload(path)
    print 'Public URL: ' + url

    client = M2XClient(Config.get('m2x', 'api_key'))
    feed = client.feeds.details(Config.get('m2x', 'feed_id'))
    result = feed.add_values({Config.get('m2x', 'stream'): [{'value': url}]})
    print result

motion = PiMotion(verbose=True, post_capture_callback=callback)
motion.start()
