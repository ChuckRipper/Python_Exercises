import logging

for _ in range(10):
    value = input().strip()
    try:
        int(value)
        logging.info("Podano liczbę całkowitą.")
    except ValueError:
        try:
            float(value)
            logging.warning("Podano liczbę zmiennoprzecinkową.")
        except ValueError:
            logging.error("Nie podano liczby.")
