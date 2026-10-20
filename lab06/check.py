from solution import count_by_extension, deepest_path, human_size

print(count_by_extension(["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]))
print(count_by_extension(["archive.tar.gz", ".gitignore"]))
print(deepest_path(["x/y/z.txt", "a/b/c.txt"]))
print(human_size(1536))
print(human_size(0))