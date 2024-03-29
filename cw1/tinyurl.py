# import urllib

# def makeTiny(url):

#   url='http://tinyurl.com/api-create.php?'+urllib.urlencode({'url':url})
#   return urllib.urlopen(url).read()

# import sys;
# from urllib.request import urlopen;
# url = str(sys.argv[1]);
# data = urlopen("http://tinyurl.com/api-create.php?url="+url);
# print(data.readlines()[1].decode());


# import contextlib
# from urllib.parse import urlencode
# from urllib.request import urlopen


# def make_tiny(url):
#     request_url = ('http://tinyurl.com/api-create.php?' +
#                    urlencode({'url': url}))
#     with contextlib.closing(urlopen(request_url)) as response:
#         return response.read().decode('utf-8')



from __future__ import with_statement
import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
import sys


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' +
                   urlencode({'url': url}))
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def main():
    for tinyurl in map(make_tiny, sys.argv[1:]):
        print(tinyurl)


if __name__ == '__main__':
    main()




