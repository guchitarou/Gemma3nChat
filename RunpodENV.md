# 環境構築手順書

## 前提条件
私は個人なので主に下記の理由からRunPodを利用することにしました。

* GPUは非常に高額（例:RTX 4090などは100万円ほどする）
* 電力消費が家庭のコンセントからではギリ、もしくは足りない。

## Runpodとは？
Runpodは、GPUサーバーを手軽に借りられるクラウドサービス。機械学習やAI開発向けに、必要なときだけ高速GPU環境を使えるのが特徴。低コストで柔軟に使えるため、個人開発から研究用途まで幅広く使われているようです。Runpodの公式サイトは下記です。

[RunPod公式サイト](https://www.runpod.io/?pscd=get.runpod.io&ps_partner_key=NDNiMzk4ODE0NWMy&sid=1-b-77e6225cf34710fedd374b91da17556c&msclkid=77e6225cf34710fedd374b91da17556c&ps_xid=7A1xTSxKItZDze&gsxid=7A1xTSxKItZDze&gspk=NDNiMzk4ODE0NWMy)

## RunPodの設定
サイトを開いてSign Upします。

![参考画像](desc_img/runpodTitle2026-04-01232458.png)

サインアップ後、利用料を前もって払います。今回はRTX 4090を使うので大体3000円くらい入れておけば大丈夫だと思われます。Billingをクリックして、課金をしてください。※下記画像1~3を参考に

![参考画像](desc_img/runpod_mypage.png)


## 使用の流れ
簡単な使用の流れは下記。

### 1. ssh keyの設定
自身のPC上で下記のコマンドを実施してpubファイルを作成。
```
ssh-keygen -t ed25519 -C "your_email@example.com"
```
上記のコマンドを実施すると下記のようなフォルダ内にpubファイルが作られる。
```
例
C:\Users\xxxx\id_ed25519.pub
```
上のファイルをメモ帳で開き中身をコピーする。
```                                          
ssh-ed25519 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+xxxxxxxxxxxxxxxxxxxxx+xxxxxxxxxxxxx xxxxxxxxxx@gmail.com
```

コピーした内容をRunpodのページで登録する。[Settings]->[SSH public keys]でページを開き先ほどコピーした.pubファイルの中身をコピペする。

![参考画像](desc_img/ssh_settings.png)


### 2. GPUやテンプレートを選ぶ
![参考画像](desc_img/t1.png)


### 3. ストレージ環境を選ぶ
![参考画像](desc_img/t2.png)

### 4. Podを起動
![参考画像](desc_img/t3.png)

### 5. SSH接続情報をメモ
「Direct TCP ports」をメモする。

![参考画像](desc_img/run_pod_acsess.png)

メモする内容例
```
ssh root@111.111.11.11 -p 22222 -i ~/.ssh/id_ed33333
```

ここで一旦Runpodのほうの設定終了。

# 使用方法
使用方法は、下記の2つある。自分の好きなほうを使ってください。
* JupyterLabを利用して使用 (一番簡単)
* VscodeでSSH接続して使用 (少しめんどう)


# JupyterLabを利用して使用 
Vscodeを使いたくない場合はJupyterLabだと何も設定しなくてもすぐ使える。

[Pods] -> [立ち上げたPodをクリック] -> [JupyterLabをクリック]


![参考画像](desc_img/JupyterLab.png)

下記のような画面が表示されれば成功。

![参考画像](desc_img/jupyterlab_web_screen.png)

# VscodeでSSH接続して使用
※前提条件として下記のようなRemoteDevelopmentのようなssh接続ができる環境があること。

![参考画像](desc_img/ssh_tools.png)

### config 設定
config fileを開いてssh接続設定を記述する。
```
Host RunPodGemma3n
    HostName 111.111.11.11
    User root
    IdentityFile ~/.ssh/id_ed33333
    Port 22222
    IdentitiesOnly yes
```
### Vscodeで開く
黄色丸からアクセスして接続する。
※ 下記はあくまで例です。各自読み替えてください。

![参考画像](desc_img/connect.png)

### 接続確認
接続完了するとターミナルに下記のような表示が出る。
※　Runpodと表示されていればOK

![参考画像](desc_img/connect_check.png)










