import sys
import os
import datetime

# Add the 'src' folder to the Python module search path
sys.path.append(os.path.abspath('src'))

from modeller import Modeller

if __name__ == "__main__":
    modeller = Modeller(startDate=datetime.date(2022, 1, 1), endDate=datetime.date(2022, 12, 31))
