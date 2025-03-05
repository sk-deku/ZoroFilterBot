#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("15072022"))

API_HASH = os.environ.get("16b9f1767df306b369039fee1202970d")

BOT_TOKEN = os.environ.get("7204165447:AAHZ_v2ptxjaVW1rsDX-jyeOtPW2W-ZhrRc")

DB_URI = os.environ.get("mongodb+srv://AnimeFireBot: Skesavan7@cluster0.zu5mx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

USER_SESSION = os.environ.get("ZoroAnimeBot")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
