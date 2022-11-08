from flask import Flask, render_template, request
import os

app = Flask(__name__)
browserLastVisitedURLS = dict()


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


############# START BROWSER ##############


@app.route('/start', methods=['GET'])
def start():
    if 'browser' in request.args and 'url' in request.args:
        browserName = str(request.args['browser'])
        url = str(request.args['url'])

        if browserName == 'chrome':
            command = "open -a 'google chrome.app' {}".format(url)
            os.system(command)
            browserLastVisitedURLS.update({browserName: url})
            return "Chrome fired up with specified url."

        elif browserName == 'firefox':
            command = "open -a 'firefox.app' {}".format(url)
            os.system(command)
            browserLastVisitedURLS.update({browserName: url})
            return "Firefox fired up with specified url."

        else:
            return "This browser is not available"

    elif 'browser' in request.args:
        return "Please specify a url"

    elif 'url' in request.args:
        return "Please provide a browser name"


############### STOP BROWSER ####################


@app.route('/stop', methods=['GET'])
def stop():
    if 'browser' in request.args:
        browserName = str(request.args['browser'])
        if browserName == 'chrome':
            os.system("pkill Chrome")
            return "Chrome closed"

        elif browserName == 'firefox':
            os.system("pkill firefox")
            return "Firefox closed"

        else:
            return "Browser not available."

    else:
        return "Browser not provided."


############# GETURL #################


@app.route('/geturl', methods=['GET'])
def geturl():
    if 'browser' in request.args:
        browserName = str(request.args['browser'])

        if browserName == 'chrome' or browserName == 'firefox':

            if browserName in browserLastVisitedURLS:
                return browserLastVisitedURLS[browserName]
            else:
                return "No url found"
        else:
            return "Browser not available."
    else:
        return "Browser not provided."


############ DELETE HISTORY ###############


@app.route('/cleanup', methods=['GET'])
def cleanup():
    if 'browser' in request.args:
        browserName = str(request.args['browser'])
        if browserName == 'chrome':
            os.system("rm -R /Users/swagata/Library/'Application Support'/Google/Chrome/Default/History")
            os.system("rm -R /Users/swagata/Library/Application Support/Google/Chrome/Default/Cookies")
            os.system("rm -R /Users/swagata/Library/Application Support/Google/Chrome/Default/DownloadMetadata")
            os.system("rm -R /Users/swagata/Library/Application Support/Google/Chrome/Default/Favicons")
            return "Chrome browser session information deleted"

        elif browserName == 'firefox':
            os.system("rm -R /Users/swagata/Library/'Application Support'/Firefox/Profiles/4l1nmf8p.default-release/cookies.sqlite")
            os.system("rm -R /Users/swagata/Library/'Application Support'/Firefox/Profiles/4l1nmf8p.default-release/favicons.sqlite")
            os.system("rm -R /Users/swagata/Library/'Application Support'/Firefox/Profiles/4l1nmf8p.default-release/places.sqlite")
            os.system("rm -R /Users/swagata/Library/'Application Support'/Firefox/Profiles/4l1nmf8p.default-release/storage.sqlite")
            return "Firefox browser session information deleted"

        else:
            return "Browser not available"
    else:
        return "Browser not provided"


if __name__ == '__main__':
    app.run()
