
# 1st Question

from django.conf import settings

applist = list(settings.INSTALLED_APPS)
applist.append('blog')
settings.INSTALLED_APPS = tuple(applist)

# 2nd Question

import os, re, shutil

regex = re.compile('^a.*\.py$')
src = '/src/dir/'
dst = '/dst/dir/'

for root, dirs, files in os.walk(src):
	for dir in dirs:
		os.mkdir(os.path.join(dst, dir))
	for file in files:
		if regex.match(file):
			shutil.copy(os.path.join(root, file), os.path.join(dst, re.sub(src,'',root),file))


# 3rd Question

import time

def printElapsed(fn):
        def wrapped():
                start_time = time.time()
                result = fn()
                print time.time() - start_time, "seconds"
                return result
        return wrapped

@printElapsed
def someFunc():
        return "This function inside decorator"


if __name__ == "__main__":
        print someFunc()





