import "./style.css";
import React from "react";

class OpenButton extends React.Component{
	constructor(props){
		super(props)
		this.state = {
			onpress: props.open
		}
	}
	render(){
		return (
			/* main idea: https://codepen.io/atloomer/pen/JEaRWX*/
			<div className="button" id="button-open">
				<div id="circle"></div>
				<a onClick={this.state.onpress}>+</a>
			</div>
		)
	}
}

export default OpenButton;
