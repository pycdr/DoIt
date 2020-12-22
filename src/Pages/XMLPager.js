import React from "react";

class XMLPager extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			xmlContent: ""
		}
		var reader = new FileReader();
		reader.onload = () => {
			if(reader.result){
				this.setState({
					xmlContent: reader.result
				});
			}
		}
		reader.readAsText(props.file);
	}
	render() {
		/* continue here */
		return <p>{this.state.xmlContent}</p> // temporary
	}
}

export default XMLPager;
