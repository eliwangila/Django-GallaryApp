# Gallary-App

## Author

[eliwangila](https://github.com/eliwangila)

This is a Django web application that is for displaying my photos taken from different locations and then put into different categories for viewing and searching.

## Technologies Used
 * Django
 * Python-3.8.12
 * Bootstrap
 

## Interactive Input

View photos from diffrent categories.

View photos from diffrent Locations.

Search photos by categories


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/eliwangila/
  ```
2. Creating virtual environment:
  ```bash
  pip install --user pipenv
  ```
3. Activate virtual environment:
  ```bash
  pipenv shell
  ```

4. Move to the folder and install requirements
  ```bash
  pip install -r requirements.txt
  ```
5. Run migrations
```bash
  python manage.py makemigrations app_name
  python manage.py sqlmigrate 0001
  python manage.py migrate
```
6. Running the application
  ```bash
    python manage.py runserver
  ```
7. Testing the application
  ```bash
  python manage.py test photos
  ```
Open the application on your browser `127.0.0.1:5000`.


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [ekirapaeli254@gmail.com]()

## License
* *MIT License:*
* Copyright (c) 2021 **Eli Wangila**
