const path = require('path');
const PATHS = {
    app: path.resolve(__dirname,'app'),
    build: path.resolve(__dirname,'build')
};
module.exports = {
    entry: {
        app: PATHS.app + "/index.js"
    },
    output: {
        path: PATHS.build,
        filename: 'bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                loaders: ['style-loader','css-loader']
            }
        ]
    },
    devServer: {
        host: '127.0.0.1',
        port: 4040,
    }
};
