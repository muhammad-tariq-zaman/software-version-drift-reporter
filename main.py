"""Report hosts running a version different from the baseline.

Usage: python3 main.py installed.csv baseline.csv
installed.csv columns: host,software,version.
baseline.csv columns: software,baseline_version.
DRIFT rows list host, software, installed and baseline version.
"""
import argparse, csv, sys

def drift(installed, baseline):
    base = {r["software"].strip(): r["baseline_version"].strip() for r in baseline}
    out = []
    for row in installed:
        software = row["software"].strip()
        if software in base and row["version"].strip() != base[software]:
            out.append((row["host"], software, row["version"].strip(), base[software]))
    return sorted(out)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("installed")
    parser.add_argument("baseline")
    args = parser.parse_args(argv)
    with open(args.installed, newline="", encoding="utf-8") as f:
        installed = list(csv.DictReader(f))
    with open(args.baseline, newline="", encoding="utf-8") as f:
        baseline = list(csv.DictReader(f))
    result = drift(installed, baseline)
    for host, software, version, wanted in result:
        print(f"DRIFT {host} {software}: {version} (baseline {wanted})")
    print(f"{len(result)} drifted install(s).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
