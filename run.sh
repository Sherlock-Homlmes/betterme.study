#! /bin/bash

##### SETUP
linebreak=$'\n'
red="\e[31m"
green="\e[32m"
endcolor="\e[0m"
# link=$(eval "readlink -f run.sh")
# arr=(`echo $link | tr '/' ' '`)
# echo "${#arr[@]}"
# link=${link#"/${arr[0]}"}
# link=${link#"/${arr[1]}"}
# link=${link%"/run.sh"}
# eval "cd ~$link"
# eval "cd ~/Documents/otani_proj"

# docker_alias = []
# docker_command = []

##### INPUT

args=("$@")

### This is for all project
if [[ ${args[0]} == "up" ]]; then
    echo "Starting docker..."
    # output=$(eval "docker compose up -d")
    # echo "$output"
    eval "cd server"
    output=$(eval "docker compose up -d")
    echo "$output"
    eval "cd ..${linebreak}cd client"
    output=$(eval "docker compose up -d")

elif [[ ${args[0]} == "down" ]]; then
    echo "Stopping docker..."
    # output=$(eval "docker compose down")
    # echo "$output"
    eval "cd server"
    output=$(eval "docker compose down")
    echo "$output"
    eval "cd ..${linebreak}cd client"
    output=$(eval "docker compose down")

### This is for install tools
elif [[ ${args[0]} == "install" ]]; then
    if [[ ${args[1]} == "docker" ]]; then
        echo "Installing Docker Desktop. Please wait..."

        echo "Step 1/3: Installing neccesary tools"
        echo $(eval "sudo apt-get update 
            ${linebreak}sudo apt-get install \
            ca-certificates \
            curl \
            gnupg \
            lsb-release -y 
        ")

        echo "Step 2/3: Setting up Docker's package repository"
        ubuntu_codename=$( \
           (grep DISTRIB_CODENAME /etc/upstream-release/lsb-release || \
            grep DISTRIB_CODENAME /etc/lsb-release) 2>/dev/null | \
           cut -d'=' -f2 )
        echo $(eval "sudo mkdir -p /etc/apt/keyrings
            ${linebreak}curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
            ${linebreak}echo \
                "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
                $ubuntu_codename stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        ")

        echo "Step 3/3: Installing Docker Engine"
        echo $(eval "sudo apt-get update
            ${linebreak}sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y
        ")

        output="Docker Desktop successfully installed"
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