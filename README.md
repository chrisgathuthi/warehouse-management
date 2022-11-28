# warehouse management application 
## project description 
The application takes in products for storage, all parameters are filled by the attendant. The model is called Stock. 
The application also records the outgoing products from the warehouse. In a model called Sales. 
The aim of this project was to test my understanding of django rest framework and cronjobs. 

The application has the following functions. 
- a cron job that runs and checks expired products based on shelf life and expiry date. If the product has expired. The product status is changed to expired. 
- The application has jwt authentication and token authentication to authenticate apis 
- The application uses DjangoModelPermissions

The model have several model fields, but one is excempted when making a request. 
```
shelf_life = models.DurationField(null=True)
```
the above field will take in a timedelta object when the data is posted to the backend. 

## how to use the application 
how to use the sales api.
```python
#create sales
http://127.0.0.1:8000/api/create-stock/
```
list all api shows all related sales under sales
```
#list all sales
http://127.0.0.1:8000/api/list-stock/

```
```
#update all sales
http://127.0.0.1:8000/api/update-stock/{id}

```
```
#delete sales 
http://127.0.0.1:8000/api/delete-stock/{id}

```


sales endpoints 
In sales endpoints I used viewsets to create them and the urls are in the routers.py in the root of the project
```python
#creating a sales instance
http://127.0.0.1:8000/api/v2/sales/
```

### Authentication 
token authentication endpoint
```python
http://127.0.0.1:8000/api/auth
```
simple JWT authentication 
```python 
#get token
http://127.0.0.1:8000/api/api/token/
#refresh token
http://127.0.0.1:8000/api/api/token/refresh/
#verify token
http://127.0.0.1:8000/api/api/token/verify/

```
## Contributor
This project was done by me, I will continue building and making changes