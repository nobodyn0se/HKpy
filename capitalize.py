

# Complete the solve function below.
def solve(s):
    for a in s[:].split():
        s = s.replace(a,a.capitalize())
    return s

