import "./style.css";
import React from "react";

class OpenButton extends React.Component{
	constructor(props){
		super(props);
		this.onpress = props.open;
		this.send_path = props.get;
		this.set_path = props.set;
		this.onDragOver = (e) => {
			e.preventDefault();
		}
		// this.onDragEnter = (e) => {}
		this.onDrop = (e) => {
			e.preventDefault();
			this.set_path(e.dataTransfer.files[0]);
		}
	}
	render(){
		return (
			/* main idea: https://codepen.io/atloomer/pen/JEaRWX*/
			<div
				className="button" id="button-open"
				onDragEnter={this.onDragEnter}
				onDragOver={this.onDragOver}
				onDrop={this.onDrop}
				onClick={this.onpress}
			>
				<div id="circle"></div>
				<a>+</a>
				<input type="file" id="file-input" onChange={this.send_path} accept=".xml"/>
			</div>
		)
	}
}

export default OpenButton;
