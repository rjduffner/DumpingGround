import pkg_resources

spec = "selenium#selenium/webdriver/firefox/webdriver_prefs.json"

req, subpath = spec.split('#')
req = pkg_resources.Requirement.parse(req)

filepath = pkg_resources.resource_filename(req, subpath)

print filepath
