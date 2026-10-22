import subprocess
import sys
from pathlib import Path

subprocess.run(
    [
        sys.executable, "-m", "torch.distributed.run",
        "--nproc_per_node", "1",
        "example_chat_completion.py",
        "--ckpt_dir", "llama-2-7b-chat/",
        "--tokenizer_path", "llama-2-7b-chat/tokenizer.model",
        "--max_seq_len", "512",
        "--max_batch_size", "6",
        "--max_gen_len", "128",
    ],
    cwd=Path(__file__).resolve().parent,
    check=True,
)
