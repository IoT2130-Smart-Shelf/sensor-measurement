def laser_linearization(data):
    if data > 8100:
        return 8190
    elif data < 310:
        data_l = 0.9393*data - 23.943
        return round(data_l,2)
    elif data < 500:
        data_l = 1.0238*data - 50.087
        return round(data_l,2)
    elif data < 860:
        data_l = 1.2657*data - 189.03
        return round(data_l,2)
    elif data < 1010:
        data_l = 0.8114*data+279.98
        return round(data_l,2)
    else: 
        data_l = 0.0385*data + 1125.7
        return round(data_l,2)