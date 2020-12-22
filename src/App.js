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
		this.openDialog = this.openDialog.bind(this);
		this.getPath = this.getPath.bind(this);
		this.setPath = this.setPath.bind(this);
	}
	openDialog(){
		this.file_input = document.getElementById("file-input");
		this.file_input.click();
	}
	getPath(){
		if (this.file_input.files){
			this.setState({path: this.file_input.files[0]});
		}
	}
	setPath(path){
		if (path) {
			this.setState({path: path});
		}
	}
	render() {
		if (this.state.path === ""){
			return (
				<OpenButton
					open={this.openDialog}
					get={this.getPath}
					set={this.setPath}>
				</OpenButton>
			)
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
