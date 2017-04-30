var express = require('express');
const fs = require('fs');
const path = require('path');
var router = express.Router();
var functions = require('../functions')

/* GET home page. */
router.get('/', function(req, res) {
    let images = functions.getImagesFromDir("./resources");
    res.render('index', { title: 'Pandas are the best', images: images })
});

module.exports = router;
