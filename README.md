## Web Automate

A simple stateless web service that allows one to interact with two web-browsers: Google Chrome and Mozilla Firefox.

The service supports the following endpoints:

| Method | Endpoint| Parameter(s) | Description 
| --- | --- | --- | ---|
| GET | /start | browser, url | Starts &#60;browser> which has the &#60;url> open inside it. |
| GET | /stop | browser | Kills the &#60;browser>. |
| GET | /cleanup | browser | Deletes all the browsing session information such as history, cache, cookies, downloads, saved passwords, etc for &#60;browser> |
| GET | /geturl | browser | Returns the current active tab's URL. Assume the <browser> has exactly one window and multiple tabs. |

Example usage of endpoints:

* http://&#60;server>/start?browser=&#60;browser>&url=&#60;url> should start the desired browser and open the URL in the same browser instance.

* http://&#60;server>/geturl?browser=&#60;browser> should get the current active tab URL for the given browser

* http://&#60;server>/stop?browser=&#60;browser> should stop the given browser if it is running

* http://&#60;server>/cleanup?browser=&#60;browser> should clean up the browsing session for the given browser if has been stopped.
