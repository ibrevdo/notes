---
order: 5
---

## Multiple files


|              | Command mode                                 |
|--------------|----------------------------------------------|
| ":p          | copy text from command line into file buffer |
| :pwd         | current directory                            |
| :cd          | change current directory                     |
| :cd %:p:h    | change current directory to file's directory |
| :Sex         | file explorer                                |
| :!<command>  | execute shell command                        |
| :so $MYVIMRC | source (reload) .vimrc file                  |

|                  | Buffers                                          |
|------------------|--------------------------------------------------|
| %                | current buffer                                   |
| #                | alternate buffer                                 |
| :ls              | list buffers (% - current buffer, # - alternate) |
| :b# or C-6       | go to alternate buffer                           |
| :bn :bp          | go to next/previous buffer                       |
| :b <name>        | load buffer by name                              |
| :bd              | delete buffer (close file)                       |
| :%bd             | delete all buffers                               |
| :wall            | write all changed buffers                        |
| :wn              | write current buffer and jump to next            |
| :w filename      | save current buffer to other file                |
| :saveas filename | save current buffer to other file and open it    |
| :e               | reload file to get colored syntax                |
| :e <file>        | load file into buffer and put in current window  |
| :new             | open new buffer (no name) in split window        |
| :enew            | open new buffer (no name)  in current window     |
| :qa              | close all buffers and close vim                  |

|                     | Opening files                                    |
|---------------------|--------------------------------------------------|
| :next <with params> | open multiple files                              |
| :next / :prev       | go to next/prev file, close current one          |
| :arglist            | show list of open files                          |
| :find               | find file recursively according to 'path' option |

* any sub directory



|            | Windows                         |
| ---------- | ------------------------------- |
| :sp[lit]   | Split new window horizontally   |
| :vs[plit]  | Split new window vertically     |


|            | Tabs                                                |
|------------|-----------------------------------------------------|
| :tabe[dit] | open file in new tab (if no param, open new buffer) |
| gt / gT    | switch tabs                                         |

