import time
import sys
import helper as h


def m_code():
    print("Programa programeando2 .......")

    try:
        h.folders_creator()

        while True:
            h.move_rename()
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopeado correctamente. =) ")
        sys.exit(0)


if __name__ == '__main__':
    print("cacatua")
    m_code()