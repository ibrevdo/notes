---
order: 3
---

## Movments

|   | Basic                    |
|---|--------------------------|
| h | move one character left  |
| j | move one row down        |
| k | move one row up          |
| l | move one character right |
| H | move to top of screen    |
| M | move to middle of screen |
| L | move to bottom of screen |


|     | Scroll                                                      |
|-----|-------------------------------------------------------------|
| zz  | scroll the line with the cursor to the center of the screen |
| zt  | scroll the line with the cursor to the top                  |
| zb  | scroll the line with the cursor to the bottom               |
| C-y | scroll up                                                   |
| C-e | scroll down                                                 |
| C-u | scroll half-page up                                         |
| C-d | scroll half-page down                                       |
| C-b | scroll page up                                              |
| C-f | scroll page down                                            |

* Some movements can be preceded by a count; e.g. 4j moves down 4 lines.

* note:  Any mnenomics to remember this? 
       efter (after in Swedish), yore (meaning the past), up, down, back, forward. 
       (The words back and forward are longer than up and down, 
       so naturally they move the screen a longer distance;)


|   | Words                                                  |
|---|--------------------------------------------------------|
| w | move to beginning of next word                         |
| b | move to beginning of previous word                     |
| e | move to end of word                                    |
| W | move to beginning of next word after a whitespace      |
| B | move to beginning of previous word before a whitespace |
| E | move to end of word before a whitespace                |


|         | Lines                                                           |
|---------|-----------------------------------------------------------------|
| f<char> | go forward to <char> inside line (after)                        |
| t<char> | go forward to <char> inside line (before)                       |
| ;       | repeat above, in same direction                                 |
| ,       | repeat above, in reverse direction                              |
| 0       | move to beginning of line                                       |
| $       | move to end of line                                             |
| _       | move to first non-blank character of the line                   |
| g\_     | move to last non-blank character of the line                    |
| gg      | move to first line                                              |
| S-g     | move to last line                                               |
| <n>gg   | move to n'th line of file (n is a number; 12G moves to line 12) |


|       | Searching                                                           |
|-------|---------------------------------------------------------------------|
| *     | find (and highlight) word under cursor (forward)                    |
| #     | find (and highlight) word under cursor (backwards)                  |
| g\*   | find (and highlight) word (not whole word) under cursor (forward)   |
| g#    | find (and highlight) word (not whole word) under cursor (backwards) |
| /text | find text (forward)                                                 |
| ?text | find text (backward)                                                |
| n     | next matching search pattern                                        |
| S-n   | previous matching search pattern                                    |


|         | Jumping                                     |
|---------|---------------------------------------------|
| ``      | last location inside of file                |
| '.      | last edit location inside of file           |
| C-o     | jump to last (older) cursor position        |
| C-i     | jump to next cursor position (after Ctrl-O) |
| :jumps  | print list of locations                     |
| ( )     | jump forward/backwards one sentence         |
| { }     | jump forward/backwards one paragraph        |
| %       | jump to matching bracket { } [ ] ( )        |
| `[[ ]]` | jump to next block of code                  |
| mx      | mark current position 'x'                   |
| 'x      | go to line of mark x                        |
| `x      | go to cursor position of mark x             |
| gf      | go to file under cursor                     |
| gd / gD | go to definition / go to global definition  |

|                      | Ctags                                                           |
|----------------------|-----------------------------------------------------------------|
| C-]                  | jump to definition according to tags                            |
| C-t                  | jump back                                                       |
| C-w C-]              | Open the definition in horizontal split                         |
| g C-]                | opens a quick dialog to select one between multiple definitions |
| :tag %%/^asserts_*%% | search for tags that start with %%asserts_%%                    |


|            | Help                           |
|------------|--------------------------------|
| :h <topic> |                                |
| C-]        | jump to tag                    |
| C-t        | jump back                      |
| K          | jump to man page of a function |
