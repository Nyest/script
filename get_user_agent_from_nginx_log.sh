#!/bin/bash

awk -F'"' '/GET/ {print $6}' /var/log/nginx-access.log | cut -d' ' -f1 | sort | uniq -c | sort -rn