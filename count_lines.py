#!/usr/bin/env python3

import os
import sys
from pathlib import Path


def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            return len(f.readlines())
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return 0


def count_lines_by_extension(directory, extensions, show_progress=True):
    total_lines = 0
    file_count = 0
    files_list = []
    
    directory_path = Path(directory)
    
    all_files = []
    for ext in extensions:
        for file_path in directory_path.rglob(f'*.{ext}'):
            if any(skip_dir in str(file_path) for skip_dir in ['node_modules', '.git', 'build', 'dist']):
                continue
            all_files.append(file_path)
    
    total_files = len(all_files)
    for idx, file_path in enumerate(all_files, 1):
        if show_progress and total_files > 0:
            if total_files < 50 or idx % 10 == 0 or idx == total_files:
                progress = (idx / total_files) * 100
                print(f"\rCounting... {idx}/{total_files} files ({progress:.1f}%)", end='', flush=True)
        
        lines = count_lines_in_file(file_path)
        total_lines += lines
        file_count += 1
        files_list.append((str(file_path.relative_to(directory_path)), lines))
    
    if show_progress and total_files > 0:
        print()
    
    return total_lines, file_count, files_list


def main():
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        target_directory = os.getcwd()
    
    if not os.path.isdir(target_directory):
        print(f"Error: Directory '{target_directory}' does not exist.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Scanning directory: {target_directory}")
    print("-" * 60)
    print()
    
    print("[1/2] Counting Lua files...")
    lua_lines, lua_files, lua_list = count_lines_by_extension(target_directory, ['lua'])
    print(f"      Found {lua_files} Lua files")
    print()
    
    print("[2/2] Counting TSX/JSX files...")
    tsx_lines, tsx_files, tsx_list = count_lines_by_extension(target_directory, ['tsx', 'jsx'])
    print(f"      Found {tsx_files} TSX/JSX files")
    print()
    
    print("\n" + "=" * 60)
    print("LINE COUNT RESULTS")
    print("=" * 60)
    print(f"\n[Lua Files]")
    print(f"   Files: {lua_files}")
    print(f"   Lines: {lua_lines:,}")
    
    print(f"\n[TSX/JSX Files]")
    print(f"   Files: {tsx_files}")
    print(f"   Lines: {tsx_lines:,}")
    
    print(f"\n[Total]")
    print(f"   Files: {lua_files + tsx_files}")
    print(f"   Lines: {lua_lines + tsx_lines:,}")
    print("=" * 60)
    
    if len(sys.argv) > 2 and sys.argv[2] == '--details':
        print("\n[Top 10 Largest Lua Files]")
        sorted_lua = sorted(lua_list, key=lambda x: x[1], reverse=True)[:10]
        for file_path, lines in sorted_lua:
            print(f"   {lines:>6,} lines - {file_path}")
        
        print("\n[Top 10 Largest TSX/JSX Files]")
        sorted_tsx = sorted(tsx_list, key=lambda x: x[1], reverse=True)[:10]
        for file_path, lines in sorted_tsx:
            print(f"   {lines:>6,} lines - {file_path}")


if __name__ == "__main__":
    main()

