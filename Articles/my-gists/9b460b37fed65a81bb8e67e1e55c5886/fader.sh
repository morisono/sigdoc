#!/usr/bin/env bash

len=30

x=""

for i in *.mov
do
  x="$x $i -mix $len -mixer luma"
done

x="melt$x -consumer avformat:fade_$(date +$s%3N).avi vcodec=libxvid b=5000k"

eval $x
