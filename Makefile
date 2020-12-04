build:
	sudo docker build -t codeinjection .

run:
	sudo docker run \
	-v /tmp/.X11-unix:/tmp/.X11-unix  \
	-v $(shell pwd):/usr/src/app \
	-e DISPLAY=${DISPLAY} \
	-e  QT_X11_NO_MITSHM=0 \
	-it codeinjection python main.py

shell:
	sudo docker run -it -v $(shell pwd):/usr/src/app codeinjection bash


