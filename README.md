# safeex_challenge
Code challenge for SafeEx

- Please create a simple Django project with only two views and one REST API endpoint. The views should be the login screen and a page displaying the current lunar phase (accessible upon logging in).

- The design of the pages and the information representation is unimportant and will not be assessed. The "lunar phase" page can either be text-based or have some graphics in it, the implementation is fully up to you.

- Use Postgres as the DB backend. Choose an application server and, possibly, a web server of your liking (Django built-in server, or Nginx + uwsgi/Gunicorn, or whatever else).

- The user should be able to log in with an email and password. Don't add the "forgot password" option or any other features - just the "email/password" prompt and a "login" button.

- The "public" REST API should only allow GET requests to the URL `/api/lunarphase/`. It should return JSON with some free-form data for the current lunar phase. The API should be accessible using basic HTTP authentication.

- The whole web app (all its services) should be containerized with Docker (you can choose to use Compose).

- Please create a repository on either Github, Gitlab or Bitbucket and provide access to me (vasili@safeex.com).

- Add a shell script run.sh to the repo. The script should launch the container(s) on the local system, so that the website is accessible at 127.0.0.1:80 locally. Assume that I have Docker and Compose installed on my Linux machine already.

- I should already have a user account (with my email) when the system runs. Please set some default password for my account.

- The idea is that I should be able to clone the repository, simply run the shell script and observe the result in the browser, without having to perform any additional manipulations.