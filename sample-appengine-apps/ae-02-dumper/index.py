import os
import sys

# Print a form for testing of POST
print 'Content-Type: text/html'
print ''
print '<form method="post" action="/" enctype="multipart/form-data">'
print 'Zap Data: <input type="text" name="zap"><br>'
print 'Zot Data: <input type="text" name="zot"><br>'
print 'File Data: <input type="file" name="filedat"><br>'
print '<input type="submit">'
print '</form>'

# Dump raw CGI
# http://hoohoo.ncsa.uiuc.edu/cgi/in.html

print '<pre>'
print 'Environment keys:'
print ''
for param in os.environ.keys():
    print param, ':', os.environ[param]
print ''

# Dump the GCI data
print 'Data'
count = 0
for line in sys.stdin:
  count = count + 1
  print line
  if count > 100:
    break

print '</pre>'

# In case you want to test file uploading
