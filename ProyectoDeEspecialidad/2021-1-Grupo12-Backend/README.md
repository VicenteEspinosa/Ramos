# Grupo12 - Backend
​
Capstone project G12 - OSAM Ingeniería
​
## Contributors
- Amaia Juanchuto
- Hans Hartmann
- Vicente Espinosa
- Francisco Araneda
- Matias Ovalle


## How to use

In order to run this project, you need to have [Docker](https://docs.docker.com/get-docker/) 
and installed. For Windows users, 
[Docker + WSL2](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers) is needed, 
while for Linux, [docker-compose](https://docs.docker.com/compose/install/) must be installed.

:warning: Please make sure Docker is working before running the script.

:warning: For Windows, following scripts must be run within a WSL2 console. Also, make
sure that the WSL distribution is [enabled](https://docs.docker.com/docker-for-windows/images/wsl2-choose-distro.png) in the Docker Graphical panel settings.


First Clone this repository and then
```sh
cd 2021-1-Grupo12-Backend
# Install dependencies and migrate database
./development.sh setup
# Start the server
./development.sh
```
Thats everything! :tada:

Here are some other commands that will be **very useful** during development:
```sh
# Start the server. Exit with ctrl + c
./development.sh
 
# Delete the Local Database
./development.sh db:drop

# Migrate the database
./development.sh db:migrate

# Reset the database (drop + migrate + seed) Useful for cleanup!
./development.sh db:reset

# Run python / poetry commands
./development.sh shell # Now you can use poetry

# Initial setup 
./development.sh setup

# Uninstall (Reverts setup)
./development uninstall

```

## Development users
The following user and passwords can be used for development!
```
devuser:  dev12345 (Admin)
devuser2: dev12345 (Admin)
```

## How to run Poetry commands

Simply run ```./development shell``` and then start typing the commands! If you add
a new dependency, you must run after that ```./development.sh setup``` to apply  the 
changes!


## How to Manage the Database :bar_chart:

```./development.sh``` comes with an integrated Graphical Mongo editor, called
[Mongo Express](https://github.com/mongo-express/mongo-express). 

When the server is running, just go to http://localhost:8081 and you will be able
to see and manage the database :tada:.

---


## How to use (Old Way)

**WARNING: This way of running the backend is more complicated and the connection with the database is slower.** 
Prefer running the backend with the Docker method explained previously
​
### Installing dependencies:
​
#### With Poetry (recommended):
​
1. Install Poetry, the modern package manager:
​
```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```
​
2. Install requirements with: 
```
poetry install
```
​
### Running the app (Old way)
​
Create a .env at the root of the project with the following structure:
​
```
B_MONGO_URI=String here
```
​

Run the following commands: 
```
poetry run osam_backend/manage.py migrate
poetry run python osam_backend/manage.py runserver
```
and the local server should be up.
​
## How to manage this project using Poetry
​
### Basics
​
1. To add a new dependency, run `poetry add name-of-your-dependency`. Example `poetry add pandas`.
   It will update `pyproject.toml` and `poetry.lock`. You must include poetry.lock on git,
   since it will assure that you and your team have the same version
   of every package of your project.
2. For running anything using Poetry virtualenv, use `poetry run`. Example `poetry run my_script.py`.
3. If you want to read any linter rule to your project, go to `setup.cfg`.
​
## pre-commit hook
​
In order to mantain an optimal code quality, you can use the `.pre-commit-config.yaml`
file to setup a git pre-commit hook. It won't let you make a commit if your code
violates some of the rules specified in the `setup.cfg` file.
If you want to use it, run `poetry run pre-commit install`.
​
This code static review will be necessary to merge a Pull request into develoment and main.
​
# OSAMBackend
​
The backend of the app is developed using Django and MongoDB. The connection to the database is done through [Djongo](https://www.djongomapper.com/). Also, in order to create endpoints, the models and serializers used are inherited from [DRF](https://www.django-rest-framework.org/). 
​
The Django structure is different from other backend frameworks, and the largest difference is that instead of using the classic MVC, it uses a MTV structure which stands for Models, Templates and Controllers, where the templates act like the ancient views. As OSAMBackend only deals the backend of an application this part contains **Models and Views**.
​
The project is accessible through the `osam_backend` folder. In the folder, we will find the following files or folders:
​
- `manage.py`: It is used to communicate with the CLI in order to run the server, open the shell, make and run migrations.
- `config.py`: It is used to access the variables contained in the `.env` file
- `osam_backend`: It is the **project** folder and it contains files to specify the settings of the entire project and the `urls.py` to specify the different connections through URLs. 
- `backend_app`: It is the **application** folder, all the files concerning the models, views, serializers, migrations and tests can be find in this folder. 
- `tests`: It contains only one file to test the pre-commits.
​
## How to run the server
​
1. Place yourself in the repository root and run: 
​
```
source .env
```
2. Run the following command:
```
poetry run python osam_backend/manage.py runserver
```
## Endpoints
​
Endpoints can be found in https://documenter.getpostman.com/view/11793429/TzY1gbaz 
