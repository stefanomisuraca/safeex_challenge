
from datetime import datetime
from typing import Dict, List
import requests
import base64
import os
import json


ASTRO_API_KEY = os.getenv("ASTRO_API_KEY")
ASTRO_API_BASE_URL = os.getenv("ASTRO_API_BASE_URL")


class MoonApi:

    def __init__(self, **kwarg) -> None:
        self.lat = kwarg.get("lat")
        self.lon = kwarg.get("lon")
        self.date = kwarg.get("date")
        self.request_body = {
            "format": "png",
            "style": {
                "moonStyle": "default",
                "backgroundStyle": "solid",
                "backgroundColor": "grey",
                "headingColor": "white",
                "textColor": "white"
            },
            "observer": {
                "latitude": self.lat,
                "longitude": self.lon,
                "date": self.date
            },
            "view": {
                "type": "landscape-simple",
                "orientation": "north-up"
            }
        }
    def _request_lunar_phase(self) -> List[Dict]:
        
        headers = {
            'Authorization': f'Basic {ASTRO_API_KEY}',
            'Content-Type': 'application/json'
        }

        response = requests.post(
            headers=headers,
            # url=f"{ASTRO_API_BASE_URL}/studio/moon-phase",
            url="https://api.astronomyapi.com/api/v2/studio/moon-phase",
            json=self.request_body
        )
        return response.json()

    
    def get_lunar_phase(self) -> List[Dict]:
        return self._request_lunar_phase()


def get_lunar_phase_service(
    lat=55,
    lon=12,
    date=datetime.now().strftime('%Y-%m-%d')
) -> List[Dict]:
    moon_api = MoonApi(lat=lat, lon=lon, date=date)
    return moon_api.get_lunar_phase()
    
