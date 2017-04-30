/**
 * Created by yoadf on 4/28/2017.
 */

const fs = require('fs');
const path = require('path');

module.exports = {
    // dirPath: target image directory
    getImagesFromDir: function (dirPath) {

        // All images holder
        let allImages = [];

        // Directory iterator
        let files = fs.readdirSync(dirPath);

        // Iterates over the files and pushes jpg and png images to allImages array.
        for (file of files) {
            let fileLocation = path.join(dirPath, file);
            var stat = fs.statSync(fileLocation);
            if (stat && stat.isDirectory()) {
                getImagesFromDir(fileLocation); // process sub directories
            } else if (stat && stat.isFile() && ['.jpg', '.png'].indexOf(path.extname(fileLocation)) !== -1) {
                allImages.push('static/' + file); // push all .jpf and .png files to all images
            }
        }

        // returns the images array
        return allImages;
    }
};