const path = require('path');
const HtmlWebPackPlugin = require('html-webpack-plugin');

module.exports = {
    target: 'web',
    mode: 'development',
    entry: './src/index',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'app.bundle.js'
    },
    resolve: {
        extensions: ['.ts', '.tsx', '.js', '.json']
    },
    module: {
        rules: [{
            // Include ts, tsx, js, and jsx files.
            test: /\.(ts|js)x?$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
        },
        {
            test: /\.html$/,
            use: [
                {
                    loader: "html-loader",
                    options: {minimize: true}
                }
            ]
            
        },
        {
            test: /\.s[ac]ss$/i,
            use: [
                "style-loader",
                "css-loader",
                "sass-loader"
            ]
        },
    {
        test: /\.css$/i,
        use: [
            "style-loader",
            "css-loader"
        ]
    }],
    },
    devServer: {
        contentBase: './',
        port: 3001
    },
    plugins: [
        new HtmlWebPackPlugin({
            template: "./public/index.html",
            filename: "./index.html"
        })
    ]
};