# Selenium with Python and Firefox

Install the selenium driver for firefox
```
brew install geckodriver
```

## Setting up a new python project

Create a directory for your project
```
mkdir selenium-example
cd selenium-example
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

