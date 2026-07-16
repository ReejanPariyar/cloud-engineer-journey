#!/bin/bash
usage=$(df -h / |  tail -1 | awk '{print $5}' | sed 's/%//')

if [ $usage -gt 80 ]; then
  echo "Warning: disk usage is at ${usage}% - getting full!"
else
  echo "Disk usage fine at ${usage}%"
fi
