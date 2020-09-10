"""Provide functional tests for rtm_doorstop."""
import rtm_doorstop as rtm
import re
from subprocess import call
import csv


def test_one_test():
    """Check that requirements with one test are recorded correctly."""
    returnval = rtm.rtm_builder("REQ", root="tests")
    assert re.match(r"|\w*REQ0001\w*|\w*True\w*|\w*TST0001\w*|", returnval)


def test_no_tests():
    """Check that requirements with no tests are recorded correctly."""
    returnval = rtm.rtm_builder("REQ", root="tests")
    assert re.match(r"|\w*REQ0002\w*|\w*False\w*|\w*|", returnval)


def test_multiple_tests():
    """Check that requirements with multiple tests are recorded correctly."""
    returnval = rtm.rtm_builder("REQ", root="tests")
    assert re.match(
        r"|\w*REQ0003\w*|\w*True\w*|\w*TST0003 TST0004 TST0005\w*|", returnval
    )


def test_cli(capfd):
    """Confirm that the program can be run from the CLI."""
    returnval = call("python rtm_doorstop.py REQ --root=tests", shell=False)
    out, err = capfd.readouterr()
    assert returnval == 0
    assert "UID" in out


def test_csv_writer(tmpdir):
    """Confirm that the results are written to CSV."""
    path = tmpdir.join("outfile.csv")

    returnval = rtm.rtm_builder("REQ", root="tests", csv_path=path)
    assert returnval == f"Successfully wrote traceability matrix to {path}"
    with open(path, newline="") as csvfile:
        csvcontents = []
        reader = csv.DictReader(csvfile)
        csvcontents = [row for row in reader]
    assert csvcontents == [
        {"UID": "REQ0001", "Has Test": "True", "Need Test": "True", "Tests": "TST0001"},
        {"UID": "REQ0002", "Has Test": "False", "Need Test": "False", "Tests": ""},
        {
            "UID": "REQ0003",
            "Has Test": "True",
            "Need Test": "True",
            "Tests": "TST0003 TST0004 TST0005",
        },
    ]
