const { readFile, writeFile } = require('fs');

readFile('interface_status.txt', 'utf8', (err, data) => {
	writeFile('interface_status.json', JSON.stringify(convertFileToJson(data)), err => {});
});

function convertFileToJson(data) {
	const dataArray = data.split('\n').map(x => x.trim());

	let params = dataArray[2]
		.toLowerCase()
		.replace(/\s{2,}/g, ' ')
		.split(' ');

	let lines = dataArray.slice(3, dataArray.length - 2);

	const output = lines.map(line => {
		return {
			[params[0]]: line.slice(0, 10).trim(),
			[params[1]]: line.slice(10, 29).trim(),
			[params[2]]: line.slice(29, 41).trim(),
			[params[3]]: line.slice(42, 52).trim(),
			[params[4]]: line.slice(52, 60).trim(),
			[params[5]]: line.slice(60, 67).trim(),
			[params[6]]: line.slice(67, line.length).trim(),
		};
	});

	return output;
}
