#!/bin/python3

def get_data() -> list:
    """
        Return: List of each lines reads from inputs
    """
    #with open("dummy.txt", "r") as f:
    with open("data.txt", "r") as f:
        return [line[:-1] for line in f]

def is_report_safe(mreport):
    diffs = [b - a for a, b in zip(mreport, mreport[1:])]
    if any(abs(diff) < 1 or abs(diff) > 3 for diff in diffs):
        return False
    return all(
        (curr > 0) == (prev > 0) and curr != 0
        for prev, curr in zip(diffs, diffs[1:])
    )

def my_safe(ds): 
    for sense in [1, -1]:
        for i in range(len(ds) - 1): 
            if 1 <= sense * (ds[i] - ds[i + 1]) <= 3 :
                i += 1
                continue
            break
        else:
            break
    else:
        return False
    return True

good_res = 0
for ds in get_data():
    ds = list(map(int, ds.split(" ")))
    t_res = any(is_report_safe(ds[:i] + ds[i+1:]) for i in range(len(ds)))
    m_res = any(my_safe(ds[:i] + ds[i+1:]) for i in range(len(ds))) # + ds[i+1:]) for i in range(len(ds)))
    if m_res != t_res:
        print(f"error for {ds}, {m_res=}, {t_res=} ")
    good_res += m_res 

print(good_res)
