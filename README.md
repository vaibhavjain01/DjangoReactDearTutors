# DjangoReactDearTutors
First Attempt at React FE and Django BE

  
# Create directory for project  
# CD into that directory  
  
pip3 install pipenv  
pipenv shell  
  
pipenv install django==2.1.*  
pipenv install djangorestframework  
pipenv install django-rest-knox  
  
  
from root folder (Project Directory)  
npm init -y  
npm install -D webpack webpack-cli  
npm install -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties  
  
npm install react react-dom prop-types  
  
create file .babelrc in project directory (Root not django)  
contents of babelrc:  
{  
    "presets": ["@babel/preset-env", "@babel/preset-react"],  
    "plugins": ["transform-class-properties"]  
}  
  

