1. Open a new folder in VS Code.

2. Open the new Terminal and Install Django by running the command -->  pip install django

3. Create a new Django project by running the command  -->  django-admin startproject project-name

4. It will create a new folder with the name project-name, as shown in the picture below:

  ![alt text](https://github.com/Yogesh11820/Django-project/blob/master/Screenshot%202023-04-06%20230346.png)
  
  
5. Close the current folder and open the project-name folder in VS Code.
   It should look like this:
   
   ![alt text](https://github.com/Yogesh11820/Django-project/blob/master/2.png)


6. In the terminal, run the command -->  python manage.py runserver.

   ![alt text](https://github.com/Yogesh11820/Django-project/blob/master/link%20-%204.png)

7. Ctrl + click on the link to open the page, as shown below:
   
   ![alt text](https://github.com/Yogesh11820/Django-project/blob/master/server-3.png)
   
   
8. To create an app, run the command  -->  python manage.py startapp app-name

   ![alt text](https://github.com/Yogesh11820/Django-project/blob/master/app-5.png)



[The app folder is created after running the startapp command, and the project folder is the folder with the same name as the main folder.]

9. In the app folder, create a urls.py file. This is a mandatory step for every Django project.


10. Register the app in the INSTALLED_APPS list in the settings.py file in the project folder.

   ![alt text](https://github.com/Yogesh11820/Django-project/blob/master/register-6.png)


12. In the project folder's urls.py file, specify the path for the app.

    ![alt text](https://github.com/Yogesh11820/Django-project/blob/master/url.png)


Now that the basic requirements for creating a Django application are fulfilled, you can develop the application according to your requirements.
