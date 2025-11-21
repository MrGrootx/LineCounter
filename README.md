# Line Counter for FiveM Scripts

Count lines of code in your FiveM resource projects (Lua and TSX/JSX files).

## How to Use

### Quick Start

1. **Drop these files in your FiveM script project folder:**
   - `count_lines.py`
   - `count_lines.bat`

2. **Double-click `count_lines.bat`** - it will count all Lua and TSX/JSX files in the current directory and subdirectories.

### Advanced Usage

**Count a specific directory:**
```
python count_lines.py "path/to/your/resource"
```

**Show top 10 largest files:**
```
python count_lines.py . --details
```

## What It Counts

- **Lua files** (`.lua` extension) - Your FiveM server/client scripts
- **TSX/JSX files** (`.tsx`, `.jsx` extensions) - Your NUI/web interface files

## Requirements

- Python 3.6 or higher (no additional packages needed)

## Example Output

```
Scanning directory: D:\...\g-bossmenu
------------------------------------------------------------

[1/2] Counting Lua files...
Counting... 64/64 files (100.0%)
      Found 64 Lua files

[2/2] Counting TSX/JSX files...
Counting... 81/81 files (100.0%)
      Found 81 TSX/JSX files

============================================================
LINE COUNT RESULTS
============================================================

[Lua Files]
   Files: 64
   Lines: 13,862

[TSX/JSX Files]
   Files: 81
   Lines: 13,742

[Total]
   Files: 145
   Lines: 27,604
============================================================
```
