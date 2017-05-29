const webdriver = require('selenium-webdriver');
const By = webdriver.By;
require('chromedriver');


let chromeOptions = {'args': ['--test-type', '--window-size=600,1020']};
let chromeCapabilities = webdriver.Capabilities
	.chrome().set('chromeOptions', chromeOptions);
let driver = new webdriver.Builder()
	.withCapabilities(chromeCapabilities)
	.build();
driver.get('https://rubiks-cube-solver.com/');

async function click() {
  const path = [
    0, 0, 0, 1, 12, 12, 12, 1, 4, 3, 2, 5, 1, 0, 3, 4, 5, 1, 5, 4, 2, 3, 1, 0,
    2, 0, 3, 3, 2, 4, 5, 5, 0, 0, 2, 3, 4, 4, 2, 3, 4, 1, 0, 2
  ];
  await driver.findElement(By.className('rotationswitcher')).click();
  let buttons = await driver.findElements(
      By.xpath("//*[@class='wrapRotaciok']/div"));
  for(let i = 0; i < path.length; i++) {
    buttons[path[i]].click();
	}
	let append = [
		'R', 'R', 'R', 'B', 'B', 'B', 'F', 'M', 'B', 'L', 'L', 'U', 'U', 'U', 'U', 'U',
		'L', 'F', 'U', 'F', 'F', 'F', 'U', 'U', 'U', 'U', 'U', 'B', 'B', 'B', 'F', 'M',
		'B', 'B', 'B', 'F', 'M', 'R', 'R', 'R', 'B', 'B', 'B', 'F', 'M', 'U', 'U', 'U',
		'U', 'L', 'F', 'U', 'F', 'F', 'F', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'B',
		'U', 'U', 'B', 'B', 'B', 'F', 'M', 'U', 'U', 'U', 'L', 'F', 'U', 'F', 'F', 'F',
		'U', 'U', 'U', 'B', 'B', 'B', 'F', 'M', 'B', 'B', 'B', 'F', 'M', 'L', 'R', 'R',
		'R', 'B', 'B', 'B', 'F', 'M'
	]

	// let append = [
	// 	'R', 'R', 'R', 'B', 'B', 'B', 'F', 'M', 'B', 'U', 'U', 'U', 'U', 'U', 'L',
	// 	'F', 'U', 'F', 'F', 'F', 'U', 'U', 'U', 'U', 'U', 'B', 'B', 'B', 'F', 'M',
	// 	'U', 'B', 'B', 'U', 'U', 'U', 'B', 'B', 'B', 'F', 'M', 'B', 'B', 'B', 'B',
	// 	'F', 'M', 'B', 'B', 'B', 'B', 'F', 'M', 'U', 'U', 'L', 'B', 'B', 'B', 'F',
	// 	'M', 'U', 'U', 'U', 'B', 'B', 'U', 'B', 'B', 'B', 'F', 'M', 'B', 'B', 'B',
	// 	'F', 'M', 'U', 'U', 'U', 'L', 'F', 'U', 'F', 'F', 'F', 'U', 'U', 'U', 'B',
	// 	'B', 'B', 'F', 'M', 'B', 'B', 'B', 'F', 'M', 'R', 'R', 'R', 'B', 'B', 'B',
	// 	'F', 'M'
	// ]

	let converted = append.map((letter) => {
		if(letter == 'M') {
			return 14;
		} else if(letter == 'L') {
			return 0;
		} else if(letter == 'R') {
			return 1;
		} else if(letter == 'U') {
			return 2;
		} else if(letter == 'D') {
			return 3;
		} else if(letter == 'F') {
			return 4;
		} else {
			return 5;
		}
	})

	for(let i = 0; i < converted.length; i++) {
    buttons[converted[i]].click();
	}

	let rotations = converted.filter((number) => number == 14)

	console.log(rotations.length);
	console.log(converted.length);

}

click();
