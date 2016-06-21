import os

bind = "0.0.0.0:%s" % os.environ.get('PORT', 8080)
workers = "4"
