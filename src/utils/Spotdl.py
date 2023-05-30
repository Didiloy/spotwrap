import os

from spotdl import Spotdl


class SpotdlSingleton:
    __instance__ = None

    def __init__(self):
        """ Constructor.
       """
        if SpotdlSingleton.__instance__ is None:
            SpotdlSingleton.__instance__ = self
            self.spotdl: Spotdl = Spotdl(os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"))
        else:
            raise Exception("You cannot create another SpotdlSingleton class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not SpotdlSingleton.__instance__:
            SpotdlSingleton()
        return SpotdlSingleton.__instance__
