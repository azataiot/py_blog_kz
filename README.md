# Python блогының толық орналастыру құжаттамасы
## 1. Тілді қалай өзгерту керек?
Бұл файлдағы тіл кодын өзгерту:  
` py_blog_kz\app\static\js\tinymce_setup.js `

## 2. Блог тілдің өзгеруін қалай құптайды?
` \py_blog_kz\app\templates\admin\admin_account.html`  


## 3. Толық орналастыру қадамдары

0. Нұсқаулық	
Мұнда қолданылатын операциялық жүйе: Ubuntu 15.10 Теориялық тұрғыдан Python блогы операциялық жүйеде орнатылған Python нұсқасы 2.6.x немесе 2.7.x.	
1. Python Blog бастапқы кодын алыңыз	
Python блогының бастапқы кодын алудың екі жолы бар:
Гиттің көмегімен
Python Blog жобасының өзіндік бетінен жүктеп алыңыз
**Біз осы екі әдісті енгіземіз, іс жүзінде, олардың біреуін ғана таңдауыңыз керек, біз бірінші әдісті ұсынамыз.**
(1) Git арқылы бастапқы кодты алыңыз
*Алдымен жүйеңізде Git нұсқасын басқару жүйесі орнатылғанын тексеріңіз:*

``` bash	
git version
«Git» бағдарламасы орнатылмаған. Орнату үшін келесі пәрменді қолдануға болады:	
sudo apt-get install git 	
```	

* Орнату аяқталған соң, пайдаланушы каталогында жоба каталогын жасаңыз:
``` bash 	
mkdir project	
cd project/	
```	
* Бастапқы кодты Python блог жобасының мекенжайынан жасаңыз:	
``` git 	
git clone https://github.com/yaakovazat/py_blog_kz.git	
``` 	
* Бастапқы код каталогының құрылымын қараңыз:
``` bash 	
ls	
```
``` bash	
app        LICENSE    migrations  README.md     requirements.txt
config.py  manage.py  Procfile    requirements	
```	
2. pip орналастыру
` sudo apt-get install python-pip` 	
3. virtualenv орналастыру	
` sudo apt-get install virtualenv`
4. Виртуалды ортаны құру	
``` python 	
virtualenv env	
``` 	

``` bash 
Running virtualenv with interpreter /usr/bin/python2
New python executable in venv/bin/python2
Also creating executable in venv/bin/python
Installing setuptools, pip...done.	
```		

5. Виртуалды ортаны белсендіру	
``` bash	
source venv/bin/activate	
```	
6. Python блогының талаптары файлын орнатыңыз...	
```	python 	
pip install -r requirements/common.txt   
```	
7. Data base :

**Дерекқордың конфигурациясынан басқа, Python блогы үшін барлық талаптар ортасы орнатылды және келесі екі аяқталуы керек:**	

7. 1	Sqlite әдепкі дерекқор ретінде пайдаланыңыз	
7. 2	MySQL-ді әдепкі дерекқор ретінде қолданыңыз	

Дерекқорды пайдалану тек олардың біреуін ғана талап етеді.	
Бірін таңдаңыз, себебі ол сізден ешқандай конфигурацияны талап етпейді. (Python әдепкі дерекқоры sqlite болып табылады)	


*	Sqlite әдепкі дерекқор ретінде пайдаланыңыз	
Блог каталогында келесі пәрменді орындаңыз:	
``` python 
python manage.py deploy product	
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 051691f120e6, fit to MySQL-ді
``` 	
Жоғарыда көрсетілген сұрақ пайда болса, бұл табысқа жетеді! MySQL-ға бейімделудің соңғы көрінісі үшін сіз таңқаларлық емессіз, бұл сол кездегі жай ғана ескерту, сонымен қатар MySQL-ді кейінірек пайдалануыңыз қажет.	

Жасалынған sqlite дерекқорын қараңыз:

`ls`	
```	
app        config.pyc   LICENSE    migrations  README.md     requirements.txt
config.py  data.sqlite  manage.py  Procfile    requirements  venv 	
```	

8. Блогты іске қосыңыз	
```	python 
gunicorn manage:app
[2016-03-08 11:49:11 +0000] [7189] [INFO] Starting gunicorn 19.4.5
[2016-03-08 11:49:11 +0000] [7189] [INFO] Listening at: http://127.0.0.1:8000 (7189)
[2016-03-08 11:49:11 +0000] [7189] [INFO] Using worker: sync
[2016-03-08 11:49:11 +0000] [7194] [INFO] Booting worker with pid: 7194	
```	
Жоғарыда келтірілген кеңестер блогтың ойдағыдай іске қосылғанын көрсетеді!	


9. Кеңес: Блог орналастырылғаннан кейін, онда ешқандай деректер жоқ. Егер Blog_mini функциясын тексеру үшін белгілі бір деректер қажет болса, жоғарыдағы әрекеттерді аяқтағаннан кейін келесі пәрменді орындауға болады:	

``` python
python manage.py deploy test_data	
```	


