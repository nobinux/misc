https://nodejs.org/download/からnode.exeをダウンロードし任意のフォルダ（例：nodejs）内に保存するだけ。
バージョンがいろいろあるが、動けばいい素人なので悩まずにhttps://nodejs.org/download/release/latest-v5.x/win-x64/からダウンロードしてきた。

npmの入手
https://github.com/npm/npm/releasesから最新版のzipをダウンロード。
node.exeと同じ場所（nodejs）内にnode_modulesというフォルダを作成し、ダウンロードしたnpmのzipをnodejs/node_modules/内へ解凍。
npm-バージョン名というフォルダ名になるので、npmへリネーム。
nodejs/node_modules/npm/bin内にあるnpmとnpm.cmdをnodejsへコピー。
以下の内容をnodejs/node_modules/npm/npmrcとして保存。
'''(npmrc)
prefix=${APPDATA}\npm
'''

パスの設定
nodejsと%AppData%/npmへパスを通す。

npm proxy config
https://qiita.com/LightSpeedC/items/b273735e909bd381bcf1

npmの環境変数に設定する。

https://docs.npmjs.com/misc/config#proxy
https://docs.npmjs.com/misc/config#https-proxy

proxy と https-proxy だけでだめなら registry を設定している。
Windows では registry も https から http に変更しないと動かない。

Windows では以下の様なBAT/CMDスクリプトファイルを用意すると良い。

call npm -g config set proxy http://proxyserver:8080
call npm -g config set https-proxy http://proxyserver:8080
call npm -g config set registry http://registry.npmjs.org/
call npm config list
pause



## ref: npm を使用した CLI のインストール
 https://developer.salesforce.com/docs/atlas.ja-jp.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm

node --version

Node.js の長期サポート (LTS) バージョンがコンピュータにインストールされていることを確認します。LTS バージョン番号を見つけるには、https://nodejs.org/en/download/ を確認してください。使用しているバージョン番号を確認するには、次のコマンドを実行します。

node --version

次のコマンドを実行します。

npm install sfdx-cli --global
