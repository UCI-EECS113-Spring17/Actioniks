const webdriver = require('selenium-webdriver');
const By = webdriver.By;
require('chromedriver');


let chromeOptions = {'args': ['--test-type', '--window-size=1000,1020']};
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
}

click();
// driver.quit();
