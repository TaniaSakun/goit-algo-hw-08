import random
from cost_saver import print_cables

if __name__ == "__main__":
    cables = [random.randint(1, 100) for _ in range(10)]

    print_cables(cables)
