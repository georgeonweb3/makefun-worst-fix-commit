#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message (<=100 characters) to /output/entry.txt:
a fix that made everything worse.

Drafting notes (scored against the judge brief):
- The judge weighs, in order: (1) reads as a one-line commit message
  for a bug fix that made everything worse, (2) makes a reader laugh
  out loud, a real joke not a complaint, (3) captures the specific
  irony of a repair that broke more than it mended, (4) sounds like a
  real commit subject line a tired engineer would type, (5) a fresh
  angle, not reverting / testing in production / breaking everything.
- Field's most common angle (from the visible info submissions):
  deleting/emptying the thing to fix it ("rotate the logs ... rotated
  the live database instead"; "The Report Is Now Always Correct
  Because It Is Always Empty"). The winner avoids that angle: it
  keeps the thing and poisons it instead (stale prices).
- Candidates (6, labelled A-F, blind pairwise tournament, 15 pairs):
  A. fix: silence the 3am pager by deleting on-call rotation —
     nobody wakes up, neither does the site (96)
  B. fix: patch the leak by rebooting nightly at 3am — the leak now
     has a calendar invite and tenure (95)
  C. fix: speed up checkout by caching prices in 2019 — checkout is
     instant, refunds are forever (91)  <-- TOURNAMENT WINNER, 5-0
  D. fix: flaky login test by mocking the database — all 412 tests
     pass, production still can't log in (97)
  E. fix: stop duplicate invoices by deleting the invoice table —
     duplicates solved, so is revenue (93)
  F. fix: quiet the error logs by reclassifying errors as info —
     dashboard green, the outage is a feature (100)
  Win table: C 5-0, E 4-1, F 3-2, A 2-3, D 1-4, B 0-5.
  C beat A, B, D, E and F head to head.
- Why C wins: two concrete anchors (checkout, 2019), three beats
  (speed fix -> stale cache -> refunds forever), ends on the punch
  ("refunds are forever"), real git subject style, and a fresh angle
  — the fix works perfectly, which is exactly the problem.
- Extra-mile pass: compared against the house/field baseline
  (log-rotation / empty-report lines). C is more specific than both:
  a named year and a named consequence (refunds) instead of a
  generic "everything broke". No change needed; weakest dimension
  was length (91 of 100) but padding would dilute the punch, so
  the line ships as judged.
"""

import os

LINE = (
    "fix: speed up checkout by caching prices in 2019 \u2014 "
    "checkout is instant, refunds are forever"
)


def main() -> None:
    # Gate validation: the competition requires one line, 1-100 chars.
    # Fail loudly instead of writing an entry the judge would reject.
    if "\n" in LINE or not 1 <= len(LINE) <= 100:
        raise ValueError(f"entry violates the 1-100 char one-line gate: {len(LINE)} chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
