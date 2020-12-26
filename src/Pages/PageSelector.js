import React from "react";
import Year from "./YearPage.js";
import Month from "./MonthPage.js";
import Day from "./YearPage.js";
import Time from "./TimePage.js";

class PageSelector extends React.Component {
	constructor(props){
		super(props);
		this.data = props.data;
	}
	render(){
		if ("data" in this.data){
			return <PageSelector data={this.data["data"]} />
		} else {
			let years, months, days, times;
			
			if (this.data.year === undefined) years = [];
			else if (!Array.isArray(this.data.year)) years = Array(this.data.year);
			else years = this.data.year;
			
			if (this.data.month === undefined) months = [];
			else if (!Array.isArray(this.data.month)) months = Array(this.data.month);
			else months = this.data.month;
			
			if (this.data.day === undefined) days = [];
			else if (!Array.isArray(this.data.day)) days = Array(this.data.day);
			else days = this.data.day;
			
			if (this.data.time === undefined) times = [];
			else if (!Array.isArray(this.data.time)) years = Array(this.data.time);
			else times = this.data.time;
			
			return <>{JSON.stringify(this.data)}</> //temporary
		}
	}
}

export default PageSelector;
