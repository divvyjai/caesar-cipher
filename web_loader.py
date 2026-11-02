import ast, sys

name = "section1.py"   # change this per page: section1.py, section2.py, section3.py

src = open(name).read().replace("input(", "await input(")
code = compile(src, name, "exec", flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
await eval(code)