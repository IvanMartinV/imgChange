import time
import sys
from helper import *


print("Programa programeando ....... Presiona Ctrl+C to stopit.")

try:
    folders_creator()

    while True:
        move_rename()
        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopeado correctamente. =) ")
    sys.exit(0)