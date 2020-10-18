
# Linux system

## System

|                                           |                                                                                        |
|-------------------------------------------| ---------------------------------------------------------------------------------------|
| initd                                     | <https://en.wikipedia.org/wiki/Init>                                                   |
| systemd                                   | <https://en.wikipedia.org/wiki/Systemd>                                                |
| services, runlevels and rcd scripts       | <https://www.linux.com/news/introduction-services-runlevels-and-rcd-scripts>           |
| udev                                      | <https://en.wikipedia.org/wiki/Udev>                                                   |
| eudev  (@toread)                          | <https://wiki.gentoo.org/wiki/Eudev>                                                   |
| Linux File system                         | <http://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/usr.html>                     |
| Wayland (display server) (@toread)        | <https://en.wikipedia.org/wiki/Wayland_(display_server_protocol)>                      |
| Shells                                    | <https://docs.slackware.com/howtos:cli_manual:shells>                                  |
| Bash                                      | <https://docs.slackware.com/slackbook:bash>                                            |
| Users and Groups                          | <https://wiki.archlinux.org/index.php/users_and_groups>                                |
| Linux - overview of memory management     | <http://www.linuxhowtos.org/System/LinuxMemoryManagement.htm>                          |
| Change root                               | <https://wiki.archlinux.org/index.php/Change_root>                                     |
| gshadow                                   | <https://www.man7.org/linux/man-pages/man5/gshadow.5.html>                             |
| Linux PAM                                 | <https://en.wikipedia.org/wiki/Linux_PAM>                                              |
| Securing applications on Linux with PAM   | <https://www.linuxjournal.com/article/5940>                                            |
| The Linux-PAM System Administarator Guide | <http://www.linux-pam.org/Linux-PAM-html/Linux-PAM_SAG.html>                           |
| What is D-Bus practically useful for?     | <https://unix.stackexchange.com/questions/604258/what-is-d-bus-practically-useful-for> |


### Bash
* (non)interactive (non)login shells
    * <https://askubuntu.com/questions/438150/scripts-in-etc-profile-d-being-ignored>
    * <https://www.quora.com/What-is-bash_profile-and-what-is-its-use>
* Difference betwwen nohup disown and &
    * <https://unix.stackexchange.com/questions/3886/difference-between-nohup-disown-and>
* About glob <https://mywiki.wooledge.org/glob>

### dotfiles examples
* dotfiles + install script <https://github.com/maguec/dotfiles>

### SSH
* eleven ssh tricks                         http://www.linuxjournal.com/article/6602
* Understanding SSH                         https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process
* SSH guide                                 https://kimmo.suominen.com/docs/ssh/
* SSH on slackware                          http://www.linuxquestions.org/questions/slackware-14/howto-ssh-slackware-and-any-linux-419680/ 
* SSH tunneling                             http://www.linuxjournal.com/content/ssh-tunneling-poor-techies-vpn
 
### Samba and NFS
* Samba - private and quest no password    
  * <http://tech.waltco.biz/2008/01/26/private-and-guest-no-password-prompt-samba-shares-with-securityuser/>
* Samba - Security howto   <http://www.linuxhomenetworking.com/wiki/index.php/Quick_HOWTO_:_Ch12_:_Samba_Security_and_Troubleshooting>
* NFS howto     <http://tldp.org/HOWTO/NFS-HOWTO/index.html>
 
 
### md5
* md5 sums examples: <https://www.tecmint.com/generate-verify-check-files-md5-checksum-linux/>
 
### Linux daemon writing howto
* http://www.netzmafia.de/skripten/unix/linux-daemon-howto.html
* http://www.cyberciti.biz/tips/linux-write-sys-v-init-script-to-start-stop-service.html
* http://www.enderunix.org/docs/eng/daemon.php
* init-d-vs-cron-which-to-use      http://serverfault.com/questions/92783/init-d-vs-cron-which-to-use

### CLI commands and services
* poular linux commands                     http://cb.vu/unixtoolbox.xhtml
* pupular linux commands                    http://www.pixelbeat.org/cmdline.html
* Finding stuff in Linux                    http://www.ice2o.com/findingstuff.php
* regular expressions                       http://www.regular-expressions.info/reference.html
* grep command to search in sub dirs        https://www.cyberciti.biz/faq/grep-command-in-unix-to-search-in-subdirectories-examples/
* Grep guide                                http://www.grymoire.com/Unix/Grep.html
* Sed guide                                 http://www.grymoire.com/Unix/Sed.html
* screen reference                          http://aperiodic.net/screen/quick_reference 
* a killer screen config file               https://gist.github.com/joaopizani/2718397
* At Your Service - Job Scheduling for Linux http://www.linuxjournal.com/article/4719

### General guides
* Alien wiki - Linux in general         http://alien.slackbook.org/dokuwiki/doku.php?id=linux:linux
* Computer hope Unix/Linux help         http://www.computerhope.com/unix.htm
* Linux home server howto               http://www.brennan.id.au/index.html
* Embedded Linux practical labs         https://bootlin.com/blog/beagle-labs
* Unix philosphy                        https://en.wikipedia.org/wiki/Unix_philosophy
* Cross Linux from scratch              http://trac.clfs.org/
* General cli guids                     https://shapeshed.com/posts/

-----------------------------------
## Development
* An ffmpeg and SDL Tutorial or How to Write a Video Player in Less Than 1000 Lines        http://dranger.com/ffmpeg/
* Kernel development in Qt Creator     https://themeaningfulengineer.github.io/Kernel-developemnt-in-QtCreator/
* strace guide                         http://www.dedoimedo.com/computers/strace.html
 
 
### Libs
* ldd and ldconfig               https://www.linux.org.ru/forum/general/8078612
* to read man of this commands:
  * ldd
  * ldconfig
  * ld.so
  * rpath
  * chroot
 
 
-------------------------------------
## Kernel

* Linux kernel on wikipedia     <https://en.wikipedia.org/wiki/Linux_kernel>
* Life cycle of process     <http://www.linux-tutorial.info/modules.php?name=MContent&pageid=84>
* Linux kernel driver writing tutorial  2008 Greg Kroah-Hartman
  * <https://www.youtube.com/watch?v=CqDUfiH2PzQi>
* Building linux kernel from source <https://wiki.alienbase.nl/doku.php?id=linux:kernelbuilding>
* initrd        <https://www.kernel.org/doc/html/v4.12/admin-guide/initrd.html>

-------------------------------------
## Real Time
* /dev/rtc documentation    <http://www.mjmwired.net/kernel/Documentation/rtc.txt>
* high resolution timer programming <https://rt.wiki.kernel.org/index.php/Cyclictest>
* Soft real time programming with linux         <http://www.drdobbs.com/184402031;jsessionid=TCIJ0XLNLRSEBQE1GHPSKHWATMY32JVN>
* IO Port - programming high resolution timing
  * <http://tldp.org/HOWTO/IO-Port-Programming-4.html>
* Real time linux wiki      <https://rt.wiki.kernel.org/index.php/Main_Page>
* howto:build and RT application , linux <https://rt.wiki.kernel.org/index.php/HOWTO:_Build_an_RT-application>
 
