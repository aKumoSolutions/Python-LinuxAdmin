# Memory Usage in percentage

import psutil 
print(psutil.virtual_memory().percent)
print(psutil.cpu_percent())