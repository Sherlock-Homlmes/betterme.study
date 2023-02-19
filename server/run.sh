#! /bin/bash

##### SETUP
linebreak=$'\n'
red="\e[31m"
green="\e[32m"
endcolor="\e[0m"

# docker_alias = []
# docker_command = []

##### INPUT

args=("$@")

### This is for all project
if [[ ${args[0]} == "up" ]]; then
    echo "Starting docker..."
    output=$(eval "docker compose up -d")
    echo "$output"
    eval "cd backend"
    output=$(eval "docker compose up -d")
    echo "$output"
    eval "cd ..${linebreak}cd frontend"
    output=$(eval "docker compose up -d")

elif [[ ${args[0]} == "down" ]]; then
    echo "Stopping docker..."
    output=$(eval "docker compose down")
    echo "$output"
    eval "cd backend"
    output=$(eval "docker compose down")
    echo "$output"
    eval "cd ..${linebreak}cd frontend"
    output=$(eval "docker compose down")

elif [[ ${args[0]} == "createsuperuser" ]]; then
    if [[ "${args[1]}" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$ ]]
    then
        echo "Starting database..."
        eval "cd backend $linebreak docker compose up db -d"
        output=$(eval "docker compose exec backend python database/postgres/peewee/superuser.py ${args[1]}")
    else
        output="Email address ${args[1]} is invalid."
        color="$red"
    fi

### This is for backend command
elif [[ ${args[0]} == "be" ]]; then
    eval "cd backend"
    if [[ ${args[1]} == "docker" ]]; then
        if [[ ${args[2]} == "up" ]]; then
            if [[ ${args[3]} ]]; then
                output=$(eval "docker compose up ${args[3]} -d")
            else
                output=$(eval "docker compose up -d")
            fi
        elif [[ ${args[2]} == "down" ]]; then
            if [[ ${args[3]} ]]; then
                output=$(eval "docker compose stop ${args[3]}")
            else
                output=$(eval "docker compose down")
            fi
        elif [[ ${args[2]} == "logs" ]]; then
            output=$(eval "docker compose logs ${args[3]} -f tails=50")
        elif [[ ${args[2]} == "build" ]]; then
            output=$(eval "sudo docker compose build")
        elif [[ ${args[2]} == "buildup" ]]; then
            output=$(eval "sudo docker compose up -d --build")
        else
            output="Unknow command '${args[2]}'"
            color="$red"
        fi

    elif [[ ${args[1]} == "db" ]]; then
        if [[ ${args[2]} == "migrate" ]]; then
            output=$(eval "docker compose exec backend alembic revision --autogenerate -m "migrate"")
        elif [[ ${args[2]} == "downgrate" ]]; then
            output=$(eval "docker compose exec backend alembic downgrade -1")        
        elif [[ ${args[2]} == "makemigrations" ]]; then
            output=$(eval "docker compose exec backend alembic upgrade head")
        elif [[ ${args[2]} == "resetmigrations" ]]; then
            eval "cd migrations"
            eval "sudo rm -rf versions"
            eval "sudo mkdir versions"
            output="Removed all migrations.${linebreak}Now remove 'alembic_version' table in postgres"
            color="$green"
        elif [[ ${args[2]} == "sampledata" ]]; then
            echo "Starting database..."
            eval "docker compose exec backend python database/sample_data.py"
            output="Done"
            color="$green"
        else
            output="Unknow command '${args[2]}'"
            color="$red"
        fi

    elif [[ ${args[1]} == "test" ]]; then
        output=$(eval "docker compose exec backend pytest --cov blackjack --cov-report html")

    else
        output="Unknow command '${args[1]}'"
        color="$red"
    fi

### This is for frontend command
elif [[ ${args[0]} == "fe" ]]; then
    eval "cd frontend"
    if [[ ${args[1]} == "docker" ]]; then
        if [[ ${args[2]} == "up" ]]; then
            output=$(eval "docker compose up -d")
        elif [[ ${args[2]} == "down" ]]; then
            output=$(eval "docker compose down")
        elif [[ ${args[2]} == "logs" ]]; then
            output=$(eval "docker compose logs ${args[3]} -f tails=50")
        elif [[ ${args[2]} == "build" ]]; then
            output=$(eval "sudo docker compose build")
        elif [[ ${args[2]} == "buildup" ]]; then
            output=$(eval "sudo docker compose up -d --build")
        else
            output="Unknow command '${args[2]}'"
            color="$red"
        fi
    fi

### This is for install tools
elif [[ ${args[0]} == "install" ]]; then
    if [[ ${args[1]} == "docker" ]]; then
        echo $(eval "sudo apt-get update 
            ${linebreak}sudo apt-get install \
            ca-certificates \
            curl \
            gnupg \
            lsb-release 
            ${linebreak}sudo mkdir -p /etc/apt/keyrings
            ${linebreak}curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
            ${linebreak}echo \
                "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
                $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
            ${linebreak}sudo apt-get update
            ${linebreak}sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
        ")
        output="Install docker success"
        color="$green"
    # elif [[ ${args[1]} == "python" ]]; then
    # elif [[ ${args[1]} == "npm" ]]; then
    # elif [[ ${args[1]} == "poetry" ]]; then
    # elif [[ ${args[1]} == "vue" ]]; then
    # elif [[ ${args[1]} == "redis" ]]; then
    # elif [[ ${args[1]} == "kubernetes" ]]; then
    else
        output="Unknow service '${args[0]}'"
        color="$red"
    fi

### This is for other tools/modules

# see all active port
elif [[ ${args[0]} == "aport" ]]; then
    output=$(eval "sudo lsof -i -P -n | grep LISTEN")
    color="$green"

# kill active port
elif [[ ${args[0]} == "kill" ]]; then
    if [[ ${args[1]} ]]; then
        output=$(eval "sudo kill -9 $(sudo lsof -t -i:${args[1]})")
    else
        output=$"Please confirm port to kill.${linebreak}Example: 'kill 8000'"
        color="$red"
    fi

else
    output="Unknow command '${args[0]}'"
    color="$red"
fi

if [[ $color ]]; then
    echo -e "$color$output$endcolor"
else
    echo "$output"
fi