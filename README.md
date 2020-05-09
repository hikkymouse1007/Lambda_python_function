# Lambda_python_funciton
reference: https://docs.aws.amazon.com/ja_jp/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-http-redirect

## API Gatewayのセットアップ
- API名の直下にGetメゾットを使って運用する。 ex) https://xxxapi/stage_name/
- リソース名は付けない。
- パスパラメータなどは不要。
- プロキシ統合はオフのまま設定
プロキシ統合とは
https://qiita.com/yuuwatanabe/items/a3bd65e709f20574b6db
