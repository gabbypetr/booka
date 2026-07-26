from dataclasses import dataclass

@dataclass
class Extension:

    browser: str
    name: str
    version: str
    permissions: list
    risk: str
