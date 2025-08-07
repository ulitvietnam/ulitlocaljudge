import subprocess
import argparse

def load_compiler_paths(path="complierpath.txt"):
    compiler_paths = {}
    with open(path, "r") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                compiler_paths[key.strip()] = value.strip().replace("\\", "/")
    return compiler_paths

def scan_python(file_path, python_path):
    python_exec = f"{python_path}/python.exe"
    result = subprocess.run([python_exec, "-m", "py_compile", file_path],
                            capture_output=True, text=True)
    return result.stderr.strip()

def scan_cpp(file_path, gcc_path):
    gcc_exec = f"{gcc_path}/g++.exe"
    cmd = [gcc_exec, "-std=c++14", "-Wall", "-Wextra", "-Werror", "-fsyntax-only", file_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stderr.strip()

def main():
    parser = argparse.ArgumentParser(description="Scan source code for syntax errors.")
    parser.add_argument("language", choices=["python", "cpp"], help="Language of the source file.")
    parser.add_argument("file", help="Path to the source file.")
    parser.add_argument("--config", default="complierpath.txt", help="Path to compiler config file.")
    args = parser.parse_args()

    paths = load_compiler_paths(args.config)

    if args.language == "python":
        errors = scan_python(args.file, paths["python"])
    else:
        errors = scan_cpp(args.file, paths["gcc"])

    if errors:
        print("1")
        print(errors, end="")
    else:
        print("0", end="")

if __name__ == "__main__":
    main()
