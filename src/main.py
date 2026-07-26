from scanner import scan
from report import print_report

extensions = scan()

print_report(extensions)
