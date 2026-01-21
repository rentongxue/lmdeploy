# LMDeploy 聊天启动脚本
# 使用方法: .\start_chat.ps1

$env:TORCH_COMPILE_DISABLE = "1"

lmdeploy chat F:\my_model --backend pytorch --eager-mode
