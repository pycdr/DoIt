import './App.css';
import React from "react";
import OpenButton from "./Buttons/OpenButton.js";
import Page from "./Pages/XMLPager.js";

class MainPage extends React.Component{
	constructor(props) {
		super(props);
		this.state = {
			path: ""
		}
	}
	getPath(){
		/* continue here */
	}
	render() {
		if (this.state.path === ""){
			return <OpenButton open={this.getPath}></OpenButton>
		}
		else {
			return <Page file={this.state.path} />
		}
	}
}
const App = () => (
	<MainPage />
);

export default App;
