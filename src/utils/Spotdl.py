#     This file is part of SpotWrap.
#     Copyright (C) 2023  Dylan Loya
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
import asyncio
import os
import sys

from spotdl import Spotdl

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
        else:
            raise Exception("You cannot create another SpotdlSingleton class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not SpotdlSingleton.__instance__:
            SpotdlSingleton()
        return SpotdlSingleton.__instance__
