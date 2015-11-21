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
                            "command": ["sudo apt-get -y install gcc build-essential python-dev python3-dev python-numpy python3-numpy python-scipy python3-scipy\
                             python-dateutil python-docutils python-feedparser python-gdata python-jinja2 python-ldap python-libxslt1 python-lxml python-mako \
                             python-mock python-openid python-psycopg2 python-psutil python-pybabel python-pychart python-pydot python-pyparsing python-reportlab\
                              python-simplejson python-tz python-unittest2 python-vatnumber python-vobject python-webdav python-werkzeug python-xlwt python-yaml\
                               python-zsi python3-dateutil python3-docutils python3-feedparser python3-jinja2 python3-lxml python3-mako python3-mock python3-psycopg2\
                                python3-psutil python3-pyparsing python3-reportlab python3-simplejson python3-tz python3-werkzeug python3-yaml","yes w | pip  install https://www.djangoproject.com/download/1.9rc1/tarball/ requests scrapy mitmproxy pyramid scikit-learn beautifulsoup4"]
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
                            "command": ["sudo apt-get -y install git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev ruby-full"]
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
                                    "command": ["sudo apt-get -y install default-jdk"]
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
                                    "command": ["sudo add-apt-repository -y ppa:webupd8team/java","sudo apt-get update","sudo apt-get -y install oracle-java8-installer"]
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
                        "command": ["sudo apt-get -y install git-core "]
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
                            "command": ["sudo apt-get -y install php5-cli "]
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
                            "command": ["sudo apt-get -y install perl "]
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
                            "command": ["sudo apt-get -y install nodejs npm "]
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
                            "command": ["sudo apt-get -y install gcc g++ "]
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
                            "command": ["sudo apt-get -y install golang-stable "]
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
                            "command": ["sudo apt-get -y install  haskell-platform"]
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
                            "command": ["sudo apt-get -y install lua5.2"]
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
                            "command": ["sudo apt-get -y install scala"]
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
                            "command": ["sudo apt-get -y install r-base"]
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
                            "command": ["sudo apt-get -y install curl" , "curl -sSf https://static.rust-lang.org/rustup.sh | sh"]
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
                            "command": ["sudo apt-get -y install arduino arduino-core"]
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
                            "command": ["sudo apt-get -y install mysql-server", "sudo mysql_install_db "," sudo /usr/bin/mysql_secure_installation"]
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
                            "command": ["sudo apt-get -y install postgresql postgresql-contrib"]
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
                            "command": ["sudo apt-get install -y python-software-properties","sudo add-apt-repository -y ppa:rwky/redis","sudo apt-get update","sudo apt-get -y install redis-server"]
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
                            "command": ["wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key -y add -", "echo 'deb http://debian.neo4j.org/repo stable/' > /etc/apt/sources.list.d/neo4j.list","sudo apt-get update","sudo apt-get -y install neo4j"]
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