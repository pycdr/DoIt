const {app, BrowserWindow} = require("electron");
const url = require("url");
const path = require("path");

let win;

app.on("ready", ()=>{
	win = new BrowserWindow({
		width: 600,
		height: 400
	});
	win.loadURL(url.format({
		pathname: path.join(__dirname, "home.html"),
		protocol: "file:",
		slashes: true
	}));
});
