#imports for SQL data part 
import pyodbc 
from datetime import datetime, timedelta
import pandas as pd 

#imports for sending email
from email.mine.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

date = datetime.today() - timedelta(days=7)  #get the date 7 days ago

date = date.strftime("%Y-%m-%d") # convert to format yyyy-mm-dd

cnxn = pyodbc.connect(cnxn_str) #initialise connection (assume cnxn_str already defined)

# build up our query string 
query = ("SELECT * FROM customers"
         f"WHERE joinDate > '{date}'")

#execute the query and read to a dataframe in python 
data = pd.read_sql(query, cnxn)

del cnxn # close the connection 

#make a few calculations 
mean_payment = data['payment'].mean()
std_payment = data['payment'].std()

# get max payment and product details 
max_vals = data[['product', 'payment']].sort_values(by=['pament'], ascending=False.iloc[0])

#write an email message using the email library and send using smtplib
txt = (f"Customer reporting for period {date} - {datetime.today().strftime('%Y-%m-%d')}.\n\n"
       f"Mean payment amount received: {mean_payment}\n"
       f"Standard deviation of payment amounts: {std_payments}\n"
       f"Highest payment amount of {max_vals['payment']}"
       f"received from {max_vals['product']} product.")

#we build the message using the email librar and send using smtplib
msg = MIMEMultipart()
msg['Subject'] = "Automated customer report" #set email subject
msg.attach(MIMEText(txt)) #add text contents 

#we will send via outlook, first we initialise connection to main server
smtp = smtplib.SMTP('smtp-mail.outlook.com', '587')
smtp.ehlo() #say hello to the server 
smto.starttls() #we will communicate using TLS encrytion

#send email to our boss 
smtp.sendmail('joebidden@mail.com', 'joebidden@mail.com', msg.as_string())

#finalls disconnect from the mail server 
smtp.quit()