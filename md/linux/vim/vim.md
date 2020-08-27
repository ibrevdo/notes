# Vim 

---------------------------------
## Jumps
Jumps commands include: searches (and repetitions), substitutions, parenthesses jumping,
paragraphs and sentences, locations inside window, opening another file

* `(`/`)`   jump to prev/next sentence
* `{`/`}`   jump to prev/next paragraph
* `gg`/`G`  jump to start/end of file
* `H`/`M`/`L` jump to windows top/middle/bottom
* `%`       jump to matching parenthess (works with `(,[,{` )
* `C-i`     jump forward (in)
* `C-o`     jump back (out)
* `C-]`     jump to tag definition (works in help or with ctags)
* `:jumps`  see list of jumps
* `g;` `g,` go back/forward through list of changes (`:changes` see list of changes)

## Marks
**Auto marks**

```
``      last jump within current file
`.      last change within current file
`0      jump to position in last file edited (after exiting vim)
`[ `]   start/end of last changed or yanked text
`< `>   start/end of last visual selelction
```
**Local marks**

* `mm` put mark in current cursor
* `` `m `` jump to mark

**Global marks**
Global marks are saved between files

* `mM`      set global mark by m and capital letter
* `` `M ``  jump to global mark M

## Registers
The command that can use a register looks like this : `"{register}command`. 
For example, to a yank a current word into register 'a' run : `"ayiw` 

* `""`      unnamed (default) register. contains what was deleted/yanked
            Commands `x`,`s`,`c{motion}`,`d{motion}` all set content of this register
* `"0`      yank register. command `y{motion}` sets this register
* `"0p`     paste from yank register
* `:reg`    inspect registers
* `"a`      named register a
* `"/`      last search register
* `":`      last Ex command
* `"%`      name of current file
* `<C-r>"`   Copy text from register in insert mode/command prompt
* `"+y`     if clipboard enabled, puts visual selection from Vim into system clipboard
* `:put +`  if clipboard enabled, puts system clipboard into Vim

## Macros

* `qa`      Start recording macro into register a. Stop recroding with `q`. 
* `@a`      play macro stored in register a
* `@@`      repeat last executed macro
* `22@a`    execute macro on next 22 buffers (num of buffers can be less than 22)
* `:%norm! @a`  To repeat macro stored in register 'a', on whole file: 

## Completions

* `C-n`/`C-p`   keyword completion completion (next/previous) uses words from open buffers
* `C-x C-o`     tags(omni) completion
* `C-x C-f`     filename completion

## Folding

* `zi`          switch folding on/off
* `za`          toggle current fold open/close
* `zo`/`zc`     open/close current fold
* `zR`/`zC`     open/close all folds
* `zv`          expand folds to reveal cursor

----------------------------------
## Visual mode
* `o`   - move to other end of marked area
* `gv`  reselect last visual selection
* highlight text objects
    1. `vi}`    highlight inner {} block
    2. `va)`    highlight outer () block

## Windows

All window commands can be activated with `<C-w><C-<letter>>` or just `<C-w<letter>>`

* `C-ws`        split current window vertically 
* `:sp <file>`  split and load file into new window
* `:new`,`:vnew` split and open new buffer
* `C-ww`        jump to prevoius window
* `:clo` or `:q` close current window
* `C-w+` `C-w-`  enlarge/decrease current window
* `C-w_`        enlarge current window maximally
* `C-w=`        make all windows even g
* `C-wr`        rotate windows locations
* `C-wx`        exchange locations of two neighbor windows

## Arglist

* `:args`           show arglist
* populate args with shell command

```sh
    :args `find *.md`
```
* `:next`/`:prev`   traverse trough buffers inside arglsist
* `:first`/`:last`  jump to first/last buffer of arglist
* `:argdo %s/\a/*/ge` execute substitude command on every file in arglist
* `:argdo edit!`    undo last change in all buffers in arglist
* `:argdo update`    save changes in all buffers in arglist
* `:argdo normal @a` execute macro on every file in arg list

## Quickfix list

* `[q`,`:cprev`     show prev entry of quickfix list
* `]q`,`:cnext`     show next entry of quickfix list
* `[Q`,`:cfirst`    show first entry of quickfix list
* `]Q`,`:clast`     show last entry of quickfix list
* `:copen`,`:close` open/close quickfix list window

## Vimdiff

Open two windows with two buffers (each buffer may be unnamed)

* `:windo diffthis` start diff on two windows
* `:windo diffoff`  stop diff
* `[c`,`]c`     jump back and forward between changes
* `:diffget`,`:diffput` resolve differences between files

## Clipboard
* In order to copy to clipboard from vim hold "Shift" while selecting with mouse. Now paste qith middle button
* In order to paste form clipboard into vim use "shift+middle click" or "Shift+Insert"

--------------------------------
## Search, substitute and vim regex

Search with `/<expr>`, substitute with `range s/pattern/string/cgiIe`. \\
Where c-confirm, g-all occurances in range, i-ignore case, I-don't ignore case, e-don't show errors
It is possible to use any character instead of `/` as a separator.

* `\<`,`\>` Anchors for start and end of a word. Example: `/\<i\>` search for a word i
* `^`, `$`  Anchors for begining and end of a line. 
* `.`       any character except a new line
* `\s`,`\d`,`\w`,`\a` Space character, digit, word, alphabetic
* `\S`,`\D`,`\W`,`\A` Non-Space character, Non-digit, Non-word, Non-alphabetic
* `*`           matches 0 or more characters. `.*` matches everything.
* `\+`          matches 1 or more.
* `\=`          matches 0 or 1
* `{n}`,`{,m}`,`{n,}`,`{n,m}` matches exactly n, 0 to m, at least n, from n to m.
* `[012345]`    character range will match any of characters inside
* `[^A-Z]`      Negation sign `^` will match any character which is not in a range
* `\(`, `\)`     group part of pattern and refer to them inside replacement pattern by their
                number `\1`,`\2`,`\3`
* `\|`      Find this or that. The first match will be used. Not greedy. (so order is important)
* 
* Examples: 
* `:s//str/`    use a prevoius expression again
* `%s:^vi$:VIM:g` Substitute all lines in a file that contain vi to VIM.
* `/\.\s+[a-z]` Find all places where new sentence doesn't start with capital letter. 
                a period followed by one or more blanks and a lowercase letter
* `%s:\([.!?]\)\s\+\([a-z]\):\1  \u\2:g` Correct the prevoius example. 
                                         Insert two spaces exactly between sentences.
* `\(Date:\|Subject:\|From:\)\(\s.*\)`  Parse various mail headings and their contents into
                                        `\1` and `\2`.
* Useful mappings for substitutions

```sh
noremap ;; :%s:::gc<Left><Left><Left>
cmap    ;\ \(\)<Left><Left>
```

### Global command

`:range g!/patern/cmd` Execute the Ex command (default: `:p`) on the lines within range 
where pattern matches. (or, if `!` is used, only where match does not occure) \\
If range is not specified then operate on whole file

* `:g/^$/ d`    delete all empty lines in a file
* `:g/^$/,/./-j` reduce multiple blank lines to a single blank
* `:g/^Error/ . w >> errors.txt` Find all lines starting with error and append them to errors.txt
* `:g//cmd`     use previous expression again

### vimgrep

vimgrep - use it to search in small group of files (like a local project)

* `:vim[grep][!] /{pattern}/[g][j] {file} ...`  Full command (possible to use shell commands to populate files list. g-every match is added. j-dont jump on first match
* `:vim /expr/ %`       Search in current file
* `:vim /expr/ *`       Search in all files in current dir
* `:vim /expr/ *.cpp`   Search in multiple cpp files in current dir
* `:vim /expr/ **`      Search recursivly in all files
* `:vim /expr/ **/*.h`    Search recursivly in all header files
* `:vim /expr/ ##`      search inside files in arglist

search for all lines containing "dostuff()" in all .c files

* `:vim /dostuff()/j ../**/*.c`

search inside hidden files

* `:vimgrep /pattern/ ./.*`

### grep

grep - use on large amounts of files

* Search in all files in current dir : `:grep /expr/ *`
* Or search recursivly : `:grep -R /expr/ *`
* `:grep -R pattern *.c`
* `map <F3> :execute " grep -srnw --binary-files=without-match --exclude-dir=.git --exclude-from=exclude.list . -e " . expand("<cword>") . " " <bar> cwindow<CR>`
* you can fill file exclude.list with file patterns to exclude from search, such as "*~" – all files ending in a '~' character

"grep" and "vimgrep" fill the "quickfix list", which can be opened with :cw or :copen, and is a list shared between ALL windows.


-----------------------------------
## netrw commands
* `e .` go to file system view of current directory
* `o`   open file in a split
* `%`   create a new file

## General commands
* `C-l`     redraw screen
* `C-g`     Shows filename, current line number, total lines in file, and % of file location

## Command-line mode
* `C-b` begining of command line
* `C-e` end of command line
* `C-w` delete the word before cursor
* `C-u` delete everything between cursor and begining of line
* `q:` `C-f` open buffer of command line
* `q/`/`q?` open cmdline for search/backward
* `C-c` exit the window
* `@:`  repeate last Ex command

----------------------------------

## Useful settings

* set completeopt=menuone,noinsert
* set autoindent
* set ft=xml
* set relativenumber

---------------------------------
## Tips

* `gn`  go to next search result and visual highlight it
* switch between two chars: cursor on the first one, and then `xp`
* switch between two lines: cursor of first one, and then `ddp`
* `:9t.`    copy line 9 to cursor position
* `:so %`   treat temp file as vimrc, source it so configuration become active
* Switch between .c and .h file

```sh
    map <F4> :e %:p:s,.h$,.X123X,:s,.cpp$,.h,:s,.X123X$,.cpp,<CR>`
```

* Put output of shell command in buffer 
`:%!ls`

* Comment multiple lines
    1. C-v to select the lines
    2. Use substitute expression `:s/^/#/`
    3. to uncomment: `:s/^#//`

* Delete blank lines
    * `g/^$/d`
    * `:g`  will execute a command on lines which match a regex. 
            The regex is 'blank line' and the command is `:d` (delete)

* Delete all buffers
    * `:%bd|e#` %bd = delete all buffers. e# = open the last buffer for editing.
    * `command! BufOnly silent! execute "%bd|e#|bd#"`
* Save file as a root
    * `w !sudo tee % > /dev/null`   put a content of current buffer into `%` (current file) using sudo
* Find and replace in project wide
    1. Put all files of the project in arglist `:args *.cpp`
    2. Find all reqiured changes in the project `:vimgrep /expr/g ##`
    3. Qargs command puts all files from quicklist into arglist
    4. Substitude in all files `argdo %s/expr/str/ge`
    5. Save all files `:argdo w`
