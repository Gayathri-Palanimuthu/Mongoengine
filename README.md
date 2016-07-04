# Mongoengine

MongoEngine is a bridge between Django and straight to pymongo. It's  syntax is close to that of django's own ORM and can be used outside of Django as well. 

Mongodb-engine requires Django non-rel which downgrades Django to 1.5 which showstpper as evryone wants the "latest and greatest" technologies.

PyMongo is the low-level driver wrapping the MongoDB API into Python and delivering JSON in and out and it totally depends on user preference whether to go for either.



Mongoengine 3.2.7

I prefer using Mongoengine (atleast to startwith) for its django like syntax and ORM, defining data models in a snap, validation , inheritance, faster than django-mongokit, constant updates and for documentation.
MongoEngine is built upon pymongo so of course you can drop into pymongo - or use raw pymongo in your code methods.

 Mongoengine, looks similar to how the structure of a table would be defined in a regular ORM. The key difference is that this schema will never be passed on to MongoDB — this will only be enforced at the application level, making future changes easy to manage.

