https://django-tutorial-447.herokuapp.com/

### Login Page
To run the account based features, a `secret` file needs to be one directory above Digital-Logic.
If `secret` is not there, then users won't be able to sign up of do other account maintenance.

To debug, remove the `secret` file and run the following code to start a debugging stmp server:

`python -m smtpd -c DebuggingServer -n localhost:1025`

The emails that would have been sent to users will display in the terminal.