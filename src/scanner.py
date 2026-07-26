from browsers.chrome import scan as chrome_scan
from browsers.edge import scan as edge_scan
from browsers.brave import scan as brave_scan
from browsers.opera import scan as opera_scan

def scan():

    result = []

    result.extend(chrome_scan())
    result.extend(edge_scan())
    result.extend(brave_scan())
    result.extend(opera_scan())

    return result
