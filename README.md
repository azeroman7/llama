# Diffusion Model
This repository contains implementations of llama

## Git clone
```bash
git clone https://github.com/azeroman7/llama.git
or 
git clone git@github.com:azeroman7/llama.git
```

## Install Environment via Anaconda (Recommended)
```bash
conda create -n llama python=3.11 -y
conda activate llama

cd llama
python -m pip install -e .
python -m pip install --upgrade huggingface_hub

#hf auth login
  # Open this URL in your browser: https://hf.co/oauth/device
  # And enter the code: ???   (90NN-85CB)

hf download meta-llama/Llama-2-7b-chat   consolidated.00.pth params.json tokenizer.model   --local-dir llama-2-7b-chat
python -m pip install   torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1   --index-url https://download.pytorch.org/whl/cu118
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.ones(1, device='cuda'))"
```

## Run script --> see outputs folder for results
```bash
python run_llama.py
```
