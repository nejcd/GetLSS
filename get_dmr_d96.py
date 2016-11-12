import urllib

startN = 453
endN = 464
startE = 116
endE = 129
bloki = [31, 34, 36, 35]

file = urllib.URLopener()

for n in range(startN, endN+1):
    print n

    for e in range(startE, endE+1):
        for b in bloki:
            try:
                url = 'http://gis.arso.gov.si/lidar/dmr1/b_{0}/D96TM/TM1_{1}_{2}.asc'.format(b, n, e)
                fileName = 'TM1_{0}_{1}.asc'.format(n, e)
                print e
                file.retrieve(url, fileName)
            except:
                print 'Ni v tem bloku'
