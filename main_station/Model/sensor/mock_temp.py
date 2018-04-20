# script used to mock temperature and humidity from DHT22 sensor

def get_temp_humid():
    '''
    Returns a tuple containing mocked
    [0] temperature
    [1] humidity
    '''
    temp = '22.52345345'
    humi = '74.34534534'

    #shorteing value
    if len(str(temp)) > 4:
        temp = temp[:4]

    if len(humi) > 4:
        humi = humi[:4]

    return humi, temp
