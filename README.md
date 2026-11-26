# Lab 8 — Unvalidated Input Program (Exp 15)

Satyam | Roll No. 2301730306

Run `python unvalidated.py` from this folder. This intentionally insecure educational program accepts invalid age values and path traversal input.

Test 1: age `-10`, filename `demo.txt`: invalid age accepted.

Test 2: age `20`, filename `../private.txt`: reads data outside `records/`.

Run only in a local test folder with fictional data. Results are shown in `01_Lab8_Abuse_Cases.png`. See the PDF for the lab report.
