#!/bin/bash          
echo Starting Git Pull
pwd
git pull https://github.com/mikebranstein/IoT master
echo Ending Git Pull 

# node agent/vsoagent
# Ctrl-Z
# jobs
# bg 1 (to keep a job running in bg)
# fg 1 (to move a job to foreground)