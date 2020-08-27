


https://flightaware.com/

Linux programming links

https://www.kernel.org/doc/
https://www.youtube.com/watch?v=CqDUfiH2PzQ
https://stackoverflow.com/questions/2594898/linux-thread-synchronization
https://users.cs.cf.ac.uk/dave/C/node31.html
https://www.kernel.org/doc/
https://www.kernel.org/doc/html/latest/kernel-hacking/index.html
https://www.youtube.com/watch?v=CqDUfiH2PzQ
https://www.youtube.com/watch?v=_8ZV-lSVs38


Skype with a grain of salt

Running binary-only applications might give open source literate people
a certain dose of unease. Even more so when this application runs at
computer start up, has constant outbound network access, becomes a
super node when open ports from the internet are detected, effectively
accepting random connections from other users on the internet. If you
are not scared enough already, think about access to your sound card,
camera, and precious files after reading the above!
Sure, some will argue that privacy is a thing of the past, and not to
run such applications if you don't want to, but sometimes you simply
don't have a choice. Whether it's your long distance family members or
coworkers and friends, price is the same, you are left with an ugly
written app (just look at that 64bit support) that is probably full of
horrible holes, intentional or not (really :^)
While safest thing, of course, is to avoid using it, and probably turn
off your computer for good, right before you put on that tin foil hat
or bury your head in a hole somewhere, we wont be exploring those
options in this awesome README!
Instead, we will start from the obvious, firewall unused ports on your
computer, in most cases it's fine to close them all down. Next in line
are also obvious things, if you do not trust that little light on your
camera, unplug it when your haircut is not presentable to the world.
Same goes for your microphone, and if it's an integrated one, take it
from the pro's in the police department that use adhesive tape to cover
it up :-)
Now that manual labor is out the way, we come to a much more fun part,
protecting your precious files in $HOME. For this we take advantage of
multi-user environment, and simply run Skype under another user with
basic access. Without further ado, create another user and group with:

  groupadd -g 666 spyke
    useradd -u 666 -d /home/spyke -m -s /bin/bash -g spyke spyke
    
    Optionally give this user access to hardware:
    
      usermod -G audio,video,pulse -a spyke
      
      If you previously had Skype set-up that you wish to keep, move it with:
      
        cp -a $HOME/.Skype /home/spyke
          chown -R spyke:spyke /home/spyke/.Skype
          
          Allow group execution:
          
            echo "%spyke ALL=(spyke) NOPASSWD: /usr/bin/skype" \
            >> /etc/sudoers.d/66_spyke
            
            Add your user to this new group:
            
              usermod -G spyke -a USERNAME
              
              Finally, run it like this:
              
                xhost +local: \
                && sudo -u spyke /usr/bin/skype
                
                Attention, due to lack of goofiness in this README, anagrams were used
                to fill that void. Together with some number crafting, level of Slack
                has peaked, and the trumpets were blown.
                
                
----








Links

https://gluek.info/wiki/
https://gluek.info/wiki/linux/bashkeyboardshortcutsru
https://gluek.info/wiki/linux/crontab
https://gluek.info/wiki/linux/screen
https://gluek.info/wiki/linux/temperaturemonitoringinlinux
http://mydebianblog.blogspot.co.il/2006/07/blog-post_24.html
http://mydebianblog.blogspot.co.il/2006/12/ssh.html


http://www.opennet.ru/
http://www.opennet.ru/base/sys/screen2.txt.html




Math courses
http://math.stackexchange.com/questions/1778446/where-do-i-start-learning-higher-mathematics

Digital signal processing - Symbol
https://en.m.wikipedia.org/wiki/Symbol_rate


Linux semaphore with max value
http://stackoverflow.com/questions/22193152/linux-c-create-semaphore-with-a-max-value


Programming Interview questions
https://www.interviewbit.com/

Josh Bloch, Lord of the APIs - A Brief, Opinionated History of the API
https://www.youtube.com/watch?v=ege-kub1qtk&feature=youtu.be


Python game
https://checkio.org/


python book - how to think like a computer scientist
http://interactivepython.org/courselib/static/thinkcspy/index.html

Book - Mr Vertigo
http://royallib.com/book/oster_pol/mister_vertigo.html


Beit Tsaida Zachi Reserve
http://goo.gl/maps/7yjCt




Linux kernel RTC guide
https://www.kernel.org/doc/Documentation/rtc.txt

TCP dump tutorials
https://danielmiessler.com/study/tcpdump/



Queen Omega - Rocking And Popping
https://www.youtube.com/watch?v=RnC2UL72858

Ski video
https://vimeo.com/32863936

Dafni Leef speech - 2011
https://www.mako.co.il/news-specials/social-protest/Article-21e985d46013231017.htm&Partner=flash_embedplayer

Мара - "Головокружения" ("Я голосую за мэра-гея!") - 1.10.2011
https://www.youtube.com/watch?v=_5rJAaox0c4

The American Dream By The Provocateur Network
https://www.youtube.com/watch?v=ZPWH5TlbloU&feature=related



http://www.evolchel.ru/whatistheman.htm

https://www.vidarholen.net/contents/wordcount/


Island culture
http://norse.ulver.com/articles/steblink/culture/index.html

Boris and Yulia wedding video
https://www.youtube.com/watch?v=mhReCgire5Q


Treks in Russia
http://www.club-perexod.ru 
http://www.vpoxod.ru/ 


test c embedded
http://www.rmbconsulting.us/a-c-test-the-0x10-best-questions-for-would-be-embedded-programmers
http://embeddedgurus.com/stack-overflow/2009/09/a-c-test-the-0x10-best-questions-for-would-be-embedded-programmers-reprised/

Megavalanche 2011 Top Race (Part 1 of 4)
https://www.youtube.com/watch?feature=player_embedded&v=qfwTlTxhbG0


tiuls and camping
http://www.tiuli.com/camping_sites.asp
http://tourism-il.livejournal.com/3627598.html
http://www.tzofit.co.il/id/7658008
http://www.tzofit.co.il/tour/showReviews.php?ts_id=104776
עין גב - קמפינג ליד כנרת
מצפה אופיר
גבעת יואב - אוהלים מונגוליים
קיבוץ דפנה
עין דבשה


C++ fstream files I/O
http://www.cplusplus.com/doc/tutorial/files/
http://www.cs.huji.ac.il/~etsman/Docs/gcc-3.4-base/libstdc++/html/27_io/howto.html

Hebrew quest
http://www.hebrewquest.osherbligvulot.com/WWW/Osher.htm


Whiskey list
1) whisky talisker, glenmorangie, lagavulin
2) laphroaig, scapa, caol ila
3) glenfiddich



Netek
https://www.netek.co.il/

More on linux threads
http://www.cs.cf.ac.uk/Dave/C/node31.html
http://stackoverflow.com/questions/1222865/guaranteed-yielding-with-pthread-cond-wait-and-pthread-cond-signal

Gimp courses
http://www.linuxchix.org/content/courses/gimp/

Linux books
http://www.e-booksdirectory.com/linux/top10.html
http://www.bloghash.com/2006/11/linux-resource-best-linux-books/
http://www.thegeekstuff.com/2009/01/12-amazing-and-essential-linux-books-to-enrich-your-brain-and-library/

kernel index
http://lxr.linux.no/

proc fs
kernel/Documentation/filesystems/proc.txt

linux boot
http://www.ibm.com/developerworks/linux/library/l-linuxboot/

busy box
http://www.linuxjournal.com/article/4335
http://www.linuxjournal.com/article/4395

Lecture by Prof. Hossam Haick, Honorary Doctorate Recipient     https://www.youtube.com/watch?v=2lKKA1amhQA
Забастовочное движение шахтеров 1988–1991                       http://ecsocman.hse.ru/data/024/831/1219/8-Levchik_111-119.pdf
Медитация для начинающих. Обучающее видео №1: Обучение базовой медитации.   https://www.youtube.com/watch?v=spbwnQ0B8yQ&list=PLk_DIFMPglOYDUx1NfKPqVcKncC-_e4m_
