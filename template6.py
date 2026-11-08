"""
RECORD CHECK  -  my version
===========================

Name  : Abdullahi hussen ousman
Lane  :  Cyber secuirity
Date  : november 5th 2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit (or your lane's own field
#    names - same shape, different words).

df = pd.read_csv("login_attempts.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#
#    Typical and above: also add a "status" column using .apply() with a
#    lambda - "OVER LIMIT" (100%+), "WARNING" (90%+), otherwise "OK".

# my csv uses attempts and failed, so percent = failed out of attempts
df["percent"] = (df["failed"] / df["attempts"]) * 100

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK", using a
#                boolean condition in [] - not a loop.
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV with .to_csv(), and save
#                one bar chart of the counts per status.

print(df)

# rows that are not OK
print(df[df["status"] != "OK"])

# count per status
counts = df.groupby("status").size()
print(counts)

# save the full table
df.to_csv("record_check_output.csv", index=False)

# bar chart of the counts
counts = counts.reindex(["OK", "WARNING", "OVER LIMIT"], fill_value=0)
plt.bar(counts.index, counts.values, color=["green", "orange", "red"])
plt.title("Services per status")
plt.ylabel("Number of services")
plt.savefig("status_counts.png")


# ==========================================================================
# 4. Before you finish:
#    [ ] Run it and check the percent/status columns by hand for one row
#    [ ] Check you used & (not "and") if you combined more than one condition
#    [ ] Check every column your code refers to actually exists - watch case