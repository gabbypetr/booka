from models import Extension

def scan():

    return [

        Extension(
            browser="Chrome",
            name="uBlock Origin",
            version="1.62",
            permissions=[
                "storage"
            ],
            risk="Low"
        ),

        Extension(
            browser="Chrome",
            name="Sample Extension",
            version="2.1",
            permissions=[
                "tabs",
                "history"
            ],
            risk="High"
        )

    ]
