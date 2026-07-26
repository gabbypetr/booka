from src.risk import calculate

def test_high():

    assert calculate([
        "tabs",
        "proxy"
    ]) == "High"


def test_low():

    assert calculate([
        "storage"
    ]) == "Low"
