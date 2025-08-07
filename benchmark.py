import subprocess

def run_benchmark(exe_path):
    result = subprocess.run([exe_path, "1"], capture_output=True, text=True)
    return result.stdout.strip()

cpp_result = run_benchmark("benchmark\\benchmark_CPP.exe")

py_result = run_benchmark("benchmark\\benchmark_PY.exe")

print(f"cpp={cpp_result}")
print(f"python={py_result}", end="")