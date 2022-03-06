#StoryType=WEB
#Owner=ejagruti
#CreationDate=7-12-2021 Tuesday
@Login
Feature: Create Company Feature

  Background:user is successfully logged in
  Given user opens the "http://localhost:90/finsys" url


  @Smoke @EndToEnd
  Scenario: Creation of a New Company by passing all Valid Details
  Given user is on the application login page
  And user is on the application login page
  When user enters "dummyfm" as username
  And user enters "passw0rd" as password
  And user clicks on login button
  Then user is on the application home page
  And user gets the message starting with "Welcome" on the top
  Given user is on the Home page
  When user clicks on the Financial Analysis menu
  And user clicks on the Manage Company link
  And user clicks on the New button
  And user enters "Kalsoft" as companyname
  And user selects "IT" as companytype
  And user selects "Support" as CompanySubtype
  And user enters "Pune" as Address
  And user enters "0202229548" as Phone
  And user enters "rahul@kalsoft.org" as email
  And user enters "APK097548S" as PANDetails
  And user enters "ABC123456AD" as TINDetails
  And user enters "9028716133"  as Mobile
  And user enters "www.kalsoft.org" as website
  And user selects "INDIA" as country
  And user selects "MAHARASHTRA" as State
  And user selects "PUNE" as city
  And user enter  "100" as totalemployees
  Then user clicks on the Save Button
  And New Company is on top of the Table