import os
import pykitti
from utils import read_data


class DataLoader:
    def __init__(self, basedir, date, drive_num):
        self.data = pykitti.raw(basedir, date, drive_num)
    
    def get_gps_imu(self):
        return self.data.oxts
    
    def get_timestamps(self):
        return self.data.timestamps
    
