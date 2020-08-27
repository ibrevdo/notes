---
order: 1

---

# Linux CLI How to's

## Time sync
update time using time server on linux
* http://www.cyberciti.biz/tips/synchronize-the-system-clock-to-network-time-protocol-ntp-under-fedora-or-red-hat-linux.html
* http://www.howtogeek.com/tips/how-to-sync-your-linux-server-time-with-network-time-servers-ntp/


## Calculate md5 checksum of a directory
* `find "$path" -type f -print0 | sort -z | xargs -r0 md5sum | md5sum`

## mplayer stream
* `mplayer -afm ffmpeg -cache 5000000 -prefer-ipv4 https://kanlivep2event-i.akamaihd.net/hls/live/749624/749624/kanbet_mp3/chunklist.m3u8`

* `mplayer -afm ffmpeg -cache 5000000 https://82.102.152.41/hls/live/749624/749624/kanbet_mp3/chunklist.m3u8`

* `mplayer -afm ffmpeg -nocache -prefer-ipv4 https://kanlivep2event-i.akamaihd.net/hls/live/749624/749624/kanbet_mp3/chunklist.m3u8`

## Linux and Youtube
how to download an MP3 track from a YouTube video
* https://askubuntu.com/questions/178481/how-to-download-an-mp3-track-from-a-youtube-video


## Virtualization
VirtualBox’s Little Secret: The Command Line
* http://www.linux-mag.com/id/7673/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+LinuxMagazine+(Linux+Magazine%3A+Top+Stories

