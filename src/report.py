from tabulate import tabulate

def print_report(exts):

    rows = []

    for e in exts:

        rows.append([
            e.browser,
            e.name,
            ", ".join(e.permissions),
            e.risk
        ])

    print(tabulate(
        rows,
        headers=[
            "Browser",
            "Extension",
            "Permissions",
            "Risk"
        ]
    ))
