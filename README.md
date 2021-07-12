
# Covid Resource tracker

Covid Resource tracker is a Django-based web application to simplify the search for very basic health resources. Users can search for health-related resources like Hospitals, Availability of Ambulances, etc. The legitness of resources is fully guaranteed as the resource posting is fully supervised by admins.

## Installation

It is a Django-based project. 

Create a virtual environment using 
```
python -m venv .env
```
Then create django project .
```
django-admin startproject project .
```

Then activate virtual environment using
```
source .env/bin/activate
```

Then install django using
```
pip install Django==3.2.5
```

Install required dependencies using the requirements.txt file.
```
pip install -r requirements.txt
```

## Features

* Users can search the details of resources (hospital, doctor, and others) of the nearest area 
* Only Admins and verified members can post the resources
* Blood donation campaign tracking
* Dynamic resources management
* Using Google Maps to find the nearest hospital of users locations

## Motive for this project
> We see many covid related applications that are made to give verified resources to the users, but they lack many things to provide the right information to users. By using our applications, users can get the required information without logging in or giving their personal information. Resources may be blood donations, oxygen cylinders, beds, medications, isolations, ventilators, ambulances services, and others that can be easily searched locationally. 
