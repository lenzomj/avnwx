"""
Fetches wind/temp point data
API: /api/data/windtemp
Parameters:
    region: Region
        - all: All sites
        - bos: Northeast
        - mia: Southeast
        - chi: North central
        - dfw: South central
        - slc: Rocky mountain
        - sfo: Pacific coast
        - alaska: Alaska
        - hawaii: Hawaii
        - other_pac: Western Pacific
    level: Level
        - low
        - high
    fcst: Forecast cycle
        - 06
        - 12
        - 24
"""

import json
import requests

from enum import Enum
from .spec import API_BASE


class Region(Enum):
    """
    Region
    """

    ALL = "all"
    BOS = "bos"
    MIA = "mia"
    CHI = "chi"
    DFW = "dfw"
    SLC = "slc"
    SFO = "sfo"
    ALASKA = "alaska"
    HAWAII = "hawaii"
    OTHER_PAC = "other_pac"


class Level(Enum):
    """
    Level
    """

    LOW = "low"
    HIGH = "high"


class ForecastCycle(Enum):
    """
    Forecast cycle
    """

    SIX = "06"
    TWELVE = "12"
    TWENTY_FOUR = "24"


class WindTemp:
    """
    Fetches wind/temp point data
    """

    ENDPOINT = "/api/data/windtemp"

    @classmethod
    def get(params: dict = {}) -> str:
        """
        Fetches wind/temp point data
        """
        uri = f"{API_BASE}{WindTemp.ENDPOINT}"

        response = requests.get(uri, params=params)
        if response.status_code == 200:
            return response.content.decode("utf-8")
        return None

    def region(self, region: Region) -> "WindTemp":
        """
        Sets region
        """
        self.region = region.value
        return self

    def level(self, level: Level) -> "WindTemp":
        """
        Sets level
        """
        self.level = level.value
        return self

    def fcst(self, fcst: ForecastCycle) -> "WindTemp":
        """
        Sets forecast cycle
        """
        self.fcst = fcst.value
        return self

    def fetch(self) -> str:
        """
        Fetches wind/temp point data
        """
        params = {
            "region": self.region if self.region else Region.ALL.value,
            "level": self.level if self.level else Level.LOW.value,
            "fcst": self.fcst if self.fcst else ForecastCycle.SIX.value,
        }
        return WindTemp.get(params)
