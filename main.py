import subprocess
import browsers
from browsers.osx import OSX_BROWSER_BUNDLE_LIST

def open_with_default_browser(default_browser_bundle_id,url):
    for browser, bundle_id, version_string in OSX_BROWSER_BUNDLE_LIST:
        if default_browser_bundle_id.lower() == bundle_id.lower():
            browsers.launch(browser, url=url)

def main():
    default_browser_bundle_id = subprocess.getoutput(cmd="sh getDefaultBrowser.sh")

    # TODO: 別タブ遷移を検知

    open_with_default_browser(default_browser_bundle_id=default_browser_bundle_id, url="https://github.com/ochio")
    

if __name__ == "__main__": 
    main() 