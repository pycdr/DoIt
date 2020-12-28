import React from "react";
import { Steps, Button } from "antd";
import { Pie } from 'ant-design-pro/lib/Charts';
import { CaretRightOutlined, CaretLeftOutlined } from "@ant-design/icons";
const { Step } = Steps;

function readtime(time_from, time_to){
	return 1; //temporary
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
				"y": readtime(x.from, x.to)
			});
		});
		console.log(this.pie_data);
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
				title="time info"
				subTitle="pie chart of progresses"
				total={() => (
					<span
						dangerouslySetInnerHTML={{
							__html: "total: "+2 //temporary
						}}
					/>
				)}
				data={this.pie_data}
				valueFormat={val => <span dangerouslySetInnerHTML={{ __html: val }} />}
				height={400}
	  		/>
		</>)
		
	}
}

export default ShowTimes;
