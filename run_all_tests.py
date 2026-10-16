"""Run every solution's tests: python run_all_tests.py"""
import pathlib
import runpy

root = pathlib.Path(__file__).parent
files = sorted(root.glob("*/lc*.py"))
for path in files:
    runpy.run_path(str(path), run_name="__main__")
print(f"\n{len(files)} solution files passed.")
