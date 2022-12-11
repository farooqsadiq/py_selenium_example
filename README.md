# Selenium with Python and Firefox

Install the selenium driver for firefox
```
brew install geckodriver
```

## Clone project and run

```
git clone https://github.com/farooqsadiq/py_selenium_example.git 
cd py_selenium_example

python3 -m venv venv
source ./venv/bin/activate
python -m pip install -r requirements.txt

python src/main.py
```

The next section explains some of the above commands.

## Starting the project from scratch

Create a directory for your project
```
mkdir selenium-example
cd selenium-example
python -m pip install --upgrade pip
```

Use your default python3 installation to create a new python virtual environment directory called venv. This will isolates python external modules.
```
python3 -m venv venv
```

Use the new virtual environment (venv).
You have to activate the venv in every new terminal. VSCode can do this for you. You can check the which python you are using to verify you are using the venv. 
```
source ./venv/bin/activate
which python
```

Optionally upgrade the pip module in the venv. You use pip to install modules.
```
python -m pip install --upgrade pip
```

Create a requirements file which list the different python modules your computer is going to use. I am just using the shell to put text into a file here.
```
cat << EOF > requirements.txt 
selenium
EOF
```

Install the modules in the requirements file into the venv directory
```
python -m pip install -r requirements.txt
```

Make two directories for source code and data. 
```
mkdir -p src data
```

Create a `data.csv` file.
```
cat << EOF > data/form_data.csv 
User,SearchString
james, What is the smelliest cheese in the world?
rashid, Do fish have ears
EOF
```

Write a small starter program
```
cat << EOF > src/main.py 
import selenium  # module you installed 
import csv       # built-in module

# __name__ is the MAGIC name of this module/file
if __name__ == "__main__":
    print "python src/main.py was run"

EOF
```

Run the project
```
python src/main.py
```

Modify the project to use selenium, run, test, and repeat.

Initialize the git reporitory, add a gitignore, and checkin the code. Create the remote repo first.
```
git init
git add \
    .gitignore \
    README.md \
    data \
    requirements.txt \
    src 

git commit -m "Initial Commit"
git remote add origin https://github.com/farooqsadiq/py_selenium_example.git
git branch -M main
git push -u origin main
