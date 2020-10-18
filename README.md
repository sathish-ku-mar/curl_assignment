# curl_assignment
### System Requirements
- Python 3+
------------
### 1. Create of virtual environment
Open the terminal and enter the following command:<br />`$ conda create -n <environment_name> python=3`<br />
Once the environment has been created, activate the environment:<br />`$ conda activate <environment_name>`

------------
### 2. Clone project to the local machine
In the terminal, navigate to the location where the project folder has to be created. Then enter the git command to clone the project:<br />`$ git clone https://github.com/sathish-ku-mar/curl_assignment.git`<br />
Once cloned, change the directory to **curl_assignment**<br />`$ cd curl_assignment`

------------
### 3. Install the project requirements
Install the python packages listed in the **requirements.txt** file.
Enter the following command in the terminal:<br />`$ pip install -r requirements.txt`

------------

### 4. Run the python file for Data Ingestion
To store the data into MongoDB from json file, run the following command:<br />`$ python tasks.py`<br />

------------

### 5. Run the development server for Flask API
To start the development server, run the following command:<br />`$ python app.py`<br />
By default the server runs on port`5000`<br />

------------
