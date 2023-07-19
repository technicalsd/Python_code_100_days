# Files just don't have name, but it does have paths

# There are two file paths
# 1. Absolute file paths
# 2. Relative file paths

# 1. Absolute file path
# with open(r"\Users\akash\OneDrive\Desktop\saurabh.txt") as file:
#     content = file.read()
#     print(content)


# 2. Relative file  path
with open("../../../Desktop/saurabh.txt") as file2:
    content = file2.read()
    print(content)
