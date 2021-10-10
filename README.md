## E-Learning App
This app is an online learning platform helps create courses and content, let students to register in courses and chat with each other.

### APP features
- Students can create accounts and enroll in courses.
- Course creators can create courses in diffiernt categories
- Students can chat with each other


### Installation
1. Colne the project repository.
```bash 
git clone https://github.com/hussamEL-Hwary/E-learning-app.git
```


2. **Python 3.7** Follow [the instructions](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python) to install the latest version of python for your platform.

3. **Virtual Environment** I recommend using virtual environment this helps separate each app dependancies and packages. check [This](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for more details. 

4. **PIP dependencies** Once you virtual environment is created and running navigate to project main directory and run:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected in ```requirements.txt``` filee.

5. **Key dependencies** 
- [Django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- [DjangoRestFramework](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [channels](https://channels.readthedocs.io/en/stable/) Channels is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called ASGI.
- [django memcached](https://docs.djangoproject.com/en/3.2/topics/cache/) Django comes with a robust cache system that lets you save dynamic pages so they don’t have to be calculated for each request.

6. **Database**
Django has a built in ORM To map models classes to database tables you can do this by:
```bash
python manage.py makemigrations
python manage.py migrate
``` 

7. **Run server**
:warning: Make sure virtual environment is running.
To run the server execute:
```bash
python manage.py runserver
```
