#!/usr/bin/env python3
"""Build the Intercom API tube-style map.

Intercom ships a single OpenAPI surface with 9 functional tags; mapped here
onto 3 product lines.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

LINES = [
    {
        "name": "Customer Data",
        "color": "#E0245E",
        "stations": [
            ("Admins",   (310, 220)),
            ("Contacts", (520, 190)),
            ("Companies",(720, 190)),
            ("Segments", (920, 220)),
        ],
    },
    {
        "name": "Messaging",
        "color": "#E68B1F",
        "stations": [
            ("Conversations",(310, 380)),
            ("Messages",     (620, 350)),
            ("Data Events",  (920, 380)),
        ],
    },
    {
        "name": "Help Center",
        "color": "#0E9D6E",
        # Closed loop with two stations becomes a back-and-forth — let's make
        # a simple short curve.
        "stations": [
            ("Articles", (480, 540)),
            ("News",     (740, 540)),
        ],
    },
]

INTERCOM_API = "https://apis.apis.io/apis/intercom/intercom-api/"
URL_OVERRIDES = {st: INTERCOM_API for ln in LINES for (st, _) in ln["stations"]}


def main():
    n = len({st for ln in LINES for (st, _) in ln["stations"]})
    build_subway(
        title="The Intercom API · Underground Map",
        subtitle=f"{n} functional areas · {len(LINES)} subway lines · click any station for the apis.io page",
        lines=LINES,
        source_label="Source: intercom/openapi/intercom-openapi.yml · github.com/api-evangelist/intercom",
        out_dir=Path(__file__).resolve().parent,
        out_basename="intercom-subway-map",
        provider_id="intercom",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
