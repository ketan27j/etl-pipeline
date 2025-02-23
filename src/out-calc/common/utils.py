def log_message(message, level='INFO'):
    import logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    if level == 'DEBUG':
        logger.debug(message)
    elif level == 'WARNING':
        logger.warning(message)
    elif level == 'ERROR':
        logger.error(message)
    else:
        logger.info(message)

def parallel_execution(func, args_list):
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(func, args_list))
    return results