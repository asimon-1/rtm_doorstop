import rtm_doorstop as rtm
import re

def test_one_test():
    out = rtm.rtm_builder("REQ")
    assert re.match(r"|\w*REQ0001\w*|\w*True\w*|\w*TST0001\w*|", out)

def test_no_tests():
    out = rtm.rtm_builder("REQ")
    assert re.match(r"|\w*REQ0002\w*|\w*False\w*|\w*|", out)

def test_multiple_tests():
    out = rtm.rtm_builder("REQ")
    assert re.match(r"|\w*REQ0003\w*|\w*True\w*|\w*TST0003 TST0004 TST0005\w*|", out)
