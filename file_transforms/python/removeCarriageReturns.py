file = open('/Users/tim.freeman/Downloads/motosport_subscriberid_20190207.csv')

for line in file:
    if '\r' in line:
        print('carriage return')
