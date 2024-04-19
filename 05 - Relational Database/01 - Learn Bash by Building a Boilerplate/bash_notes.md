
# Bash Command Guide

This document provides an overview of commonly used Bash commands along with their primary uses and examples.

## Basic Commands

### `echo`
Used to display a line of text/string that is passed as an argument.
```bash
echo "Hello, World!"
```

### `pwd`
Prints the current directory path.
```bash
pwd
```

### `cd`
Changes the directory. `cd ..` moves up one directory.
```bash
cd /path/to/directory  # Change to specific directory
cd ..                  # Go up one directory
cd                     # Go to the home directory
```

### `ls`
Lists all files and directories in the current directory.
```bash
ls
ls /path/to/directory  # List files in a specific directory
```

### `ls -a`
Lists all items in the current directory, including hidden files (those starting with `.`).
```bash
ls -a
```

### `ls -l`
Lists files with detailed information including permissions, number of links, owner, group, size, and time of last modification.
```bash
ls -l
```

### `mkdir`
Creates a new directory.
```bash
mkdir new_directory
mkdir -p path/to/new_directory  # Creates the path if it does not exist
```

### `touch`
Creates a new empty file.
```bash
touch new_file.txt
```

### `rm`
Removes files.
```bash
rm filename.txt
rm -f filename.txt  # Force deletion without prompting
rm -r directory     # Recursively remove a directory and its contents
```

### `rmdir`
Removes empty directories.
```bash
rmdir empty_directory
```

### `cp`
Copies files or directories.
```bash
cp source.txt destination.txt
cp -r source_directory destination_directory  # Recursively copy entire directories
```

### `mv`
Moves or renames files or directories.
```bash
mv old_name.txt new_name.txt
mv file.txt /path/to/directory/  # Move file to a new directory
```

### `find`
Searches for files in a directory hierarchy.
```bash
find /path/to/search -type f
find . -type d  # Find all directories in the current directory
```

### `find -name`
Searches for files by name in a directory hierarchy.
```bash
find /path/to/search -type f -name "pattern"
find . -type f -name "*.txt"  # Find all text files in the current directory
```

These commands form the foundation of navigating and manipulating the file system using the command line in Unix/Linux systems.
