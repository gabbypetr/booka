from models import Extension

def scan():

    return [

        Extension(
            browser="Edge",
            name="Grammarly",
            version="14.0",
            permissions=[
                "storage",
                "cookies"
            ],
            risk="Medium"
        )

    ]
