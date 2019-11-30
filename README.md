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

Update the twilio SID and token in ``settings.py`` so that sms function works properly, Also you need to verify the phone numbers on twilio that you are about to use as the host's number or the number on which you want to recieve messages -

      TWILIO_ACCOUNT_SID = 'Your_SID'
      TWILIO_AUTH_TOKEN = 'Your_Token'

Here , I have created a ``superuser`` that you can have access to using:
      
      usrename: admin
      password: admin
      
### Result:
    As soon as the check-In details are entered, an E-Mail and SMS is sent to the Host's E-mail address and phone.
    The SQLite database is updated with the user details.
    Also, during the check-Out an email is sent to the visitor's E-Mail containing the details regarding the 
    check-in along with check-out details, and the SQLite database is updated.

## SAMPLE IMAGES:

### User Interface:
<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/user%20interface.png" width="500px">


<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/user-interface2.png" width="500px">


### Submission Form:
<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/submission1.png" width="500px">


<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/submission2.png" width="500px">


<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/submission3.png" width="500px">


<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/submission4.jpeg" width="500px">


### Check-Out Form:
<img src="https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/checkout1.png" width="500px">


<img src ="https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/checkout2.png" width="500px">


<img src ="https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/checkout3.png" width="500px">


### SQL DATABASE:
<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/database.png" width="500px">


### No Such USER:
<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/error1.png" width="500px">


<img src = "https://github.com/Bansalritik/SummerGeeks-Innovaccer/blob/master/images/error2.png" width="500px">



## Tech-Stack:
             HTML, CSS, Python, SQLite, Django


## Credits

     Created and Developed By: Ritik Bansal
     Contact Email: ritik.4545@gmail.com
   
   
   
   
   
   
