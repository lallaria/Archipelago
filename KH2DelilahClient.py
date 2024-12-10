import ModuleUpdate
import Utils
from worlds.kh2delilah.Client import launch
ModuleUpdate.update()

if __name__ == '__main__':
    Utils.init_logging("KH2 Delilah Client", exception_logger="Client")
    launch()
