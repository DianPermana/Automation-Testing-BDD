# Framework Automation 

this is basic end to end UI Automation testing using python 3.11 and pycharm tools

### Feature
1. Behavior driven development (BDD)
2. Page object Model (POM)
3. Selenium
4. Allure Reporting


### Test run
https://user-images.githubusercontent.com/18004033/229706622-5d627be1-ce1c-4371-b7c8-da62e4d41760.mp4



### Result testing 

![img.png](img.png)


### how to use allure report

#### Install allure-behave

`pip install allure-behave` or check this https://github.com/behave/behave 

#### run allure report

`behave -f allure_behave.formatter:AllureFormatter -o .\reports\ .\features\login.feature`

#### show result

`allure serve %allure_result_folder%`
