## Automatic Bill Downloader

### Brief Overview
<p>This Automatic Bill Downloader was created in an attempt to alleviate the burden of repetitive 
manual tasks and optimise the process of acquiring data.</p>
<p>This project was initiated in response to a request from my brother who was growing tired of manually checking his
outstanding electricity bill.</p>
<p>This project makes use of <a href="(https://www.selenium.dev/">Selenium ID</a>E for automation</p>

### How It Works
<ol>
    <li>The web driver opens the electricity bill website and fills in the login details</li>
    <li>After successfully logging in, the driver looks for the download button and downloads the file</li>
    <li>The downloaded PDF file will then be extracted to text, 
        where it will filter down to the desired keyword (Amount Due)</li>
    <li>If keyword found, the console will print out the outstanding payment</li>
</ol>

### Steps to take:
<p>You only need to do this once.</p>
<p>Before running this downloader, please ensure that you have the necessary packages installed.</p>

```
pip install selenium
pip install webdriver-manager
pip install PyPDF2
```
<p>Change the desired file path in the main python script (AutomatedBill.py) to wherever you want your file to be 
saved.</p>

```
file_path = r"C:\Users\XXXXX\Downloads"
```

<p>Set your login details</p>

```
login_username.send_keys("**********")
login_password.send_keys("**********")
```

