# Django Blog

## Useful Constants
* Navigation Bar Background Colour - #2f2fa2
* Page Background Colour           - #2f2fa2
* Text Color                       - #000000
* Secondary Text Color             - #f64c72

docker run --mount type=bind,source=C:\Users\Tom\Documents\SnowplowAnalytics\django-blog\micro-conf,destination=/config -p 9090:9090 snowplow/snowplow-micro:latest --collector-config /config/micro.conf --iglu /config/iglu.json