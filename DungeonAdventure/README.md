Dungeon pickup - minimal demo using rlutil.h

Build (MinGW / g++ on Windows):

```bash
g++ main.cpp -o dungeon -std=c++11
./dungeon
```

Or with MSVC (Developer Command Prompt):

```powershell
cl /EHsc main.cpp
main.exe
```

Controls:
- Arrow keys to move
- Esc to quit

Goal: pick up all `$` chests. Player is `@`, walls are `#`.

This version supports 10 randomly generated solvable levels (maze-like). Each level places several `$` chests; clear all to advance.

Files:
- `main.cpp` - game source
- `rlutil.h` - console helper (already present)

Next: the user can ask to add enemies, doors, or more levels.
