menu_data = {
    "title": "Ubuntu Stater Kit",
    "type": "menu",
    "subtitle": "Please select an option...",
    "options": 
    [
        {
            "title": "Languages",
            "type": "menu",
            "subtitle": "select the once u want to install",
            "options": 
            [
                {
                    "title": "Python modules(Recommended)",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install gcc build-essential python-dev python3-dev python-numpy python3-numpy python-scipy python3-scipy python-dateutil python-docutils python-feedparser python-gdata python-jinja2 python-ldap python-libxslt1 python-lxml python-mako python-mock python-openid python-psycopg2 python-psutil mitmproxy python-pybabel python-pychart python-pydot python-pyparsing python-reportlab python-simplejson python-tz python-unittest2 python-vatnumber python-vobject python-webdav python-werkzeug python-xlwt python-yaml python-zsi python3-dateutil python3-docutils python3-feedparser python3-jinja2 python3-lxml python3-mako python3-mock python3-psycopg2 python3-psutil python3-pyparsing python3-reportlab python3-simplejson python3-tz python3-werkzeug python3-yaml"]
                        }
                    ]
                },
                {
                    "title": "Ruby",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev ruby-full"]
                        }
                    ]
                },
                {
                    "title": "Java",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "Open JDK",
                            "type": "menu",
                            "subtitle": "Press Yes if u want to install",
                            "options": 
                            [
                                {
                                    "title": "YES",
                                    "type": "command",
                                    "command": ["sudo apt-get install default-jdk"]
                                }
                            ]
                        },
                        {
                            "title": "Oracal JDK",
                            "type": "menu",
                            "subtitle": "Press Yes if u want to install",
                            "options": 
                            [
                                {
                                    "title": "YES",
                                    "type": "command",
                                    "command": ["sudo add-apt-repository -y ppa:webupd8team/java","sudo apt-get update","sudo apt-get install oracle-java8-installer"]
                                }
                            ]
                        }
                    ]
                },
                {
                    "title": "GIT(no need if you have installed ruby)",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                        "command": ["sudo apt-get install git-core "]
                        }
                    ]
                },
                {
                    "title": "Php",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install php5-cli "]
                        }
                    ]
                },
                {
                    "title": "Perl",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install perl "]
                        }
                    ]
                },
                {
                    "title": "NodeJS",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install nodejs npm "]
                        }
                    ]
                },
                {
                    "title": "C++ and C",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install gcc g++ "]
                        }
                    ]
                },
                {
                    "title": "GO",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install golang-stable "]
                        }
                    ]
                },
                {
                    "title": "Haskell",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install  haskell-platform"]
                        }
                    ]
                },
                {
                    "title": "Lua",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install lua5.2"]
                        }
                    ]
                },
                {
                    "title": "Scala",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install scala"]
                        }
                    ]
                },
                {
                    "title": "R Language",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install r-base"]
                        }
                    ]
                },
                {
                    "title": "Rust Language",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install curl" , "curl -sSf https://static.rust-lang.org/rustup.sh | sh"]
                        }
                    ]
                },
                {
                    "title": "Arduino",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install arduino arduino-core"]
                        }
                    ]
                }
            ]
        },
        {
            "title": "Databases",
            "type": "menu",
            "subtitle": "select the once u want to install",
            "options": 
            [
                {
                    "title": "MySQL",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install mysql-server", "sudo mysql_install_db "," sudo /usr/bin/mysql_secure_installation"]
                        }
                    ]
                },
                {
                    "title": "postgresql",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install postgresql postgresql-contrib"]
                        }
                    ]
                },
                {
                    "title": "MongoDB",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10"," echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list","sudo apt-get update","sudo apt-get install -y mongodb-org"]
                        }
                    ]
                },
                {
                    "title": "Redis",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install -y python-software-properties","sudo add-apt-repository -y ppa:rwky/redis","sudo apt-get update","sudo apt-get install redis-server"]
                        }
                    ]
                },
                {
                    "title": "Neo4j",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key add -", "echo 'deb http://debian.neo4j.org/repo stable/' > /etc/apt/sources.list.d/neo4j.list","sudo apt-get update","sudo apt-get install neo4j"]
                        }
                    ]
                }
            ]
        },
        {
            "title": "Software",
            "type": "menu",
            "subtitle": "select the once u want to install",
            "options": 
            [
                {
                    "title": "Chrome",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -", "sudo sh -c 'echo \"deb http://dl.google.com/linux/chrome/deb/ stable main\" >> /etc/apt/sources.list.d/google-chrome.list'","sudo apt-get update","sudo apt-get install google-chrome-stable"]
                        }
                    ]
                },
                {
                    "title": "IntelliJ IDEA(needs JAVA to work)",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo wget -O /usr/intellij.tar.gz http://download.jetbrains.com/idea/ideaIC-15.0.1.tar.gz","sudo tar xfz /usr/intellij.tar.gz","sudo cd idea*/bin","sudo ./idea.sh","sudo rm /usr/intellij.tar.gz"]
                        }
                    ]
                },
                {
                    "title": "VLC",
                    "type": "menu",
                    "subtitle": "Press Yes if u want to install",
                    "options": 
                    [
                        {
                            "title": "YES",
                            "type": "command",
                            "command": ["sudo apt-get install vlc"]
                        }
                    ]
                }
            ]
        }   
    ]
}
no_internet_menu={
    "title": "Ubuntu Stater Kit",
    "type": "menu",
    "subtitle": "No Network connections...",
    "options": [
        {
            "title": "Try again",
            "type": "command",
            "command": "tryagain"
        }
    ]
}