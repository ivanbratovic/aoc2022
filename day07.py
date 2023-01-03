import sys
import subprocess

test = False

def read_input():
    global test
    filename = "inputs/day07-input.txt"
    if test:
        filename = "inputs/day07-test.txt"
    with open(filename, "r") as file:
        return list(map(lambda x: x.strip(), file.readlines()))

def main():
    lines = read_input()
    script = ["MAIN_DIR=$(pwd)", "mkdir root"]
    for line in lines:
        match line.split():
            case ["$", "cd", d]:
                script.append(f"cd {d}")
            case ["$", "ls"]:
                continue
            case ["dir", d]:
                script.append(f"mkdir {d}")
            case other:
                size, filename = tuple(other)
                script.append(f"fallocate --length {size} {filename}")
    script.append("cd $MAIN_DIR")
    with open("create_files.sh", "w+") as file:
        for line in script:
            file.write(f"{line}\n")
    subprocess.run(["/bin/bash", "./create_files.sh"])
    out = subprocess.check_output("find root -mindepth 1 -type f -exec du -bs {} +".split()).decode().split()
    subprocess.run(["/usr/bin/rm", "-rf", "./root"])
    subprocess.run(["/usr/bin/rm", "-rf", "./create_files.sh"])
    dir_sizes = {}
    for i in range(0, len(out), 2):
        size = int(out[i])
        path = out[i+1]
        exact_dir = ""
        for subdir in path.split("/")[:-1]:
            exact_dir += subdir
            dir_sizes.setdefault(exact_dir, 0)
            dir_sizes[exact_dir] += size
            exact_dir += "/"

    
    print(sum([size for size in dir_sizes.values() if size <= 100000]))

    need_to_delete = dir_sizes["root"] - 40000000

    print(min([size for size in dir_sizes.values() if size >= need_to_delete]))


if __name__ == "__main__":
    main()