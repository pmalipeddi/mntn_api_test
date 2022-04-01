# mntn_api_test

Install venv and activate the environment
1. Clone the git project to a folder
2. cd to project folder
2. Install: Run this command in the same folder
            "python3 -m venv ./venv"
3. Activate venv with this command
   mac : source venv/bin/activate
   windows: \path\to\env\Scripts\activate
   
4. Install requirements.txt file by running the command
   "pip install -r requirements.txt"
   

Run the Tests
1. Run this command after activating the venv and installing requirements.txt file "pytest --html=Reports/Reports.html --self-contained-html"
2. It should generate the "Reports" folder in the with file which can open in any browser to view the results

Approach

1. Created utils.py file in api_utils folder which contains a class and methods to execute different API Types (GET, POST, PATCH,DELETE) using requests library from python for each of this method passing the headers and Authorization token
2. Created a config.py file for generating the Testdata (Ex: In this case I have created random names and emails for creating users)
3. Created a conftest.py file under "tests" folder where I have created a pytest.fixture for generating the token(In this case the token is constant and not dynamic but can also create a dynamic tokens for API autorizations) so this fixture can be used in all the API Authorization test cases
4. In the tests folder created "test_api.py" file where created all the test scripts as each function with the function name starting with "test" as py test recognizes and runs all the tests with this notation
5. First test script "test_get_users" is GET API where it retrieves all the users data and I have asserted on status code 200 and also making the return list is not empty
6. Second test script "test_create_user" is POST API where I have passed the parameters using pytest fixtures to this test case to generate as many users for different test scenarios after getting the response from the api also asserting on the resposne to validate it did created the users with data same test data provided
7. I have also created some negative test cases like invalid token to get 401 status code and 422 status code for Data validation failed
8. Update test case "test_update_user " with PATCH for this one to provide the user id for update I have again used get_user test script to get the data and then picked the first record from it to update. After getting the response also asserted on status code and the attributes that were updated 
9. Delete test case "test_delete_user" used the same approach as the updat user test case for getting the record to be deleted but after the deletion is completed validated the status code of 204 and also make sure the record does exist by calling the users api 