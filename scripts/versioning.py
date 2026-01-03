with open("VERSION", "r") as f:
    version = f.read().strip()

major, minor, patch = map(int, version.split("."))

patch += 1

new_version = f"{major}.{minor}.{patch}"

with open("VERSION", "w") as f:
    f.write(new_version)

print("New version:", new_version)
