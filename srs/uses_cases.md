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
        2. El sistema muestra la meta con sus caracteristicas, y algunas opciones, entre ellas la opción "Modificar".
        3. El usuario selecciona la opción Modificar.
        4. El sistema muestra un formulario con las caracteristicas que puede modificar de la meta, entre ellas: submetas, tiempo de plazo, etc.
        5. El usuario hace las modificaciones pertinentes.
        6. El sistema confirma que se modificó exitosamente.

    * Exceptional scenario:
        5. i. El usuario hace modificaciones de forma incorrecta en algún parametro.
            * El sistema informa de dicho error y resalta los parametros que tiene que reveer el usuario.
            * El usuario hace los recambios necesarios.
            * El sistema revisa que está todo bien y confirma la operación.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 8: Delete user task.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 9: Archive user task.
    * Principal actor: Usuario.
    * Precondition: El usuario está loggueado en el sistema, y ya tiene al menos una meta creada.
    * Successful scenario:
        1. El usuario selecciona de sus lista de metas sin archivar la que desea archivar.
        2. El sistema muestra la meta con sus caracteristicas, y algunas opciones, entre ellas la opción "Archivar".
        3. El usuario selecciona la opción archivar.
        4. El sistema muestra una lista con los nombres de las carpetas ya creadas, y al finalizar una opción "crear carpeta"
        5. El usuario selecciona una de las carpetas ya previamente creadas.
        6. El sistema confirma que se archivo exitosamente.

    * Exceptional scenario:
        6. i. El usuario selecciona la opción "crear carpeta".
            * El sistema muestra una ventana indicando que ponga el nombre de la nueva carpeta.
            * El usuario completa la opción con el nombre de la nueva carpeta.
            * El sistema revisa que no exista ya una carpeta con dicho nombre. Sino existe la crea y archiva la meta ahi, si sí existe indica: "Ya existe una carpeta con dicho nombre", archiva la meta en ésa carpeta y vuelve al menú inicial.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 10: Create new category.
    * Principal actor: User.
    * Precondition: The user is login.
    * Successful scenario:
        1. The user select "Create new category".
        2. El sistema muestra el campo para que se escriba el nombre de la categoria.
        3. El usuario rellena el campo y hace clic en “Crear”.
    * Exceptional scenario:
        3. i. El usuario rellena con caracteres o formatos invalidos los datos de la meta.
            * El sistema notifica que esta mal y pide que se reintente.
          ii. The category alredy exist.
            * El sistema notifica que ​ ya existe la categoria.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 11: Modify category.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 12: Delete category.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 13: Create new user sub task.
    * Principal actor: User.
    * Precondition: The user is login on the system and select a task.
    * Successful scenario:
        1. The user select "Create sub task".
        2. The system sign a form to complete with nexts elements: Title, Descriptión, date and time to finish.
        3. The user complete the form.
        4. The system confirms the operation.
    * Exceptional scenario:
        3. i. The user leaves without completing parameters.
            * The system reports all parameters must be completed and redisplay the form as it had completed the user.
            * The user complete all parameters.
            * The system confirms the operation.
          ii. El vencimiento es mayor al vencimiento de la meta madre.
              El sistema informa el error y ​ pide que ingrese un vencimiento menor al vencimiento de la meta madre.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 14: Modify user sub task.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 15: Delete user sub task.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 16: View user task.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 17: View user sub task.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 18: View category.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 19: View profile.
    * Principal actor: TODO.
    * Precondition: TODO.
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