import itertools
def truth_table(expr, vars):
    print(" | ".join(vars) + " | Result")
    for values in itertools.product([False, True, ], repeat=len(vars)):
        env = dict(zip(vars, values))
        res = eval(expr, env)
        row = " | ".join(['T' if v else 'F' for v in values])
        print(row + " | " + ('T' if res else 'F'))
truth_table("not p or q and r", ["p","q","r"])