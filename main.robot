*** Settings ***
Documentation   Test robot with Robot Framework
Resource    resources/web.resource
Library     ../Libraries/WebAutomation.py

*** Task ***
Test For Real Type RPA
    Login To Website
    Fill Form Five Times
    Get All The Table Data
