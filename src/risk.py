HIGH = {
    "tabs",
    "webRequest",
    "proxy",
    "nativeMessaging",
    "management"
}

MEDIUM = {
    "cookies",
    "storage",
    "history",
    "downloads"
}

def calculate(permissions):

    score = 0

    for p in permissions:

        if p in HIGH:
            score += 3

        elif p in MEDIUM:
            score += 1

    if score >= 6:
        return "High"

    if score >= 2:
        return "Medium"

    return "Low"
