# assessment_lizard
Please clone this repo

first acivate virtual environment

1) source blog_venv/bin/activate

then

2) cd blog

after that

3) python3 manage.py runserver

## Test Goals

Our simple blog webiste have few pages. Everybody can register then can post any blog they desire.
please take a look at few urls bellow:

http://localhost:8000/

http://localhost:8000/register/

http://localhost:8000/login/

http://localhost:8000/blogpost/

http://localhost:8000/blog-detail/

Without changing the current setup complete the website as describe bellow:

1) Create a Django custome user model to have firstname, lastname, gender, date of birth, email, password, date of joined and at the end terms to accept. Then complete login proccess.

2) In http://localhost:8000/blogpost/ use Django from for creating a new blog post, in this URL user should be authenticated if not redirect the user to login page.
and if the user is authenticated shouldn't be able to go to register page. pay attention each blog post can have more than one image.

3) In home page all webiste visitors should be able to see all blog posts, when they click on a particular post should redirect them to a new page for reading more.
http://localhost:8000/blog-detail/ (Don't forget to make pagination at home page).

4) Create a new page for a user that can view his/her posts and be able to edit and delete any post they desire. Attention that the user should be authenticated.

Feel free to install any Django app or packages you need.

Good luck






