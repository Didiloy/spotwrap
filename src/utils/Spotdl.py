import asyncio
import os
import sys

from savify import Savify, Quality
from savify.utils import PathHolder
from spotdl import Spotdl

from src.utils.Config import Config


class SpotdlSingleton:
    __instance__ = None

    def __init__(self):
        """ Constructor.
       """
        if SpotdlSingleton.__instance__ is None:
            SpotdlSingleton.__instance__ = self
            loop = (
                asyncio.new_event_loop()
                if sys.platform != "win32"
                else asyncio.ProactorEventLoop()  # type: ignore
            )
            asyncio.set_event_loop(loop)
            if loop is None:
                asyncio.set_event_loop(loop)
            self.spotdl: Spotdl = Spotdl(os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET"), loop=loop)
            self.savify: Savify = Savify(api_credentials=(os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET")), quality=Quality.Q192K, path_holder=PathHolder(downloads_path=Config.get_instance().SAVE_PATH), skip_cover_art=False, retry=1, logger=Config.get_instance().logger)

        else:
            raise Exception("You cannot create another SpotdlSingleton class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not SpotdlSingleton.__instance__:
            SpotdlSingleton()
        return SpotdlSingleton.__instance__
