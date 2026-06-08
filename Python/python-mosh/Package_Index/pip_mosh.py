
# How to upgrade pip
# pip3 install --upgrade pip

# search for all package install on machine
# pip3 list

# How to install earlier version of the package
# pip3 install requests==VERSION

# install latest version of the package
# pip3 install requests==2.9.*
# Alternative
# pip3 uninstall requests
# pip3 install requests
# Alternative latest version
# pip3 install requests~=2.9.0
# pip3 install requests = 2.*

import requests

response = requests.get("http://google.com")
print(response)

