import logging

def setup_logger(logging_enabled: bool, debug_mode: bool):
    """
    Configure logger based on environment variables.
    
    Args:
        logging_enabled (bool): Enable/disable logging.
        debug_mode (bool): Enable/disable debug-level logging.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("Sifty_HTS")
    logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if debug_mode else logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    
    # Add handler only if logging is enabled
    if logging_enabled:
        logger.addHandler(console_handler)
    
    return logger 