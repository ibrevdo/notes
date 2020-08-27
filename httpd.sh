#!/bin/bash

DIR=/home/mago/work/notes/
EXE=server.py

webserver_start() {
    if [ ! -z $(ps caux |grep $EXE | awk '{print $2}') ]; then
        echo "Already running"
        return
    fi
    if [ -d $DIR ]; then
        echo "Starting webserver in $DIR"
        cd $DIR
        ./$EXE > /tmp/webserver.log 2>&1 &
    else
        echo "Cannot start webserver because $DIR doesn't exist"
    fi
}

webserver_stop() {
    killall $EXE
}

webserver_restart() {
    webserver_stop
    sleep 1
    webserver_start
}

webserver_status() {
    if [ ! -z $(ps caux |grep $EXE | awk '{print $2}') ]; then
        echo "Running"
    else
        echo "Not running"
    fi
}

case "$1" in
'start')
  webserver_start
  ;;
'stop')
  webserver_stop
  ;;
'restart')
  webserver_restart
  ;;
'status')
  webserver_status
  ;;
*)
  echo "usage $0 start|stop|restart|status"
esac
