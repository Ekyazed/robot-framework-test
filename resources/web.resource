*** Settings ***
Library     ../Libraries/WebAutomation.py

*** Keywords ***
Login To Website
    Open Chrome Browser    url=https://robotsparebinindustries.com/#/  headless=False   closeBrowser=False
    Input Text      username    maria
    Input Text      password    thoushallnotpass
    Submit Form

Fill Form Five Times
    Wait Until Element Appear    firstname
    Input Text    firstname    Simon
    Input Text    lastname    Didier
    Select From Range   salestarget     30000
    Input Text    salesresult    35000
    Submit Form

Get All The Table Data
    Extract Data From Table    table