import React from "react";
import { Steps, Button } from "antd";
import { Pie } from 'ant-design-pro/lib/Charts';
import { CaretRightOutlined, CaretLeftOutlined } from "@ant-design/icons";
const { Step } = Steps;

function readtime(time_from, time_to){
	time_from = time_from.split(":");
	if (time_from.length === 0) time_from = 0;
	else if (time_from.length === 1) time_from = Number(time_from[0])*60*60;
	else if (time_from.length === 2) time_from = Number(time_from[0])*60*60+Number(time_from[1])*60;
	else if (time_from.length === 3) time_from = Number(time_from[0])*60*60+Number(time_from[1])*60+Number([2]);
	else {throw "give a valid time for <time_from>"; return 0;}
	
	time_to = time_to.split(":");
	if (time_to.length === 0) time_to = 0;
	else if (time_to.length === 1) time_to = Number(time_to[0])*60*60;
	else if (time_to.length === 2) time_to = Number(time_to[0])*60*60+Number(time_to[1])*60;
	else if (time_to.length === 3) time_to = Number(time_to[0])*60*60+Number(time_from[1])*60+Number([2]);
	else {throw "give a valid time for <time_to>"; return 0;}
	
	let d = time_to-time_from;
	return d;
}
function showtime(sec){
	if (sec <= 0) {throw "<time_from> must be bigger than <time_to>"; return 0;}
	let out;
	if (sec < 60) out = sec+"s";
	else if (sec >= 60 && sec < 3600) out = Math.floor(sec/60) + "m " + (sec%60) + "s";
	else if (sec >= 3600) out = Math.floor(sec/3600) + "h " + (Math.floor((sec%3600)/60)) + "m " + (sec%60) + "s";
	return out;
}

class ShowTimes extends React.Component {
	constructor(props){
		super(props);
		this.data = props.data;
		this.state = {step: 0};
		this.pie_data = [];
		this.data.map((x)=>{
			this.pie_data.push({
				"x": x.title+" - "+x.description,
				"y": readtime(x["from"], x["to"])
			});
		});
	}
	render(){
		return (<>
			<Steps current={this.state.step}>
				{this.data.map(x=>(
					<Step
						title = {x.title}
						description = {x.description}
						subTitle = {x.from+" > "+x.to}
					/>
				))}
			</Steps>
			{this.data.length<2?<></>:(<>
				<Button
					onClick = {()=>{
						this.setState({
							step: (
								this.data.length + this.state.step-1
							)%this.data.length})
					}}
					icon = {<CaretLeftOutlined />}
				>previous</Button>
				<Button
					onClick = {()=>{
						this.setState({
							step: (
								this.data.length + this.state.step+1
							)%this.data.length})
					}}
					icon = {<CaretRightOutlined />}
				>next</Button>
			</>)}
			<Pie
				hasLegend
				title = "time info"
				subTitle = "pie chart of progresses"
				total = {() => (
					<span
						dangerouslySetInnerHTML={{
							__html: "total: " + showtime(this.pie_data.reduce((pre, now) => pre.y + now.y))
						}}
					/>
				)}
				data = {this.pie_data}
				valueFormat = {val => <><br /><span dangerouslySetInnerHTML={{ __html: showtime(val) }} /></>}
				height = {400}
	  		/>
		</>)
		
	}
}

export default ShowTimes;
