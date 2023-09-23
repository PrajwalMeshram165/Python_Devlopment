import os
import pyttsx3 as p
#speak() converts text to speech
p.speak("Welcome to my chatbot")   
#loops until user specify to quit
p.speak("if you have any query select the any one of the option given bellow  ")
print("choose the relatable option given bellow:")
ques=input("\n a> Product related query \n b> Query related to product delivery \n c> Cancle the order :  ")
if ( ques == "a") :
	p.speak("you are selected Product related query ")
	a =input("\n a> Product quality issue \n b> want to contact deliveryboy \n c> change the product    \n d> Cancle the order :  ")
	if ( a == "a") :
		p.speak("you are selected the Product quality issue now you can change your product ")
	if ( a == "b") :
		p.speak("we will send the contact details of deliveryboy to you")
	if ( a == "c") :
		p.speak("now you can change your product ")
	if ( a == "d") :
		p.speak("your order will be canceled within 48 hours")
		
elif( ques == "b") :
	p.speak("you are selected Query related to product delivery ")
	b =input("\n a> change the delivery address \n b> want to reshudule the delivery \n c> Cancle the order :  ")
	if ( b == "a") :
		p.speak("now you can change the delivery address ")
	if ( b == "b") :
		p.speak(" now you can reshudule the delivery")
	if ( b == "c") :
		p.speak("your order will be canceled within 48 hours")
elif(ques == "c"):
	p.speak("your order will be canceled within 48 hours")
		