---
order: 4
---

## Editing

|         | Delete                      |
|---------|-----------------------------|
| x       | delete char under cursor    |
| dd      | delete line                 |
| S-d     | delete till end of line     |
| d<move> | delete till end of movement |

|     | Examples                         |
|-----|----------------------------------|
| dw  | delete world                     |
| d$  | delete till end of line          |
| df> | delete till word ending with '>' |
| diw | delete word under cursor         |


|         | Copying text          |
|---------|-----------------------|
| yy      | copy line             |
| y<move> | copy till end of move |


|         | Change text - delete text and enter editing mode |
|---------|--------------------------------------------------|
| s       | delete one character and stay in editing mode    |
| cc      | change current line                              |
| S-c     | change till end of line                          |
| ciw     | change word under cursor                         |
| c<move> | change till end of move                          |


|     | Insert text                          |
|-----|--------------------------------------|
| i   | inserts before cursor                |
| a   | inserts after cursor                 |
| S-i | inserts at start of current line     |
| S-a | insets after end of current line     |
| o   | inserts new line after current line  |
| S-o | inserts new line before current line |

|                  | Insert mode                   |
|------------------|-------------------------------|
| C-w              | erase work backwards          |
| C-u              | erase line backwards          |
| S-<middle click> | paste from clipboard into vim |


|         | Text completion                                                       |
|---------|-----------------------------------------------------------------------|
| C-n     | next word proposal (from file)                                        |
| C-p     | previous word proposal (from file)                                    |
| note    | these keys are also used to navigate on the opned menu of completions |
| C-x C-o | omni-completion (Intellisense)                                        |
| C-x C-l | line completion                                                       |
| C-x C-k | dictionary completion                                                 |
| C-x C-f | filenames completion                                                  |


|     | misc                                          |
|-----|-----------------------------------------------|
| p   | paste yanked text                             |
| ]p  | paste yanked text and adjust the indent level |
| .   | repeat last editing                           |
| u   | undo                                          |
| tr  | transpose two characters                      |
| S-j | join lines                                    |


| indent    |                                           |
|-----------|-------------------------------------------|
| >>        | indent line forward                       |
| <<        | indent line backwards                     |
| ##        | auto indent current line                  |
| >%        | indent curly-braces block (put your cursor on one of the curly braces) |


| Search and replace |                                                  |
|-----------|-----------------------------------------------------------|
| :%s/old/new/g | replace old with new inside a file                    |
| :%s/old/new/gc | replace old with new inside a file with conformations|


| Visual mode |                                         |
|-----------|-------------------------------------------|
| v         | start visual mode                         |
| S-v       | visual line mode                          |
| C-v       | select columns                            |
| y         | yank highlighted area                     |
| d         | kill highlighted area                     |
| >         | shift right                               |
| <         | shift left                                |
| ~         | switch case                               |
| o         | move to opposite of highlighted area      |
| aw        |   mark a word                             |
| ab        | mark a () block                           |
| aB        | mark a {}  block                          |
| Esc       | exit visual mode                          |


