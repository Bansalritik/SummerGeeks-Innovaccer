# SummerGeeks-Innovaccer
An Application that captures the visitor's and host's information and triggers an email and SMS to the host about the visitor's details, also as the visitor checks out, it triggers an email to the visitor about his visit.
### Approach:
 I defined a model that contains all the attributes stored in the SQLite table. Then I created two forms, one for the submission and another to get the details of the checkout time. In views.py file, there are two functions defined mainly, one to get the input and store the visitor's arrival info into the SQLite database, send the required info to the host and another to set checkout time and send the checkout details to the visitor. It also takes care of certain errors and exceptions. Then used HTML, CSS for the frontend integrated with the backend.
   
### Steps to run:
    Requirements:
               Any platform that is capable of running django.
    Commands:
              Installation Commands:
                               pip install twilio
              Running Commands:
                               python manage.py runserver


You'll have to update the email host user and password in ``settings.py`` - 

      EMAIL_HOST_USER = "email_id@user.com"
      EMAIL_HOST_PASSWORD = 'Your_password'

Update the twilio SID and token in ``settings.py`` so that sms function works properly -

      TWILIO_ACCOUNT_SID = 'Your_SID'
      TWILIO_AUTH_TOKEN = 'Your_Token'
      
### Result:
    As soon as the check-In details are entered, an E-Mail and SMS is sent to the Host's E-mail address and phone.
    The SQLite database is updated with the user details.
    Also, during the check-Out an email is sent to the visitor's E-Mail containing the details regarding the 
    check-in along with check-out details, and the SQLite database is updated.
  

### User Interface:
![User Interface](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/user%20interface.jpg)


![UI 2](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/user-interface2.jpg)


### Submission Form:
![submission 1](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/submission1.jpg)


![Submission 2](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/submission2.jpg)


![Submission_3](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/submission3.jpg)


![Submission_4](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/submission4.jpg)


### Check-Out Form:
![Checkout_1](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/checkout1.jpg )


![Checkout_2](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/checkout2.jpg )


![Checkout_3](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/checkout3.jpg )


### SQL DATABASE:
![SQLite Database](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/database.jpg)


### No Such USER:
![NO_such Entry](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/error1.jpg )


![NO_such_Entry](https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/error2.jpg )



## Tech-Stack:
             HTML, CSS, Python, SQLite, Django


   
   
   
   
   
   
