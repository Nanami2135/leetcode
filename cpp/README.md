# LeetCode C++

This workspace treats every file in `problems/` as one standalone LeetCode
program. The filename is the problem id, and CMake creates one executable with
the same name.

```text
cpp/
  CMakeLists.txt
  Makefile
  problems/
    103.cpp
    547.cpp
```

## Commands

```sh
make build
make run PROBLEM=103
make list
make clean
make distclean
```

## Adding a Problem

Create a new file named after the LeetCode problem id:

```text
problems/1.cpp
```

Keep each problem self-contained:

- include the LeetCode `Solution` class in the file
- add a small `main()` with local sample cases when useful
- avoid shared helpers until there is real duplication across problems

After adding the file, run it with:

```sh
make run PROBLEM=1
```
