# emu_archive
HTML based front end for video game console emulators

It uses WebSockets to connect the HTML front-end, to a Go back-end. The 
back-end manages the emulators and game files. The project was written in 
Python, but is slowly being converted to Go. For now, Python is required to 
run some of the sub modules.


Install python 3.X
-----
http://www.python.org

Install 32 bit MinGW
-----
http://sourceforge.net/projects/mingw/?source=typ_redirect
Install base and gcc-c++ packages

Install 32 bit Go
-----
https://storage.googleapis.com/golang/go1.4.2.windows-386.msi

Set GOPATH environmental variable
-----
C:/GO_WORKSPACE/

Install WebSockets Module
-----
~~~bash
go get golang.org/x/net/websocket
~~~

Checkout the code
-----
~~~bash
cd C:/GO_WORKSPACE/src
git clone http://github.com/workhorsy/emu_archive
cd emu_archive
git clone http://github.com/workhorsy/emu_archive_meta_data games
~~~


Build and run the exe
-----
~~~bash
cd C:/GO_WORKSPACE/src/emu_archive
go run server/generate/generate_include_files.go
go run server/server.go
~~~

Visit this url
~~~bash
http://localhost:9090
~~~
