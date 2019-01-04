# Simple Automation Bot -  SAB

## Modules

* Services
* Web
* Utils

### Services Module

Rest Client
````
rc = RestClient('{IP or base uri}')
response = rc.get_request('{endpoint}')
print(str(response.content))
````
SSH Client
````
ssh = SSHClient({IP})
result = ssh.run_cmd({command})
print(str(result))
````

### Web Service

Install [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox or [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) to use Selenium with Chrome

Browser options: Chrome, Firefox

````
wd = WebDriver.create_driver('Chrome').run()
wd.navigate_url('http://www.python.org')
````

### Log
````
log = Log('sab.log')
log.info('Log info level')
````