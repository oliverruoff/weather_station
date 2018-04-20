# script used to receive temperature and humidity from DHT22 sensor

import Adafruit_DHT as dht

def get_temp_humid():
    '''
    Returns a tuple containing
    [0] humidity
    [1] temperature
    '''
    # Data pin of DHT22 sensor
    pin = 4
    result = dht.read_retry(dht.DHT22, pin)
    str_result = [str(result[0]), str(result[1])]
    #shorteing value
    if len(str_result[0]) > 4:
        str_result[0] = str_result[0][:4]

    if len(str_result[1]) > 4:
        str_result[1] = str_result[1][:4]

    return str_result
