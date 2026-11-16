"""Exact-token matching for numbers in prose, shared by the verify_* scripts.

Plain `needle in text` lets '4' match inside '40' and '6.00' inside '16.00',
so a wrong figure can pass if a different figure contains it."""
import re


def present(text, needle):
    """True if needle appears as a whole token: not glued to other digits or decimals."""
    return re.search(r"(?<![\d.,])" + re.escape(needle) + r"(?!\d|[.,]\d)", text) is not None
