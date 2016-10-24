# Uses cases:

List of all uses cases.

1.  Register.
2.  Login.
3.  Logout.
4.  Edit profile.
5.  Validate user email.
6.  Create new task.
7.  Modify user task.h
8.  Delete user task.
9.  Archive user task.
10. Create new category.
11. Modify category.
12. Delete category.
13. Create new user sub task.
14. Modify user sub task.
15. Delete user sub task.
16. View user task.
17. View user sub task.
18. View category.
19. View profile.

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 1: **Register.***
    * **Primary actor**: User.
    * **Precondition**: User has Internet connection and a browser installed and the Web Server is running.
    * **Successful scenario**: 
        1. User enters to the app's url and gets the login/register interface 
        2. User clicks on "register" button and then types username, email and password in the correct boxes. 
    * **Exceptional scenario**:
        3. User types wrong the email format and he needs to type again.
   

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 2: **Login.***
    * **Primary actor**: User.
    * **Precondition**: User has Internet connection, a browser installed  and an account in the system and the Web Server is running.
    * **Successful scenario**:
        1. The user enters to the app's url in the browser and gets the login/register interface.
        2. The user clicks on "login" button and types email and password in the correct boxes.
        3. The system shows an successful login in the screen and redirect the user to the main page where the personal goals are shown.
    * **Exceptional scenario**:
        1. The password or email is incorrect and user has to type it again.

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 3: **Logout.***
    * **Primary actor**: User.
    * **Precondition**: User has Internet connection, a browser installed, an account in the system and is already logged in, and the Web Server is running.
    * **Successful scenario**:
        1. User clicks on the "logout" button in the upper right edge of the screen.
        2. System logs out the user redirects him to the login/register menu.


![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 4: **Edit profile***.
    * **Primary actor**: User.
    * **Precondition**: User has Internet connection, a browser installed, an account in the system and is already logged in, and the Web Server is running.
    * **Successful scenario**:
        1. User clicks on "Edit profile" button.
        2. A new interface, where user can edit his data, It's shown to him on the screen.
        3. User changes the settings or information as he wishes and confirms the changes.
        4. A successful message is shown to the user on the screen.
    * **Exceptional scenario**:
        3. Changes can't be applied and the user has to try again.

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 5: **Validate user email***.
    * **Primary actor**: System.
    * ** Precondition**: The user is logged in, and the server is running.
    * **Successful scenario**:
        1. User tries to login to the system 
        2. System checks if the password and email are correct in the data base
        3. If it's all OK, the login process will proceed successfully
    * **Exceptional scenario**:
        3. email or password don't match with any in the data base and will return an wrong validation message.

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 6: **Create new task***.
    * **Primary actor**: User.
    * **Precondition**: User has Internet connection, a browser installed, an account in the system and is already logged in, and the Web Server is running.
    * **Successful scenario**:
        1. The user clicks on "create new task" option.
        2. A interface will be shown by the System to the user where he can complete the fields which describes the task: Title, Description, expiration date.
        3. The user full fills the form and submits the new task.
        4. The system confirms the operation and shows a success message.
    * **Exceptional scenario**:
        3. The user submit the task without completing all parameters. The system reports all parameters must be completed and displays uncompleted form for further full filling by the user.

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 7: **Modify user task.***
    * **Primary actor**: User.
    * **Precondition**: User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a task at least, and the Web Server is running.
    * **Successful scenario**:

        1. User selects a task by searching it or through the task list.
        2. A new interface is shown to the user where he can see the fields of a task (description, expiration date, etc) and several options where one of them is `Modify`.
        3. User selects the option `Modify`.
        4. The interface changes where the fields of the task are modifiable.
        5. User modifies the task as he desire, and submit the changes.
        6. A successful message is shown to the user, and the system saves the changes.

    * **Exceptional scenario**:
        1. The user modifies a task's field with the wrong format, so the system will show a invalid format message.
        2. The user has to modify again the field and continue the steps (from 5).

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 8: **Delete user task***.
    * **Primary actor:** User.
    * **Precondition:** User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a task at least, and the Web Server is running.
    * **Successful scenario**:
        1. User selects a task by searching it or through the task list.
        2. A new interface is shown to the user where he can see the fields of a task (description, expiration date, etc) and several options where one of them is `Delete`.
        3. User selects the option `Delete`.
        4. A warning message will be shown for the user if he is sure on delete the selected task.
        5. User has to confirm the warning.
        6. The system saves the changes.
    * **Exceptional scenario:**
        3. If the user deletes a wrong task, it can't be recovered.

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 9:** Archive user task.***
    * **Primary actor:** User.
    * **Precondition:** User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a task at least, and the Web Server is running.
    * **Successful scenario:**
        1. User selects a task by searching it or through the task list.
        2. A new interface is shown to the user where he can see the fields of a task (description, expiration date, etc) and several options where one of them is `Archive`.
        3. User selects the option `Archive`.
        4. The system archive the task and redirects the user to homepage.

    * **Exceptional scenario:**
        6. If the user archives the wrong task, it can be restored.
        
![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 10: **Create new category.***
    * **Primary actor:** User.
    * **Precondition:** User has Internet connection, a browser installed, an account in the system, is already logged in and the Web Server is running.
    * **Successful scenario:**
        1. The user selects `Create new category` from the main page.
        2. A new interface is shown to the user where he can create a new category inserting its name.
        3. User full fills the category name and submits it. **Exceptional scenario:**
        3. User types wrong the category name and submit it. It can be modify.
        4. User fills the Category name with an invalid format. A invalid format message it will be shown to the user and he has to proceed the remaining steps again (from 3).
        3.  If the category name is already used, a message it will be shown and the user can search it in the `search Category` button in the main page.

![separador](http://www.bigband.es/img_cm/separador.png)

* **Use case # 11: Modify category.**
    * **Primary actor:** User
    * **Precondition**: User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a category at least, and the Web Server is running.
    * **Successful scenario:**
        1. The user searches the category through `Search category` from the main page.
        2. A new interface is shown to the user where all the categories are on a list. The user selects the category for modify it.
        3. The name of the category is modifiable and the user types the new category's name and press `Enter`.
        3. The system will save the changes.
    * **Exceptional scenario:**
        3. If the user selects a wrong category it can be deselected.
        
![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 12: **Delete category.***
    * **Primary actor:** User.
    * **Precondition:** User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a category at least, and the Web Server is running.
    * **Successful scenario:**
        1. The user searches the category through `Search category` from the main page.
        2. A new interface is shown to the user where all the categories are on a list. The user selects the category for deletion.
        3. A warning message is shown to the user which he has to confirm the deletion.
        3. If the message is confirmed the system will delete the category selected.
    * **Exceptional scenario:**
        3. If the user deletes a wrong category it can't be recovered.

![separador](http://www.bigband.es/img_cm/separador.png)

* *Use case # 13: **Create new user sub task***.
    * **Primary actor:** User.
    * **Precondition:** User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a task at least, and the Web Server is running.
    * **Successful scenario:**
        1. The user selects a task from the list task or through searching it.
        2. Once he selected one, one of the option where is shown in the new interface is `add subtask`. The user has to press that option.
        3. A new interface is shown to the user where he can full fill the new subtask fields (expiration date, description, etc).
        4. The user once finished full filling the subtask fields, submits it.
        5. the system saves the new task linked with the task selected.
    * **Exceptional scenario:**
        3. The user leaves without completing parameters.
            * The system reports all parameters must be completed and redisplay the form with the fields uncompleted and those which were completed.
            * The user completes all parameters.
            * The system confirms the operation.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 14: Modify user sub task.
    * Principal actor: TODO.
    * Precondition: User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a task and subtask at least, and the Web Server is running.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 15: Delete sub task.
    * Principal actor: TODO.
    * Precondition: User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a task and subtask at least, and the Web Server is running..
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 16: View user task.
    * Principal actor: TODO.
    * Precondition: User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a task at least, and the Web Server is running.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 17: View user sub task.
    * Principal actor: TODO.
    * Precondition: User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a task and subtask at least, and the Web Server is running.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 18: View category.
    * Principal actor: TODO.
    * Precondition: User has Internet connection, a browser installed, an account in the system, is already logged in and has already created a category at least, and the Web Server is running.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 19: View profile.
    * Principal actor: TODO.
    * Precondition: User has Internet connection, a browser installed, an account in the system, is already logged in and the Web Server is running.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 20: .
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)