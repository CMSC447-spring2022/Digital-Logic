# DigitalLogic
We created a Python Django based web app that supports a password protected launch into backend Docker workspace 
configured to run a modified version of Logisim.

### Login Page
To run the account based features, a `secret` file needs to be one directory above Digital-Logic.
If `secret` is not there, then users won't be able to sign up of do other account maintenance.

To debug, remove the `secret` file or use `Email(debug=True)`. Emails will not be sent in debug mode.

### Launcher
The launcher client communicates with a backend server running Kasm hosted on AWS.  
Kasm is a Docker container launcher.  When a user logs in they can get a fresh 
Logisim workspace.

### Selenium Tests
To run Selenium tests as a developer, run the app locally, then run the Selenium
integration tests.