import React from "react";
import scrjs from "scriptjs";

/* code from a forgotten stackoverflow link! */
var parseXml;

if (window.DOMParser) {
    parseXml = function(xmlStr) {
        return ( new window.DOMParser() ).parseFromString(xmlStr, "text/xml");
    };
} else if (typeof window.ActiveXObject != "undefined" && new window.ActiveXObject("Microsoft.XMLDOM")) {
    parseXml = function(xmlStr) {
        var xmlDoc = new window.ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async = "false";
        xmlDoc.loadXML(xmlStr);
        return xmlDoc;
    };
} else {
    parseXml = function() { return null; }
}
/* end of code */

var jsonOut = {};
var xmlOut = "";


class XMLPager extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			xmlContent: "",
			jsonContent: {}
		}
		var reader = new FileReader();
		reader.onload = () => {
			if(reader.result){
				this.setState({
					xmlContent: reader.result
				});
				xmlOut = this.state.xmlContent;
				let set = (o)=>{
					this.setState({xmlContent: this.state.xmlContent, jsonContent: o});
					console.log("after loader: ",this.state);
				};
				scrjs("https://goessner.net/download/prj/jsonxml/xml2json.js", () => {
					let x = window.xml2json(parseXml(xmlOut),"");
					set(JSON.parse(x));
				});
			}
		}
		reader.readAsText(props.file);
		scrjs("https://goessner.net/download/prj/jsonxml/json2xml.js", () => {});
	}
	render() {
		console.log("from render: ",this.state.jsonContent);
		return <p>keys: {JSON.stringify(this.state.jsonContent)}</p> // temporary
	}
}

export default XMLPager;
