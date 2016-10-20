# Uses cases:

List of all uses cases.

1)  Register.
2)  Login.
3)  Logout.
4)  Edit profile.
5)  Validate user email.
6)  Create new task.
7)  Modify user task.
8)  Delete user task.
9)  Archive user task.
10) Create new category.
11) Modify category.
12) Delete category.
13) Create new user sub task.
14) Modify user sub task.
15) Delete user sub task.
16) View user task.
17) View user sub task.
18) View category.
19) View profile.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 1: Register.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 2: Login.
    * Principal actor: User.
    * Precondition: El servidor funciona correctamente.
    * Sussefun scenario:
        1. The user select the option "Login".
        2. The system muestra la pantalla de login, con los parámetros: Nombre y password.
        3. El sistema confirma el logeo exitoso y lo redirecciona a su lista de metas.
    * Exceptional scenario:
        3. i. El seudonimo o contraseña son invalidos.
            * El sistema notifica error y que vuelva a intentar.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 3: Logout.
    * Principal actor: TODO.
    * Precondition: TODO.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 4: Edit profile.
    * Principal actor: User.
    * Precondition: TODO.
    * Successful scenario:
        1. The user select "Edit profile".
        2. El sistema muestra el perfil del usuario con la posibilidad de hacer cambios en los parámetros que desea.
        3. El usuario hace los cambios que desea.
        4. El sistema confirma la operacion.
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 5: Validate user email.
    * Principal actor: TODO.
    * Precondition: The user is login, y el servidor funciona correctamente.
    * Successful scenario: TODO.
        1. .
        2. .
    * Exceptional scenario:
        3. i. TODO.
            * TODO.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 6: Create new task.
    * Principal actor: User.
    * Precondition: The user is loggin on the system.
    * Successful scenario:
        1. The user choose the option "create new task".
        2. The system sign a form to complete with nexts elements: Title, Descriptión, date and time to finish, sub-task.
        3. The user complete the form.
        4. The system confirms the operation.
    * Exceptional scenario:
        3. i. The user leaves without completing parameters.
            * The system reports all parameters must be completed and redisplay the form as it had completed the user.
            * The user complete all parameters.
            * The system confirms the operation.

![separador](http://www.bigband.es/img_cm/separador.png)

* Use case # 7: Modify user task.
    * Principal actor: User.
    * Precondition: The user is loggin on the system. Has created at least one goal.
    * Successful scenario:
       

        1. El usuario selecciona de sus lista de metas la que desea modificar.
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