## Adding a New Service
Adding a new service to the Python eHelply SDK is simple. It requires the creation of two files, and the modification of two additional files.
* Create a new directory inside of `./ehelply_python_sdk/services`. Name it after the new service
* Inside of that directory, create a `schemas.py` and `sdk.py` file. 
* Modify `./ehelply_python_sdk/services/services.py` to add an import for the new service
* Modify `./ehelply_python_sdk/sdk.py` to add a CONST representing the new service. Then add an IF statement for the new service inside of the _make_client method. Finally, add a new method called `make_<service_name>()`