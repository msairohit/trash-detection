def eAlerts(data, os, y, index):
	imagePath = data.test_ds.items[index]
	imageName = os.path.basename(imagePath)
	category = y[index]
	location = "Cam " + imageName[len(category):-4]
	if category == "trash":
		import emailNotification as emailSender
		import smsNotification as smsSender
		emailSender.sendEmailNotification('siva.nulakani@gmail.com', category, location, imageName, imagePath)
		smsSender.sendSmsNotification(category, location)
		print("Alert sent")
	#learn.data.test_ds[index][0]
	print('Image identified as ' + category)