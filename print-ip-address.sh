#!/bin/sh

# This script attempts to print your IP address.

ifconfig en0 | grep "inet " | cut -d: -f2 | awk '{print $2}'
