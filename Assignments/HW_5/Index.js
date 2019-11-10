var AWS = require('aws-sdk');
var dynamo = new AWS.DynamoDB.DocumentClient();

exports.handler = (event, context, callback) => {
    //console.log('Received event:', JSON.stringify(event, null, 2));

    const done = (err, res) => callback(null, {
        statusCode: err ? '400' : '200',
        body: err ? err.message : JSON.stringify(res),
        headers: {
            'Content-Type': 'application/json',
        },
    });
    const payload = {};
    if (event.tableName) {
        payload.TableName = event.tableName;
    }
    if (event.Item) {
        payload.Item = event.Item;
    }
    if (event.Key) {
        payload.Key = event.Key;
    }
    switch (event.operation) {
        case 'DELETE':
            dynamo.delete(payload, done);
            break;
        case 'GET':
            dynamo.scan(payload, done);
            break;
        case 'POST':
            dynamo.put(payload, done);
            break;
        case 'PUT':
            dynamo.update(payload, done);
            break;
        default:
            done(new Error(`Unsupported method "${event.httpMethod}"`));
    }
};
