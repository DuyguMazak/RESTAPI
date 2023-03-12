[London Houses Dataset]( https://www.kaggle.com/datasets/arnavkulkarni/housing-prices-in-london)

**This repository contains an implementation of a RESTful API for serving the London Houses dataset. The dataset is persisted in a MongoDB database and can be accessed through the API endpoints defined in this project.**


**GETTING STARTED**

To run the API, you need to have Docker and Docker Compose installed on your system. If you don't have them yet, please follow the instructions provided in the following links:

    [Docker installation guide](https://docs.docker.com/get-docker/)
    [Docker Compose installation guide](https://docs.docker.com/compose/install/)

Once you have Docker and Docker Compose installed, follow these steps to run the API:

**1- Clone this repository to your local machine:** 
git clone https://github.com/yourusername/london-houses-restapi.git

**2-Open a terminal window and navigate to the root directory of the project.**

**3-Run the following command to start the API and the MongoDB database:**
docker-compose up

**4-Once the services are up and running, you should be able to access the API endpoints at http://localhost:5000/houses or you can open terminal and test with curl method.**



**API endpoints**

This API provides the following endpoints:

    PUT /houses: adds a new house to the dataset.
    GET /houses: retrieves a list of houses that match the query parameters.

**PUT /houses**

To add a new house to the dataset, send a PUT request to the /houses endpoint with a JSON payload that contains the data for the new house.

**GET /houses**

To retrieve a list of houses that match the query parameters, send a GET request to the /houses endpoint with the query parameters in the URL.



**Stopping the services**

To stop the API and the MongoDB database, press Ctrl+C in the terminal window where the services are running. Alternatively, you can run the following command in the root directory of the project:

**docker-compose down**
This will stop and remove the containers and networks created by docker-compose up.



**Conclusion**
That's it! You now have a working implementation of a RESTful API for serving the London Houses dataset. Feel free to explore the code and experiment with different queries to retrieve the data you need.

