def line_format(x, y):
    print(f"""\t{x} \t{y}""")


line_format("NOT", "True?")
line_format("not False", "True")
line_format("not True", "False")

t = True
f = False


def Or_Table(t, f):
    print(f"""
    OR           \tTrue?\n
    {t} or {f} \t{t}
    {t} or {t} \t{t}
    {f} or {t} \t{t}
    {f} or {f} \t{f}
    """)


def And_Table(t, f):
    print(f"""
    AND         \tTrue?\n
    {t} and {f} \t{f}
    {t} and {t} \t{t}
    {f} and {t} \t{f}
    {f} and {f} \t{f}
    """)


Or_Table(t, f)
And_Table(t, f)
