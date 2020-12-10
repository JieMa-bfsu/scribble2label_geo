from torch.utils.tensorboard import SummaryWriter
from pathlib import Path
import matplotlib.pyplot as plt
plt.switch_backend('agg')


def init_tb_logger(directory, log_file_name):
    
    log_path = Path(directory, log_file_name)
    print(log_path)
    tb_logger = SummaryWriter(log_dir=log_path)
    
    return tb_logger
