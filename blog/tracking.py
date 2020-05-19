from .CONSTANTS import *

from snowplow_tracker import Emitter, Tracker

def create_tracker():
    e = Emitter(SNOWPLOW_MICRO_URL)
    return Tracker(e)