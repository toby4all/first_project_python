# first_project_python
# The files in this project are as follows
     #backend testing.py- post, get, update and delete method route testing.
     
     #frontend testing.py- For testing route that returns html element using selenium for testing it..
     
      #db_connector.py. for establishing connection with the datbase using functions to perform crude operation  for the database.
      this functions will be exported to the server script. rest_app.py
     
      #resp_app.py- contains api server bult with Flask.
       each of the methoods in this route should return a json file on request.
       web_rest.py. This script contains only route expected to retun htm elements on request not json.
      
       combine_testing.py. This contains both forntend and backend testing that was accomplished previously. 

#The web_rest.py works perfectly with the database and I was able to test using Selenium with the frontend
test.py script. 

The route for rest_app.py is working now and I am getting a Json response but not the response I want because I am 
getting a status code of 500 which say user does not exist when I try to post a new user to the database
with a new user Id ="3".


Please examine my code, I do not really know why am not getting the desired response from the database. 



