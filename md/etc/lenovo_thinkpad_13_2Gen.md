
Lenovo thinkpad  configuration
====================================

Hardware
------------------------------------

| Module | Characteristics  | More     |
| -----  | ---------------  | -------- |
| CPU    | 4 cores i7-7500U | 2.7 GHz  |
| Memory | 16G              |          |
| HD     | 500 GB           |          |
| Slots  |                  |          |


Bios setup
-----------------------------------


Partitions list
-----------------------------------
```
477 GiB, 512110190592 bytes, 1000215216 sectors

Partition          Start        End   Sectors   Size Type
/dev/nvme0n1p1      2048     534527    532480   260M EFI System
/dev/nvme0n1p2    534528     567295     32768    16M Microsoft reserved
/dev/nvme0n1p3    567296  293535743 292968448 139.7G Microsoft basic data           C:
/dev/nvme0n1p5 293535744  327090175  33554432    16G Linux swap
/dev/nvme0n1p6 327090176  431947775 104857600    50G Linux filesystem               /
/dev/nvme0n1p7 431947776  998166527 566218752   270G Linux filesystem               /home
/dev/nvme0n1p4 998166528 1000214527   2048000  1000M Windows recovery environment
```

Boot loader : grub2
------------------------------------
* to switch to linux:
    * edit `/etc/default/grub`: GRUB_DEFAULT=0
    * `grub-mkconfig -o /boot/grub/grub.cfg`
    * reboot

* to switch to windows:
    * edit `/etc/default/grub`: GRUB_DEFAULT=2
    * `grub-mkconfig -o /boot/grub/grub.cfg`
    * reboot


Windows 10
------------------------------------
password:


Slackware 14.2+ (ie current based on 14.2)
-------------------------------------
* hostname:ultra-haze, 
* users:mago/igor,root/$okol23
* Kernel version:         4.19.24
* Ktown versions:
* KDE                     5_19.02
    * KDE Frameworks      5.55.0
    * Plasma              5.13
    * Applications        18.12.2
    * QT                  5.12.1


Update slackware
-----------------------------------------
```sh
slackpkg update
slackpkg install-new
slackpkg upgrade-all
slackplg clean-system
```

### if using grub
`grub-mkconfig -o /boot/grub/grub.cfg`

Notes
------------------------------------------
Slackware was added with help of this video
<https://www.youtube.com/watch?v=kBIWSEoWIkw>
