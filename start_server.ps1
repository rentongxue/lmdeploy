# LMDeploy API 服务启动脚本
# 使用方法: .\start_server.ps1
# API 地址: http://localhost:23333

$env:TORCH_COMPILE_DISABLE = "1"

lmdeploy serve api_server F:\my_model --backend pytorch --eager-mode --server-port 23333
