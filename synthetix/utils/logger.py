import logging
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class SynthetixLogger:
    def __init__(self, name="Synthetix"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create console handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%H:%M:%S')
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, message):
        self.logger.info(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} {message}")

    def success(self, message):
        self.logger.info(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} {message}")

    def warning(self, message):
        self.logger.info(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} {message}")

    def error(self, message):
        self.logger.info(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {message}")

    def system(self, message):
        self.logger.info(f"{Fore.MAGENTA}[SYSTEM]{Style.RESET_ALL} {message}")

logger = SynthetixLogger()
