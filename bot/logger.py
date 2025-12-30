import logging
import os

def setup_logger():
    """
    Logger setup function.
    Ye function ek hi jagah logging configure karta hai
    taaki poore project me same logger use ho.
    """

    # logs folder exist na kare to bana do
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logging.basicConfig(
        filename="logs/bot.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return logging.getLogger()

