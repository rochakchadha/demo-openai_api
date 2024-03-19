#!/bin/bash

#source /datadrive/miniconda3/etc/profile.d/conda.sh


# Check if specific screen sessions exist
if screen -ls | grep -q -E "(openai-server|llama2-7b-model|fastchat_server_controller)"; then
    echo "One or more of the specified screen sessions already exist. Exiting."
    exit 1
fi

# Start Screen sessions and execute commands in each
screen -S fastchat_server_controller -dm bash -c "sleep 2; cd /datadrive/FastChat/; python3 -m fastchat.serve.controller"
sleep 30
screen -S llama2-7b-model -dm bash -c "sleep 2; cd /datadrive/FastChat/; python3 -m fastchat.serve.model_worker --model-path /datadrive/models/Llama-2-7b-chat-hf --device cpu --port 21002 --worker http://localhost:21002"
sleep 180
screen -S Mistral-7b-model -dm bash -c "sleep 2; cd /datadrive/FastChat/; python3 -m fastchat.serve.model_worker --model-path /datadrive/models/Mistral-7B-Instruct-v0.2 --device cpu --port 21003 --worker http://localhost:21003"
sleep 240

screen -S openai-server -dm bash -c "sleep 2; cd /datadrive/FastChat/; python3 -m fastchat.serve.openai_api_server --host 0.0.0.0 --port 9000"


