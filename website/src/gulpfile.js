const gulp = require('gulp');
const browserify = require('browserify');
const source = require('vinyl-source-stream');
const streamify = require('gulp-streamify');
const uglify = require('gulp-uglify');
const rename = require('gulp-rename');
const concat = require('gulp-concat');
const sass = require('gulp-sass');
const uglifycss = require('gulp-clean-css');
const clean = require('gulp-clean');
const imagemin = require('gulp-imagemin'); 
const watch = require('gulp-watch');
const babel = require('gulp-babel');


// Combines the Javascript files in /js/ into app.js,
gulp.task('concat', function(){
	return gulp.src('./js/*')
		.pipe(concat('./app.js'))
		.pipe(babel({
			presets: ['env']
		}))
		.pipe(gulp.dest('./'));
});
// Browserify's app.js and puts it into assets/js, 
// Minifies the app.js into app.min.js and puts it into assets/js as well
gulp.task('js', ['concat'], function(){
	var bundleStream = browserify('./app.js').bundle();
	return bundleStream
		.pipe(source('./app.js'))
		.pipe(gulp.dest('../assets/js/'))
		.pipe(streamify(uglify()))
		.pipe(rename({
			suffix: '.min'
		}))
		.pipe(gulp.dest('../assets/js/'));
});
// Removes all images in assets/img in preparation for image minify
gulp.task('clear-img', function() {
	return gulp.src('../assets/img/*')
		.pipe(clean({force: true}));
});
// Minifies the images in /img/ and puts them in the assets/img folder
gulp.task('img', ['clear-img'], function() {
	return gulp.src('img/*')
		.pipe(imagemin())
		.pipe(gulp.dest('../assets/img/'));
});
// Combines the Scss files in /scss/ and puts them in the assets/css folder as style.css
// Minifies the Scss files into scss.min.js and puts it into assets/css as well
gulp.task('scss', function() {
	return gulp.src('./scss/style.scss')
		.pipe(sass())
		.pipe(gulp.dest('../assets/css/'))
		.pipe(uglifycss())
		.pipe(rename({
			suffix: '.min'
		}))
		.pipe(gulp.dest('../assets/css/'));
});
// Executes all of the tasks in one command
gulp.task('all', ['js', 'img', 'scss']);
// Watches for changes in each of the directories and calls the respective gulp task

gulp.task('watch', function() {
	gulp.watch('js/**/*', ['js']);
	gulp.watch('scss/**/*', ['scss']);
	gulp.watch('img/**/*', ['img']);
});
