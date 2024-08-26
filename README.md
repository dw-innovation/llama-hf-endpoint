## HF Endpoints
This repository contains examples of handlers, requirements.txt to host a customized Llama.

## Installation
Create a conda environment if you don't have one.
```shell
conda create --name hf_inference python=3.10
```

## Development
Follow the instructions at https://www.philschmid.de/custom-inference-handler

## Testing
CUDA_VISIBLE_DEVICES="1" python -m test_handler
