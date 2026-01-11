// Simple dungeon pickup game using rlutil.h
// Player: @, Chest: $, Wall: #. Pick all chests to win.

#include "rlutil.h"
#include <vector>
#include <string>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>

using namespace std;
using namespace rlutil;

int main() {
    srand((unsigned)time(nullptr));
    // Multi-level random maze generator parameters
    const int LEVELS = 10;
    const int MAX_ROWS = 21; // recommended maximum (odd)
    const int MAX_COLS = 41; // recommended maximum (odd)

    // Helper: carve a perfect maze using randomized DFS on odd coordinates
    // generate_level now accepts desired rows/cols so we can fit smaller terminals
    auto generate_level = [&](int level, int mrows, int mcols)->pair<vector<string>, pair<int,int>> {
        // ensure odd dimensions >= 7
        if (mrows < 7) mrows = 7;
        if (mcols < 11) mcols = 11;
        if (mrows % 2 == 0) --mrows;
        if (mcols % 2 == 0) --mcols;

        // initialize full walls
        vector<string> m(mrows, string(mcols, '#'));

        // mark cell positions (odd coords) as passages
        for (int y = 1; y < mrows-1; y += 2) {
            for (int x = 1; x < mcols-1; x += 2) {
                m[y][x] = ' ';
            }
        }

        int cellRows = (mrows-1)/2;
        int cellCols = (mcols-1)/2;
        vector<char> vis(cellRows * cellCols, 0);
        auto idx = [&](int cy, int cx){ return cy * cellCols + cx; };

        // stack for DFS
        vector<pair<int,int>> stack;
        int scy = 0, scx = 0; // start cell
        vis[idx(scy,scx)] = 1;
        stack.emplace_back(scy, scx);
        while (!stack.empty()) {
            auto [cy, cx] = stack.back();
            vector<int> dirs = {0,1,2,3}; // up,right,down,left
            random_shuffle(dirs.begin(), dirs.end());
            bool moved = false;
            for (int d : dirs) {
                int ncy = cy + (d==0?-1: d==2?1:0);
                int ncx = cx + (d==3?-1: d==1?1:0);
                if (ncy < 0 || ncy >= cellRows || ncx < 0 || ncx >= cellCols) continue;
                if (vis[idx(ncy,ncx)]) continue;
                // knock down wall between cells
                int wallY = 1 + cy*2 + (ncy-cy);
                int wallX = 1 + cx*2 + (ncx-cx);
                m[wallY][wallX] = ' ';
                vis[idx(ncy,ncx)] = 1;
                stack.emplace_back(ncy, ncx);
                moved = true;
                break;
            }
            if (!moved) stack.pop_back();
        }

        // Add some extra openings to reduce linearity (more openings at higher levels)
        int extra = 3 + level; // increases with level
        for (int i = 0; i < extra; ++i) {
            int ry = 1 + (rand() % (mrows-2));
            int rx = 1 + (rand() % (mcols-2));
            if (m[ry][rx] == '#') m[ry][rx] = ' ';
        }

        // place chests: fixed count per level
        int chestCount = 5; // fixed 5 chests per level
        int placed = 0;
        int attempts = 0;
        while (placed < chestCount && attempts < chestCount * 50) {
            ++attempts;
            int ry = 1 + (rand() % (mrows-2));
            int rx = 1 + (rand() % (mcols-2));
            if (m[ry][rx] == ' ') {
                m[ry][rx] = '$';
                ++placed;
            }
        }

        // pick a good player start: prefer a floor cell with at least one adjacent floor
        int px = -1, py = -1;
        for (int y = 1; y < mrows-1 && px == -1; ++y) {
            for (int x = 1; x < mcols-1; ++x) {
                if (m[y][x] != ' ') continue;
                if (m[y-1][x] == ' ' || m[y+1][x] == ' ' || m[y][x-1] == ' ' || m[y][x+1] == ' ') {
                    px = x + 1; // return 1-based coords for console
                    py = y + 1;
                    break;
                }
            }
        }
        // fallback: any floor
        if (px == -1) {
            for (int y = 1; y < mrows-1 && px == -1; ++y) {
                for (int x = 1; x < mcols-1; ++x) {
                    if (m[y][x] == ' ') {
                        px = x + 1; py = y + 1; break;
                    }
                }
            }
        }
        // last resort: force (1,1)
        if (px == -1) { px = 1; py = 1; if (m[1][1] == '#') m[1][1] = ' '; }

        return {m, {px, py}};
    };

    int currentLevel = 1;
    int totalLevels = LEVELS;
    char playerChar = '@';
    int playerColor = WHITE;

    saveDefaultColor();
    hidecursor();
    cls();

    // Start menu
    while (true) {
        cls();
        locate(1, 1);
        setColor(LIGHTCYAN);
        cout << "===== DUNGEON ADVENTURE =====";
        resetColor();
        locate(1, 3);
        cout << "Press [S] to Start";
        locate(1, 4);
        cout << "Press [C] to Choose Character";
        locate(1, 5);
        cout << "Press [Esc] to Quit";
        cout.flush();
        int k = getkey();
        if (k == 's' || k == 'S') {
            break;
        } else if (k == 'c' || k == 'C') {
            // Character selection menu
            bool selecting = true;
            while (selecting) {
                cls();
                locate(1, 1);
                setColor(LIGHTCYAN);
                cout << "===== CHARACTER SELECTION =====";
                resetColor();
                locate(1, 3);
                setColor(WHITE); cout << "1. @"; resetColor(); cout << " (Brave)";
                locate(1, 4);
                setColor(YELLOW); cout << "2. @"; resetColor(); cout << " (Rogue)";
                locate(1, 5);
                setColor(LIGHTGREEN); cout << "3. @"; resetColor(); cout << " (Ranger)";
                locate(1, 6);
                setColor(LIGHTCYAN); cout << "4. @"; resetColor(); cout << " (Mage)";
                locate(1, 7);
                cout << "Press Esc to back";
                cout.flush();
                int ck = getkey();
                if (ck == '1') {
                    playerChar = '@'; playerColor = WHITE; selecting = false;
                } else if (ck == '2') {
                    playerChar = '@'; playerColor = YELLOW; selecting = false;
                } else if (ck == '3') {
                    playerChar = '@'; playerColor = LIGHTGREEN; selecting = false;
                } else if (ck == '4') {
                    playerChar = '@'; playerColor = LIGHTCYAN; selecting = false;
                } else if (ck == KEY_ESCAPE) {
                    selecting = false;
                }
            }
        } else if (k == KEY_ESCAPE) {
            showcursor();
            resetColor();
            cls();
            return 0;
        }
    }

    bool quitAll = false;
    for (currentLevel = 1; currentLevel <= totalLevels && !quitAll; ++currentLevel) {
        // determine usable terminal area and generate map to fit
        int termCols = tcols();
        int termRows = trows();
        int usableCols = min(MAX_COLS, termCols);
        int usableRows = min(MAX_ROWS, termRows - 4); // leave room for HUD/messages

        if (usableCols < 11 || usableRows < 7) {
            // terminal very small: prompt user to resize or quit
            cls();
            locate(1,1);
            cout << "Terminal too small. Need at least 11x7 for auto-fit, or resize bigger.";
            cout << " Current " << termCols << "x" << termRows << ". Press any key after resize, or Esc to quit.";
            cout.flush();
            int k = getkey();
            if (k == KEY_ESCAPE) { quitAll = true; break; }
            --currentLevel; // retry same level
            continue;
        }

        // make odd sizes
        if (usableCols % 2 == 0) --usableCols;
        if (usableRows % 2 == 0) --usableRows;

        auto lvl = generate_level(currentLevel, usableRows, usableCols);
        vector<string> map = lvl.first;
        int playerX = lvl.second.first;
        int playerY = lvl.second.second;

        // count chests
        int totalChests = 0;
        for (int y = 0; y < (int)map.size(); ++y) for (int x = 0; x < (int)map[0].size(); ++x) if (map[y][x] == '$') ++totalChests;
        int collected = 0;

        // draw initial map and HUD
        auto draw_level = [&]() {
            int mrows = (int)map.size();
            int mcols = (int)map[0].size();
            for (int y = 0; y < mrows; ++y) {
                for (int x = 0; x < mcols; ++x) {
                    locate(x+1, y+1);
                    char c = map[y][x];
                    if (c == '#') { setColor(BROWN); cout << '#'; resetColor(); }
                    else if (c == '$') { setColor(YELLOW); cout << '$'; resetColor(); }
                    else cout << c;
                }
            }
            // draw player
            locate(playerX, playerY);
            setColor(playerColor); cout << playerChar; resetColor();
            // HUD
            int mrows_off = (int)map.size();
            locate(1, mrows_off+1);
            cout << "Level " << currentLevel << "/" << totalLevels << "  ";
            cout << "Chests: " << collected << " / " << totalChests << "    ";
            cout.flush();
        };

        // draw level
        draw_level();

        bool levelDone = false;
        while (!levelDone) {
            int k = getkey();
            int nx = playerX, ny = playerY;
            if (k == KEY_UP) ny -= 1;
            else if (k == KEY_DOWN) ny += 1;
            else if (k == KEY_LEFT) nx -= 1;
            else if (k == KEY_RIGHT) nx += 1;
            else if (k == KEY_ESCAPE) { quitAll = true; break; }

            // bounds check using actual map size
            int mrows = (int)map.size();
            int mcols = (int)map[0].size();
            if (nx < 1) nx = 1; if (nx > mcols) nx = mcols;
            if (ny < 1) ny = 1; if (ny > mrows) ny = mrows;

            char dest = map[ny-1][nx-1];
            if (dest != '#') {
                // restore the tile at the old player position
                int oldX = playerX, oldY = playerY;
                locate(oldX, oldY);
                char under = map[oldY-1][oldX-1];
                if (under == '#') { setColor(BROWN); cout << '#'; resetColor(); }
                else if (under == '$') { setColor(YELLOW); cout << '$'; resetColor(); }
                else cout << under;

                playerX = nx; playerY = ny;
                if (dest == '$') {
                    ++collected;
                    map[ny-1][nx-1] = ' ';
                }
                // draw player at new pos
                locate(playerX, playerY);
                setColor(playerColor); cout << playerChar; resetColor();
                // update chest HUD
                int mrows_off = (int)map.size();
                locate(1, mrows_off+1);
                cout << "Level " << currentLevel << "/" << totalLevels << "  ";
                cout << "Chests: " << collected << " / " << totalChests << "    ";
                cout.flush();
            }

            if (collected >= totalChests) {
                // Level complete
                int mrows_off = (int)map.size();
                locate(1, mrows_off+2);
                setColor(LIGHTCYAN);
                cout << "You cleared level " << currentLevel << "! Press any key to continue.";
                resetColor();
                cout.flush();
                anykey();
                levelDone = true;
            }
        }
        if (quitAll) break;
        cls();
    }

    // Final outcome
    cls();
    if (!quitAll) {
        locate(1,1);
        setColor(LIGHTCYAN);
        cout << "Congratulations! You finished all " << totalLevels << " levels.";
        resetColor();
        anykey();
    }

    showcursor();
    resetColor();
    cls();
    locate(1,1);
    return 0;
}
