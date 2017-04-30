let express = require('express');
const fs = require('fs');
const path = require('path');
let router = express.Router();

let counter = 0;

/* GET home page. */
router.get('/', function(req, res) {
    res.render('index', { title: "Counting: " + counter})
});

router.post('/', function(req, res) {
    counter ++;
    res.send("moo");
});

module.exports = router;
