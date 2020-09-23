# SAS Analysis Software
https://domains.bornais.ca

### About
The treatment and analysis of small angle scattering (SAS) data is always a technical hurdle and a barrier for many groups. Through this project, we aim to develop a web based analysis package for researchers to use. The goal is to make SAS accessible to non-experts to increase the applications of the technique.

### Current Features
* User authentication via email and password
* Uploading new datasets via .txt files and input fields
* Viewing all of your datasets by name
* Computing homogeneous I(q) curves

### Future Features
* Computing heterogeneous I(q) curves
* Editing datasets
* Deleting datasets

### Current Bugs
* Currently sometimes when loading the site for the first time it loads for a long time. This is most likely due to objects not being cached properly on the server. A remedy is hopefully going to come out soon.
* I(q) curves show other curves/colours. This is due to the need to clear plots in matplotlib. The fix is trivial and should be out in the next release.

### Tech Stack
* Python (used overall)
* Numpy, Scipy (used for certain computations)
* Pandas (used for testing)
* Flask (used as a back end for the web app)
* Flask-wtf, Flask-login, Flask-SQLAlchemy (different Flask modules used to extend functionality)
* Bootstrap (to make the website look nicer and also mobile friendly, though I don't recommend using this on mobile)
* BCrypt (used for better security)
* SQLite (database used to store user profiles and dataset info)
* Caddy Server V2 (reverse proxy)
* Gunicorn (used to run Flask app)
* Google Cloud Platform (VM used to host web app, but this is only temporary)

## Interested in supporting or want to know more?
Contact Jeremie Bornais at borna113@uwindsor.ca

#### Please note that since this is under development your datasets may be subject to being deleted in the event of a major update
#### The above message will be removed when the first stable release is issued