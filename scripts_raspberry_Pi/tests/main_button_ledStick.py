import time
import gateway_button_ledStick as gateway

print("Initialisation de l'application")
passerelleObject = gateway.Gateway()
print("Lancement de l'application")

while True:
	print("---------------")
	passerelleObject.inputUpdate()
	passerelleObject.inputProcessing()
	passerelleObject.graph()
	passerelleObject.outputProcessing()
	passerelleObject.outputUpdate()

	time.sleep(1.0)