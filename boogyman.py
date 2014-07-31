import pygerduty
import phue
import soco
import ConfigParser


class boogeyman:
    configFile = "config.ini"

    def setSonosBridge(self,SonosIP=''):
        if not SonosIP:
            return

        self.sonosObj =

    # Allow people to use this even if they don't have one of these devices / applications
    def __init__(self, hue=False, sonos=False, pagerduty=False):
        config = ConfigParser.ConfigParser()
        config.read(self.configFile)

        self.sonosIP = config.get('sonos', 'bridge_ip') if sonos == True else self.sonosIP = False
        self.hueIP = config.get('hue', 'bridge_ip') if hue == True else self.hueIP = False
        self.pdApiKey = config.get('pagerduty','api_key') if pagerduty == False else self.pdApiKey = False

