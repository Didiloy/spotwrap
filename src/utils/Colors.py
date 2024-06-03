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
import json
from typing import Dict

from materialyoucolor.scheme.scheme import Scheme
# from materialyoucolor.utils.theme_utils import getDominantColors, themeFromSourceColor

class Colors:
    __instance__ = None

    def __init__(self):
        """ Constructor.
       """
        if Colors.__instance__ is None:
            Colors.__instance__ = self
            self.SECONDARY_BACKGROUND_COLOR = "rgb(239, 242, 233)"
            self.ON_SECONDARY_BACKGROUND_COLOR = "rgb(0, 0, 0)"
        else:
            raise Exception("You cannot create another Config class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not Colors.__instance__:
            Colors()
        return Colors.__instance__

    # def getDominantColorFromImage(self, image, onColor=False) -> Dict:
    #     argbs = getDominantColors(image, quality=5, default_chunk=128)
    #     argb = argbs[1]  # choose index
    #     color = themeFromSourceColor(argb)
    #     # 40 is for the primary color and 100 is for the onColor
    #     theme = json.loads(color["schemes"]["light"].toJSON())
    #     return theme
