import sys
import subprocess
import os

def read_config(file_path):
    config = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key.strip()] = value.strip()
    return config

def get_language(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.py':
        return 'python'
    elif ext == '.cpp':
        return 'cpp'
    else:
        raise ValueError(f"-1")

def compile_file(file_path):
    language = get_language(file_path)
    args_config = read_config('complieagruments.txt')
    path_config = read_config('complierpath.txt')
    compile_args = args_config.get(language, '')
    compiler_path = path_config.get('gcc' if language == 'cpp' else language, '')
    build_dir = os.path.join('build', os.path.dirname(file_path))
    os.makedirs(build_dir, exist_ok=True)
    filename = os.path.basename(file_path)
    build_path = os.path.join(build_dir, filename)
    if language == 'python':
        import shutil
        shutil.copy(file_path, build_path)
        cmd = [os.path.join(compiler_path, 'python'), build_path]
    elif language == 'cpp':
        output_file = os.path.splitext(filename)[0] + '.exe'
        output_path = os.path.join(build_dir, output_file)
        cmd = [os.path.join(compiler_path, 'g++')] + compile_args.split() + [file_path, '-o', output_path]
    else:
        raise ValueError("1")
    subprocess.run(cmd, check=True)
    print(0, end="")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("-1", end="")
        sys.exit(1)

    source_file = sys.argv[1]
    compile_file(source_file)
