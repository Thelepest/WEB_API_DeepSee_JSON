WEB API developed in Django. JSON format has been used for the client/server communication.
All datas are stored in an sqlite3 database.
The API has 1 model with 3 views that :
- recall the products available in the warehouse ;
- can add new products, or increase the amount in stock in case of the product already exists ;
- make a single-article order, showing the confirmation and decreasing the related amount from the stock. If
  the article doesn't exist, or the ordered amount exceeds the stock amount, the user receives an error message.

TO RUN THE API :
- Open your code editor (I used VSC);
- Install the required adds (see requirements.txt)
- Move to the project folder (cd store)
- Runserver : python manage.py runserver

TO USE THE FUNCTIONALITIES FROM BROWSER : 
- Open the local server at : http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin --> You can log as "admin"/"password" to see the products from the admin panel ;

TO SIMULATE GET/POST REQUEST and SEE the RESPONSE :
- Open your emulation layer (I use GIT BASH) ;
- GET(see products) --> curl http://127.0.0.1:8000/products/
- POST(new product) --> curl -X POST http://127.0.0.1:8000/add/ -H 'Content-Type: application/json' -d '{"name":"product_name", "amount_in_stock": 10}'
- POST(new order) --> curl -X POST http://127.0.0.1:8000/order/ -H 'Content-Type: application/json' -d '{"name":"product_to_order", "amount_in_stock": 5}'

OBSERVATIONS : 
- Considering that GIT BASH doesn't offer a "login" panel, I had to remove the voice "django.middleware.csrf.CsrfViewMiddleware" 
 from the settings.py file ;
- I prefered to use "curl" instead of the browser because I could easily force the POST request to my views.

Thanks for watching!
If you want to have more info, please write me at marco.biasone.90@gmail.com
Cheers! :)

