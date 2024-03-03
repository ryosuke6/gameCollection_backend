import json

def lambda_handler(event, context):
    # リクエストから情報を取得
    body = json.loads(event['body'])
    player_name = body.get('player_name')  # プレイヤーの名前
    password = body.get('password')  # パスワード

    # ここでマッチングロジックを実装（例: DynamoDBを検索して、プレイヤー名とパスワードが一致するルームを探す）

    # マッチング結果を返す
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Match request received',
            'player_name': player_name,  # レスポンスにプレイヤー名を含める
        })
    }
