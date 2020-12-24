# Check System CPU and RAM

import os
import subprocess
import re

statistics = {}

cpu_count = os.cpu_count()
statistics['cpu_count'] = cpu_count

"""
# Load Average
"""

cpu_load = [x / os.cpu_count() * 100 for x in os.getloadavg()[-1]]
statistics['cpu_load'] = cpu_load