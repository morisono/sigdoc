function SendPathToExternalAPI($PathToSend) {
    # 送信先APIのエンドポイント
    $apiEndpoint = "https://example.com/api/path"

    # 送信するデータ
    $postData = @{
        Path = $PathToSend
    } | ConvertTo-Json

    try {
        # POSTリクエストを送信
        $response = Invoke-RestMethod -Uri $apiEndpoint -Method Post -Body $postData -ContentType "application/json"
        
        # レスポンスの確認
        Write-Host "Path sent successfully. Response: $response"
    } catch {
        # エラー処理
        Write-Host "Error occurred while sending the path: $_"
    }
}

# パスを取得し、外部APIに送信
function GetAndSendPaths($CurrentTarget, $Indent){
    $CurrentName = Split-Path -Leaf $CurrentTarget

    # パスの形式を調整
    if($CurrentTarget.EndsWith("\"))
    {
        $PathToSend = "$(Get-Location)" + $Indent + $CurrentName
    } else {
        $PathToSend = "$(Get-Location)" + $Indent + $CurrentName + "\"
    }
    
    # 外部APIにパスを送信
    SendPathToExternalAPI $PathToSend

    # ディレクトリの場合は再帰的に処理を行う
    if(Test-Path $CurrentTarget -PathType Container) {
        $Children = Get-ChildItem -Path $CurrentTarget -Force -Directory | Select-Object -ExpandProperty FullName
        foreach ($Child in $Children) {
            GetAndSendPaths $Child ($Indent + $CurrentName)
        }

        # ディレクトリ内のファイルも再帰的に処理
        $Files = Get-ChildItem -Path $CurrentTarget -Force -File | Select-Object -ExpandProperty FullName
        foreach ($File in $Files) {
            GetAndSendPaths $File ($Indent + $CurrentName)
        }
    }
}

# メイン処理
GetAndSendPaths $Path ""

Write-Host "All paths sent."
