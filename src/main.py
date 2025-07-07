from code.utils import setup_logger

logger = setup_logger(name="main")

def main():
    print("Hello from src!")


if __name__ == "__main__":
    logger.info("Starting CodeLens")
    main()
