import time
import sys
import helper as h


def m_code() -> None:
    try:
        h.folders_creator()

        while True:
            h.move_rename()
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nStopeado correctamente. =) ")
        sys.exit(0)


if __name__ == '__main__':
    print("Starting Main")
    m_code()