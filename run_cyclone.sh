#!/bin/bash

rm /tmp/cyclone.pid
twistd --pidfile /tmp/cyclone.pid -n cyclone-sse -l 0.0.0.0 --redis-host=redis --broker=redis