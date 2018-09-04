# DEV450 on 10-15 May

## $2-3 Object and Items

### 項目のアクセス許可

1. オブジェクトへの参照権限がまず必要

2. 項目レベルセキュリティの設定で参照できることがさらに必要

### 項目レベルセキュリティ

a. スキーマビルダーで作成した場合

- デフォルトで全プロファイルが参照・編集可能

- 参照のみをチェックONすることで参照のみに限定可能

- 参照付加とするためには、デフォルトでONとなっている参照可能のチェックをOFFに

  - ただしページレイアウトには自動で追加されないため、適宜手動で追加する必要あり

b. 設定ページから追加した場合

- ページレイアウトへの追加が自動でなされる

### Relationship

A. lookup relationship

- 参照先のレコードを削除した後には参照項目は空になる
　-> lookup項目の設定時に空になるように設定した場合

B. m/d: Master/Detail relationship

- 参照先の親（主）レコードを削除した後には、参照元の子オブジェクトのレコードも削除される

- 子（従）レコードの共有設定が標準の参照・編集・削除ではなく、親（主）レコードの設定が引き継がれる

## $4 Apex

大文字小文字を区別しない\!

- カスタム項目の参照関係オブジェクトの指定
  - XXXXX__c : 参照項目のidを指す
  - XXXXX__r : 参照項目のレコードを指す

## $6 SOQL

- $6-2 親-子カスタムリレーションを持つ結合クエリの注意事項

`SELECT Name, (SELECT Name FROM Courses__r) FROM Certification__c WHERE Id IN (SELECT Certification__c from Course__c)`

>     比較演算子 - IN を使用した準結合とNOT IN を使用した反結合

- リレーションクエリを評価する準結合または反結合 - 主クエリの制限:

    左のオペランドは、1 つの ID (主キー) 項目または参照 (外部キー) 項目をクエリする必要があります。サ
ブクエリで選択した項目は、参照項目にできます。
左のオペランドにはリレーションを使用できません。たとえば、WHERE Account.Id IN (...)は無効。

- 部分処理（コミット） - DML Statements vs. Database Class Methods

    Databaseメソッドで第二引数に`False`を指定すれば部分処理可に

    `Database.insert(contacts, false);`

- p.209

  - DML行数制限（10,000行）を回避するためにForループを使用してループの外でDML処理

  - リスト反復変数（200行ずつ処理）を使用してヒープ制限を回避

## $7 Trigger

- p.215-217 コードベースで開発する必要があるケース

 宣言ベースの入力規則などでは関連のない「休日」オブジェクトを参照できない

- p.218 before / after
 リレーション項目を指定するためにはIDが必要　＝>　after trigger

## $9 Apex

- with sharing : 共有モデルを適用

  default : without sharing
  明示的に`with sharing`を指定して、ユーザのレコードに対するアクセス権に従った制御としない限りは、全レコードが取得される

## $10 transaction

## $11 Test

- keyword : @isTest

  `testMethod キーワードまたは@isTest アノテーション`とApexガイドにあるが、`testMethod キーワード`は非推奨

- @testSetup

  testMethodが呼び出される前に必ず実行されるメソッド、テストメソッド共通のデータ格納や初期化処理の実装に向く

- (FYI) @isTest(seeAllData = true)

  テストデータが環境依存してしまうため、望ましくない

- testMethodは並列で実行される

  ![Apex test option on UI](\img/2018-05-14-10-50-14.png)

  UI設定メニューのApexテスト実行からオプションを開き、「並列 Apex テストを無効化」をチェックONにすると順次実行可

- Guideline

  - テストコードをハードコードしない

    -> プロファイルやユーザなどをID指定する際は、一度SelectしてIDを取得してから利用するなど

  - 200件を超えるデータを読み込む可能性がある場合テストデータ読み込み時の動作検証

  - 静的リソースなどテストデータをコードと共にFull/本番環境へ移行

## $13 Limits

- System.LimitException: Too many SOQL queries: 101

  解決例１:リスト反復変数にループ外でデータセットにクエリ結果を格納してループ内のクエリをなくす

  ```Java
  for (List<Course_Delivery__c> cds : [SELECT Id, Course__c, Status__c,
  (SELECT Status__c FROM Course_Attendees__r
   WHERE Status__c = :ENROLLED)
   FROM Course_Delivery__c
   WHERE Course__c IN :courseIds AND Status__c = :SCHEDULED]) {
     ...
   }
  ```

  ![SOQl limitation screen](\img/2018-05-14-12-59-33.png)

- trigger

  - 200レコードごとのバッチ処理

  - Apex一括処理の各トランザクションが実行されるのは並列でなく直列（順序）

  - 処理されるレコードの順序は予測不可

  - see Trigger Frameworks and Apex Trigger Best Practices
   @developer Technical Library
  <https://developer.salesforce.com/page/Trigger_Frameworks_and_Apex_Trigger_Best_Practices>

## $16 VisualForce Model & View Controler

- <apex:pageBlockTable> vs <apex:dataTable>

  |tag|pageBlockTable|dataTable|
  |---|------|------|
  |detail|designed and simple table|customized like HTML Table|

## $18 SOSL

- SOSL vs SOQL

  - SOSLはソート不可

  - グローバル検索はSOSL

  - 集計関数はSOQL ／ SOSLの場合、取得後にSize()で段階的に可能

  e.g.
  |case|SOSL|SOQL|
  |---|---|---|
  |特定の文言を含むすべてのレコードの名前とIDを取得|O|X|
  |特定のコースの開催コースを開催日順に取得|X|O|
  |名前に「Acme」を含む商談レコードの件数をカウント|△|O|

## $19 VisualForce page consideration

$19-1 Example Scenario

1. 認定資格チームは、各認定資格レコードにChatterフィードを含めることを希望

    -> 標準でOK

    設定 - Chatterのメニューから「フィード追跡を有効化」にチェックON

2. 認定資格チームは、開催コースの状況が「開催予定（Scheduled）」になったときのみ「開始日（Start Date）」項目が表示されることを希望

    -> 標準でOK

    - ページレイアウト

    - レコードタイプ

    - ワークフロールール　など

    レコードタイプに値を指定する項目を指定してレコードタイプごとのページレイアウトで制御可能
    ※ただしレコードタイプを多く定義することはメンテナンス性が落ちるため、実際には考慮要

      i. レコードを保存されたタイミングでレコードタイプを設定するワークフロー

      ii. レコードタイプごとのページレイアウトを定義

3. 認定資格チームは、コースレコードに表示される関連リストを[開催コース（CourseDeliveries）]関連リストのみにすることを希望

    -> 標準でOK

    - ページレイアウトの関連リストから不要分を削除して制御

4. 取引先責任者オブジェクトには多くの項目があり、すべての情報を表示するにはスクロールする必要がある。

    認定資格チームは、すべてのセクションと関連リストを、クリックにより参照できる個別のタブにすることを希望

    -> VisualForce

    - apex:tab を使用

5. 認定資格チームは、コースのリストビューのデザインを会社Webサイトのデザインにあわせることを希望

    -> VisualForce

    - CSS, etc.

## referense

### link

- 開発者ドキュメント > Force.com SOQL および SOSL リファレンス

  - Apex 開発者ガイド

  - SOQL および SOSLリファレンス

  - Salesforce Developer の制限および割り当てクイックリファレンス

- Cheat Sheet: Apex Code

  <http://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/SF_Apex_Code_cheatsheet_web.pdf>

- Cheat Sheet: Visualforce

  <http://resources.docs.salesforce.com/rel1/doc/en-us/static/pdf/SF_Visualforce_Developer_cheatsheet_web.pdf>
