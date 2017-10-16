# Welcome!
Notella is a mockup music recommendation system. It uses the MusicBrainz API to suggest songs based on direct connections between artists: band memberships, collaborations...

There's a server running Notella [here](http://ec2-52-25-177-224.us-west-2.compute.amazonaws.com/), give it a try!

# Installation
Clone the repo and install the required Python packages:
```
pip install -r pip-requirements.txt
```

Run the webserver using the following command:
```
python manage.py runserver 0:8000
```
If necessary, change the IP adress `0` and port `8000` in the command above.

That's it! Visit `http://localhost:8000` (or whatever IP and port apply in your case) and start discovering music.
