$env:TORCH_COMPILE_DISABLE="1"; lmdeploy chat F:\my_model --backend pytorch --eager-mode

$env:TORCH_COMPILE_DISABLE = "1"; lmdeploy serve api_server F:\my_model --backend pytorch --eager-mode --server-port 23333

lmdeploy serve api_server F:\my_model --backend pytorch --server-port 23333

$env:TORCH_COMPILE_DISABLE = "1"; lmdeploy serve api_server D:\model_cache\modelscope\models\Qwen\Qwen2***5-1***5B-Instruct --backend pytorch --eager-mode --server-port 23333

环境
pip install torch==2.7.1 torchvision==0.22.1 --index-url https://download.pytorch.org/whl/cu126
Python 3.10.19

-
