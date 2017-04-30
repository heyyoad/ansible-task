let express = require('express');
let bodyParser = require('body-parser');
let path = require('path');
let index = require('./routes/index');

let app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // support encoded bodies
app.use(express.static(path.join(__dirname, 'public')));
app.use('/static', express.static(path.join(__dirname, 'resources')));
app.use('/', index);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
    res.writeHead(404);
    res.end("Page Does not exists");
});


module.exports = app;
