# Windowsが起動するまでのプロセス

Windowsの起動プロセスは、コンピュータの電源を入れてから実際にWindowsのデスクトップが表示されるまでに、複数の段階を経ています。以下に、その主要なステップを専門的に解説します。

1. **BIOS/UEFI**:
   - コンピュータの電源が入ると、最初にBIOS（またはUEFI）が実行されます。BIOSは基本的なハードウェアの初期化を行い、POST（Power On Self Test）を実行します。具体的にはBIOS自体の整合性チェックやメインメモリの確認(古いPCだと確認処理を直接見れたりします)、デバイスの検出・初期化など。そしてブートするデバイスを特定/ディスクの先頭にあるMBRを読み取ります。

2. **ブートデバイスの選択**:
   - BIOS/UEFIは、ブートデバイスのリストを検索し、最初のブートデバイス（通常はハードディスク）を選択します。

3. **MBR (Master Boot Record) の読み込み**:
   - 選択されたブートデバイスから、MBRが読み込まれます。MBRにはブートローダーへのポインタが含まれており、コンピュータの起動プロセスはここから始まります。

4. **ブートマネージャー (Boot Manager)**:
   - MBRから読み込まれたブートマネージャーは、利用可能なオペレーティングシステム（通常はWindows）を検出し、ユーザーがどのOSを起動するか選択するオプションを提供します。

5. **OSローダー (OS Loader)**:
   - 選択されたWindowsのエントリが存在する場合、ブートマネージャーはOSローダー（通常は`%SystemRoot%\system32\winload.exe`）を起動します。OSローダーは、Windowsの起動処理を制御し、カーネルを読み込みます。このファイルがあるパーティションは通常ドライブレターが割り当てられていないだけなので、ディスクの管理から割り当てれば、エクスプローラーで表示できます。

6. **NTカーネル (NT Kernel)**:
   - NTカーネル（ntoskrnl.exe）はWindowsの中核であり、メモリの管理やデバイスの制御などの基本的な機能を提供します。NTカーネルが読み込まれると、Windowsのロゴが画面に表示されます。カーネルの読み込みに必要な最低限のドライバー(もはやカーネルモードドライバーよりも本当の意味でシステムに近い)を読み込み、カーネルをメモリにロードします。これ以降でWindows内部に致命的なエラーが発生した場合には、BSODが表示されるようになります。逆にこれ以前のエラー、例えばBitLockerが複合化できない場合は若干濃い青の偽BSODが表示されます。

7. **KMDF / smss.exe**:
   - カーネルモードドライバフレームワーク（KMDF）などのドライバや、システムマネージメントモード（SMM）を使用する場合、これらの要素が読み込まれます。また、セッションマネージャサブシステム（smss.exe）も起動され、セッションの開始を処理します。この段階でようやくユーザーセッションが準備され、またデバイスのノードと呼ばれるものが構築されます。

8. **win32k.sys**:
   - グラフィカルなユーザーインターフェースを提供するためのWindowsのGDI (Graphical Device Interface) ドライバであるwin32k.sysが読み込まれます。この段階で、画面が一時的に暗くなることがあります。

9. **Winlogon**:
   - Winlogonプロセスが起動され、ユーザー認証やセッションの開始を担当します。画面が青くなり、ユーザーがログインするための画面が表示されます。なお、ログイン時にCtrl+Alt+Deleteの押下を求めることができますが(2000以前やServerは必須)、これはOSのみ認識できる操作であるため、暗黙的に"本物のログイン画面"の証明となります。

10. **Windows Explorer**:
    - ユーザーが正常にログインすると、Windows Explorerが起動され、デスクトップやタスクバーなどのグラフィカルなユーザーインターフェースが表示されます。これで、Windowsの起動プロセスが完了し、ユーザーがアプリケーションを実行できる状態になります。

以上が、Windowsが起動するまでの主要なステップです。このプロセスは、コンピュータのハードウェアや設定によって異なる場合がありますが、一般的な流れは大きく変わりません。
